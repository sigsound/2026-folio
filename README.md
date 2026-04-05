# Nick Woods Portfolio - Astro

A static portfolio website built with Astro, migrated from Gatsby + Contentful to Astro + Markdown.

## 🚀 Tech Stack

- **Framework**: Astro v6 (zero-JS static site generator)
- **Content**: Markdown files with frontmatter (migrated from Contentful)
- **Styling**: CSS Custom Properties with light/dark themes
- **Interactive Elements**: Vanilla JS for theme toggle and THREE.js hero animation
- **Typography**: Google Fonts (Bodoni Moda + IBM Plex Mono)

## 📁 Project Structure

```
├── src/
│   ├── components/
│   │   ├── MinimalistHero.astro    # THREE.js background animation
│   │   └── ProjectCard.astro       # Project preview cards
│   ├── content/
│   │   ├── projects/               # Case study markdown files
│   │   └── about/                  # About page content
│   ├── layouts/
│   │   └── Base.astro             # Main layout with theme system
│   ├── pages/
│   │   ├── index.astro            # Homepage
│   │   ├── case-studies/[slug].astro # Dynamic case study pages
│   │   └── 404.astro              # Error page
│   └── styles/
│       └── global.css             # Global styles and theme variables
├── public/
│   └── images/                    # Static assets (logos, project images)
└── astro.config.mjs               # Astro configuration
```

## 🛠️ Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🎨 Features

- **Zero JavaScript**: Static site generation with selective hydration
- **Dark/Light Theme**: Automatic system preference detection with manual toggle
- **Interactive Hero**: THREE.js network animation background
- **Responsive Design**: Mobile-first responsive layout
- **Case Studies**: Dynamic pages generated from markdown content
- **Performance**: Optimized images and minimal bundle size

## 📝 Content Management

Content is managed through markdown files in `src/content/`:

- **Projects**: Each case study is a markdown file with frontmatter metadata
- **About**: Personal information and profile content

To add a new project:
1. Create a new `.md` file in `src/content/projects/`
2. Add the required frontmatter fields
3. Write the content in markdown
4. Add images to `public/images/projects/[project-name]/`

## 🎯 Migration Notes

This project was successfully migrated from:
- **Gatsby + React + Contentful** → **Astro + Markdown**
- **Styled Components** → **CSS Custom Properties**
- **GraphQL** → **Content Collections**
- **React State Management** → **Vanilla JS**

All visual design and functionality has been preserved while achieving:
- Faster build times
- Zero runtime JavaScript (except for interactive components)
- Simplified content management
- Better performance scores