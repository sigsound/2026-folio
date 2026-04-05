import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  site: 'https://nickwoods.us',
  build: {
    assets: 'assets'
  },
  markdown: {
    shikiConfig: {
      theme: 'github-light',
      wrap: true
    }
  }
});