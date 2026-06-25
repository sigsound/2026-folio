# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- **Dev server:** `npm run dev`
- **Production build:** `npm run build` (outputs to `/dist`)
- **Preview build:** `npm run preview`
- No linter or test runner configured.

## Architecture

This is a static portfolio site built with **Astro 4.x** (`output: 'static'`). The only dependency is Astro itself; THREE.js is loaded via CDN (Skypack) at runtime.

### Content Collections

Content lives in `src/content/` as Markdown with YAML frontmatter, validated by Zod schemas in `src/content.config.ts`:

- **projects/** — Case study pages. Schema: `title`, `role`, `timeline`, `impact`, `thumbnail`, `hero`, optional `hisImage`, `videos` (string array), `media` (array of `{src, alt}`), `order`.
- **about/** — Single `index.md` with `headline` and `profileImage`.

To add a project: create `src/content/projects/<slug>.md`, add images to `public/images/projects/<slug>/`.

### Routing

- `/` — `src/pages/index.astro` (homepage with project grid, about section, skills)
- `/case-studies/<slug>` — `src/pages/case-studies/[slug].astro` (dynamic from projects collection)
- `/404` — `src/pages/404.astro`

### Layout & Components

- `src/layouts/Base.astro` — Single shared layout. Handles header, theme init script (runs before paint to avoid flash), scroll-triggered header state, and scroll reveal animations via IntersectionObserver.
- `src/components/MinimalistHero.astro` — THREE.js animated network background with mouse interaction. Theme-aware colors.
- `src/components/ProjectCard.astro` — Card with frosted-glass hover overlay on desktop, always-visible caption on mobile.

### Styling

All in plain CSS (no preprocessor, no Tailwind). Theme system uses CSS Custom Properties:

- Light/dark themes auto-detected via `prefers-color-scheme`, with time-based fallback (dark after 6pm).
- Global styles in `src/styles/global.css`, plus scoped `<style>` blocks in `.astro` components.
- Responsive breakpoint at 1023px.

### Key Patterns

- **Progressive enhancement:** `.js` class on `<html>` gates JS-only behaviors in CSS. Content works without JS.
- **Zero JS by default:** Pages ship no runtime JS unless they include interactive components.
- **Vimeo embeds:** Case study template converts various Vimeo URL formats to player embeds.
- **Scroll reveals:** Elements with `.reveal` class animate in via IntersectionObserver.
- **Static assets** go in `public/` (served as-is, no processing). Images organized by `public/images/projects/<slug>/`.
