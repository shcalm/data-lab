import importlib.util
from pathlib import Path
import unittest
from datetime import datetime, timezone


class ChannelRankingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).with_name('build_results.py')
        if not path.exists():
            cls.build = None
            return
        spec = importlib.util.spec_from_file_location('ask_show_build', path)
        cls.build = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.build)

    def test_channels_match_self_posts_and_show_without_confusing_external_questions(self):
        self.assertIsNotNone(self.build, 'Ask/Show exporter is not implemented')
        classify = self.build.archive_channel
        self.assertEqual(classify('Ask HN: How?', ''), 'ask')
        self.assertEqual(classify('Tell HN: Thank you', None), 'ask')
        self.assertIsNone(classify('Ask HN: How?', 'https://example.com'))
        self.assertEqual(classify(' show HN：A useful tool', ''), 'show')
        self.assertEqual(classify('Show YC: Early project', 'https://example.com'), 'show')
        self.assertIsNone(classify('How to show HN a tool', 'https://example.com'))

    def test_top10_uses_score_time_id_and_keeps_original_fields(self):
        self.assertIsNotNone(self.build, 'Ask/Show exporter is not implemented')
        rows = [{'id': i, 'score': 100, 'time_utc': '2020-01-01T00:00:00Z',
                 'comments': 1000-i, 'archive_score': 1} for i in range(14, 0, -1)]
        ranked = self.build.rank_rows(rows)
        self.assertEqual([r['id'] for r in ranked], list(range(1, 11)))
        self.assertEqual([r['rank'] for r in ranked], list(range(1, 11)))
        self.assertEqual(ranked[0]['archive_score'], 1)
        self.assertNotIn('rank', rows[0])
        self.assertEqual(self.build.rank_rows([]), [])

    def test_calendar_keeps_empty_and_sparse_months(self):
        self.assertIsNotNone(self.build, 'Ask/Show exporter is not implemented')
        self.assertEqual(self.build.common.calendar_months('2006-10', '2007-01'),
                         ['2006-10', '2006-11', '2006-12', '2007-01'])
        self.assertEqual(len(self.build.rank_rows([{'id': 1, 'score': 1, 'time_utc': '2007-02-01T00:00:00Z'}])), 1)

    def test_original_show_with_removed_tag_and_low_snapshot_score_can_still_win(self):
        when = datetime(2023, 8, 1, tzinfo=timezone.utc)
        row = {'id': 42, 'channel': 'show', 'title': 'Show HN: An original project',
               'time': when, 'url': 'https://example.com', 'score': 3,
               'descendants': 0, 'by': 'maker', 'text': ''}
        hit = {'objectID': '42', 'created_at_i': int(when.timestamp()), 'points': 963,
               'num_comments': 100, 'title': 'An edited title', '_tags': ['story']}
        checked, mismatches = self.build.reconcile_candidates('show', '2023-08', [(hit, '2026-11-19T00:00:00Z')], {42: row})
        self.assertEqual(checked[0]['score'], 963)
        self.assertEqual(checked[0]['archive_score'], 3)
        self.assertEqual(checked[0]['title'], row['title'])
        self.assertEqual(checked[0]['category_source'], 'archive')
        self.assertEqual(mismatches, {})
        hit['created_at_i'] += 3600
        checked, mismatches = self.build.reconcile_candidates('show', '2023-08', [(hit, '2026-11-19T00:00:00Z')], {42: row})
        self.assertEqual(checked, [])
        self.assertIn(42, mismatches)

    def test_generic_candidate_pagination_covers_ties_and_stops_when_all_originals_matched(self):
        rows = [{'score': 100}] * 10
        response = {'hits': [{'points': 100}] * 100, 'nbHits': 500}
        self.assertFalse(self.build.candidate_boundary(rows, 50, 20, response, 100))
        response['hits'][-1]['points'] = 99
        self.assertTrue(self.build.candidate_boundary(rows, 50, 20, response, 100))
        response['hits'][-1]['points'] = 100
        self.assertTrue(self.build.candidate_boundary(rows[:3], 3, 3, response, 100))
        with self.assertRaisesRegex(ValueError, 'pagination ended'):
            self.build.candidate_boundary(rows, 50, 20, {'hits': [], 'nbHits': 500}, 100)
        with self.assertRaisesRegex(ValueError, 'API error'):
            self.build.candidate_boundary(rows, 50, 20, {'hits': [], 'nbHits': 0, 'message': '1000 hit limit'}, 1000)

    def test_api_limit_restarts_at_an_inclusive_score_window(self):
        pages = [{'response': {'page': 9, 'hits': [{'points': 68}]}}]
        self.assertEqual(self.build.next_generic_page(pages), (0, 68))
        pages.append({'score_ceiling': 68, 'response': {'page': 0, 'hits': [{'points': 60}]}})
        self.assertEqual(self.build.next_generic_page(pages), (1, 68))


if __name__ == '__main__':
    unittest.main()
