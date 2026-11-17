import type { APIRoute, GetStaticPaths } from 'astro';
import { projects, getProject } from '../../lib/data.mjs';

export const getStaticPaths: GetStaticPaths = () => projects.map((project) => ({ params: { slug: project.exportSlug }, props: { id: project.id } }));

export const GET: APIRoute = ({ props }) => {
  const { id, title, source, entries } = getProject(props.id);
  return new Response(JSON.stringify({ id, title, source, entries }, null, 2) + '\n', {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
