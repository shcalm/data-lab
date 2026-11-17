import type { APIRoute, GetStaticPaths } from 'astro';
import { projects, getProject, toCsv } from '../../lib/data.mjs';

export const getStaticPaths: GetStaticPaths = () => projects.map((project) => ({ params: { slug: project.exportSlug }, props: { id: project.id } }));

export const GET: APIRoute = ({ props }) => new Response(toCsv(getProject(props.id).entries), {
  headers: { 'Content-Type': 'text/csv; charset=utf-8' },
});
