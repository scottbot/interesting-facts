# Random Bluesky Fact

A deliberately tiny Hugo site. Each page load chooses one verified fact and
shows only its verbatim Bluesky text, the author's name, and their handle.

There is no theme, JavaScript framework, package manager, bundler, or minifier.
The complete front end is:

- `layouts/index.html`
- `static/css/style.css`
- `static/js/random-fact.js`
- `static/data/facts.json`

## Deploy to GitHub Pages

1. Create an empty GitHub repository and put these files in it.
2. In the repository settings, set **Pages → Source** to **GitHub Actions**.
3. Push to the `main` branch.

The included workflow builds and deploys the site automatically. Netlify,
Cloudflare Pages, and similar hosts can also deploy it with `hugo` as the build
command and `public` as the output directory.
