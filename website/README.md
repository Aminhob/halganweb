# HALGAN website

A cinematic, responsive, multi-page HALGAN boxing website. Built with semantic static HTML, Teko, CSS and small client-side JavaScript. Three.js is a separate lazy-loaded chunk used only when a visitor requests a 3D preview.

## Run

```sh
npm ci
npm run build
npm run check
```

Serve `dist/` from any static host with directory index support. All assets and dependencies are local; no CDN is required at runtime. Do not serve the project root: it contains internal audit and development documentation.

The website is isolated from original HALGAN/Unity assets. `src/catalog.json` is the sanitized structured content model. It holds development designs, not verified sale eligibility or prices. The complete preparation source is not distributed to visitors.

## Content and pages

Home; The Game; Fighters & Legends; Game Modes; HALGAN City; Shop; Rewards & Progression; Media & Gallery; Development Journey; News; Coming Soon; About. Twenty item pages, seventeen fighter pages and three verified development articles give 52 routes plus 404.

- Interactive, on-demand GLB viewers with rotation, zoom, reset, fullscreen and keyboard controls.
- Search/category/name sorting, empty states and up-to-three-item comparison.
- Interactive conceptual city district selector and artwork lightbox.
- Motion pause, reduced-motion preference, mobile navigation and dialog focus restoration.
- Honest planned/coming-soon states for undocumented systems. No fake payments, notifications, trailer, gameplay or release countdown.

## Assets

The private Site source includes optimized web derivatives under `public/assets/`. In the GitHub repository, these are generated from the adjacent original asset folders rather than duplicating the binaries. `npm run build` prepares them automatically when missing; install Git LFS and fetch the repository assets first. To regenerate them explicitly from the unmodified official asset repository:

```sh
node scripts/prepare-assets.mjs /absolute/path/to/halganweb
npm run build
npm run check
```

Only the four approved Teko weights are copied. Original HALGAN logo/mascot art and twenty static model previews are reused. Original materials/extensions are retained. Texture dimensions are capped at 1024 and WebP encoded; this is a web derivative process, not a source modification. Excluded partial robes are never copied.

## Publication

The initial site is owner-private and noindex while approvals and integrations are pending. Read [docs/HANDOVER.md](docs/HANDOVER.md) before public release. The checked-in hosting configuration belongs to this private Sites project; generic hosts can serve `dist/` directly.

## Validation

`npm run check` verifies all local route/asset links, anchors, semantic headings, image descriptions, metadata, all GLB meshes/textures and meaningful DOM interactions. It checks absence of invented prices, purchase CTAs and prohibited font weights.

Browser/GPU rendering, actual responsive screenshots and Lighthouse measurement could not be performed: the supported browser control skill is unavailable in this session. No performance score or visual-browser pass is claimed. See [docs/QA.md](docs/QA.md).
