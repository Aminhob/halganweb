# HALGAN verification record

Automated result: **PASS** — 52 routes, 2,820 local references, 306 image alt attributes and 20 valid GLBs.

## Automated checks

Run `npm run build` and `npm run check` from the website directory.

- All 52 independent page routes plus a custom 404 are generated.
- Every local link, cross-page anchor, stylesheet, script, image and referenced model resolves to a build artifact.
- Each route has one H1, semantic main content, a unique title, descriptive metadata, canonical URL and owner-private noindex directive.
- Images have alternative text, and navigation/dialog/search controls have accessible names or associated labels.
- All 20 optimized GLBs are parsed using the registered glTF extension set. Nonempty scenes, finite position bounds, actual mesh geometry and embedded textures capped at 1024px are required.
- Partial robes REF044/REF118 are excluded; all prices and rarities remain null, and public sale approval is not inferred.
- DOM tests execute search, combined filters, no-result states, filter reset, the 17-character category, three-item comparison cap, comparison table, clear selection, motion preference persistence, mobile menu, city district selection, lightbox and trailer-status dialog.
- New CSS font declarations use only approved weights and include reduced-motion support.
- Purchase flows, top-up storefronts, fabricated cash prices and unsupported account features are absent.
- Original repository tracked files are unchanged. Website work lives in a new directory/branch.

## Manual verification required

The supported browser control skill is unavailable in this environment. Per the Sites workflow, no preview server or alternate browser automation was started. As a result, there are no claimed browser screenshots, actual WebGL drawing checks, viewport visual pass, real assistive-technology result, or Lighthouse score.

Before broad release, inspect:

- Desktop 1440×900 and 1920×1080; tablet 768×1024; Android 360×800 and 390×844; narrow 320px; landscape orientation.
- Hero/logo cropping, typography loading, card text wrapping, catalog filters, mobile navigation, modal scroll/focus and touch targets.
- All 20 viewers on actual Android GPUs; load failures should preserve the original image. Test reset, auto rotation, keyboard alternatives, native fullscreen and context loss. Verify device quality, visibility pause and max-two-context policy.
- Reduced motion before first load and via page controls, including arena camera movement and pointer depth.
- Accessible color contrast under actual compositing; the specified Blue is used as an accent rather than white-on-blue body text.
- HTTP security/cache headers, custom 404 status and canonical origins on the chosen host.
- Core Web Vitals and Lighthouse with genuine functionality enabled. No 90+ score is claimed without measurement.

## Content and release limitations

The hero is official raster mascot artwork, with pointer depth; the original ring has a real optional WebGL viewer. The mascot is not a rigged animated character. The city uses an explicitly conceptual interactive illustration because a confirmed final city scene was not present. Planned game systems, collection reveals, shop price/rarity, release date, trailer, account features, waitlist and company relationship remain qualified. The first deployment is owner-private.
