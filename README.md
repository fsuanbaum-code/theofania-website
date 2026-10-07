# Theofania website

Static site for Theofania: QHHT, BQH and psychic readings in Berlin and online.
Plain HTML and CSS, no build step, no paid platform. Fonts and images are served
from the site itself (no Google or other third-party requests, which keeps it GDPR friendly).

## Editing

- Each page is its own `.html` file. Shared styles live in `assets/css/style.css`.
- `build.py` holds all page content in one place and regenerates every page
  (`python3 build.py .`). Use it when changing the header, footer or menu.
- Anything highlighted in yellow (class `todo`) is a placeholder to fill in.

## Hosting

Served by GitHub Pages from the `main` branch root.
