# waylandchin.com

Personal professional platform for Wayland Chin.

## Site sections

- Home
- Education & Innovation
- Educational Innovation Projects
- About
- CV & Documents
- Contact

The site is a static website hosted with GitHub Pages. The `CNAME` file must remain in the repository so the custom domain continues to work.

The Pages workflow also builds the public travel calendar from the separate
`chinwayland/travel-calendar` source repository. Its private TripIt URL is stored
only in this repository's `TRIPIT_ICAL_URL` Actions secret, and the published
calendar is refreshed every 15 minutes.

The site presents one unified professional profile. The former `/business/` route redirects to `/about/` for existing bookmarks.

## Content editing

See [EDITING.md](EDITING.md) for Pages CMS instructions. Editable content lives in
`content/*.json`; `.pages.yml` defines the editor. `templates/` holds layout and
`scripts/build-content.py` renders the 13 pages during deployment. The original
root HTML pages are migration snapshots, not the live content source; do not edit
them for future content changes. Build locally with
`python3 scripts/build-content.py --output /tmp/wayland-preview` and serve that
output with the site's assets copied alongside it. Tests use only Python's
standard library: `python3 -m unittest discover -s scripts -p 'test_*.py'`.
