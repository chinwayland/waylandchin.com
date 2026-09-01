# waylandchin.com

Personal professional platform for Wayland Chin.

## Site sections

- Home
- Education & Innovation
- Educational Innovation Projects
- Business & Operations
- About
- CV & Documents
- Contact

The site is a static website hosted with GitHub Pages. The `CNAME` file must remain in the repository so the custom domain continues to work.

The Pages workflow also builds the public travel calendar from the separate
`chinwayland/travel-calendar` source repository. Its private TripIt URL is stored
only in this repository's `TRIPIT_ICAL_URL` Actions secret, and the published
calendar is refreshed every 15 minutes.
