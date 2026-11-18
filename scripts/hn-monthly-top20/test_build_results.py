import unittest
from datetime import datetime, timezone

import build_results as build


def row(item_id, time, score, **extra):
    return {'id': item_id, 'time_utc': time, 'title': f'Story {item_id}',
            'score': score, 'comments': 3, 'archive_score': 1,
            'archive_comments': 0, **extra}


class RankingTests(unittest.TestCase):
    def test_months_include_empty_calendar_months(self):
        self.assertEqual(build.calendar_months('2006-10', '2007-02'),
                         ['2006-10', '2006-11', '2006-12', '2007-01', '2007-02'])

    def test_ties_use_utc_time_then_id_without_comment_tiebreak(self):
        rows = [row(3, '2024-03-01T00:00:00Z', 30, comments=900),
                row(2, '2024-02-29T23:59:59Z', 30),
                row(1, '2024-02-29T23:59:59Z', 30),
                row(4, '2024-03-01T00:00:00Z', 40)]
        ranked = build.rank_rows(rows)
        self.assertEqual([r['id'] for r in ranked], [4, 1, 2, 3])
        self.assertEqual([r['rank'] for r in ranked], [1, 2, 3, 4])
        self.assertNotIn('rank', rows[0])
        self.assertEqual(ranked[0]['archive_score'], 1)
        self.assertEqual(build.rank_rows([]), [])

    def test_top20_and_safe_plain_text_excerpts(self):
        rows = [row(i, '2024-01-01T00:00:00Z', i) for i in range(25)]
        self.assertEqual([r['id'] for r in build.rank_rows(rows)], list(range(24, 4, -1)))
        self.assertEqual(build.plain_excerpt('<p>A &amp; B</p><p>C<br>D</p>'), 'A & B C D')
        self.assertEqual(build.plain_excerpt(None), '')

    def test_official_exception_uses_checked_score_without_inventing_comment_total(self):
        source = {'id': 12, 'title': 'Original title', 'by': 'author',
                  'time': datetime(2023, 7, 25, tzinfo=timezone.utc),
                  'url': 'https://example.com/original', 'text': '',
                  'score': 1202, 'descendants': 3}
        response = {'checked_at': '2026-11-18T00:00:00Z', 'response': {
            'id': 12, 'time': int(source['time'].timestamp()), 'type': 'story',
            'score': 1205, 'dead': True, 'kids': [21, 22]}}
        entry = build.firebase_entry(source, response)
        self.assertEqual(entry['title'], 'Original title')
        self.assertEqual(entry['url'], source['url'])
        self.assertEqual((entry['score'], entry['score_source']), (1205, 'firebase'))
        self.assertEqual((entry['comments'], entry['comments_source']), (3, 'archive'))
        self.assertTrue(entry['current_dead'])
        self.assertEqual(entry['archive_score'], 1202)
        response['response']['descendants'] = 8
        self.assertEqual(build.firebase_entry(source, response)['comments'], 8)
        self.assertEqual(build.firebase_entry(source, response)['comments_source'], 'firebase')
        response['response']['time'] += 1
        with self.assertRaises(ValueError):
            build.firebase_entry(source, response)


if __name__ == '__main__':
    unittest.main()
