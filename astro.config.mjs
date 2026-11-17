import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://shcalm.github.io',
  base: '/data-lab',
  trailingSlash: 'always',
  output: 'static',
  build: { format: 'directory' },
});
