# HALGAN approved branding kit

This kit uses the three images approved in the current chat: metallic cutout logo, supplied monochrome logo, and supplied boxing app icon. They replace the earlier reconstruction candidate and previous kit identities. No logo reconstruction is used here.

The exact originals are in 01_OFFICIAL_LOGOS. Full-color exports preserve the supplied silver material, red brush stroke and boxer. Black, white and silver flat versions derive from the supplied monochrome artwork, with its white image background removed. The app and profile icons use the supplied boxer illustration.

Folders 02 and 03 contain Android and Unity exports; 04 social templates; 05 livestream cards and transparent overlays; 06 web and marketing; 07 flat print assets and event art; 08 the PDF guide; 09 self-contained editable SVG layouts and color tokens; 10 previews. See MANIFEST.csv for every file.

Edit text and shapes in the SVG templates with an SVG-capable editor. The approved logos and icon remain embedded raster images. These are editable layout files, not vector logo masters. Teko is the official HALGAN GAME font, approved on 2026-10-14. Installable fonts, local webfonts and the SIL OFL license are in 11_OFFICIAL_FONTS. See 08_BRAND_GUIDELINES/HALGAN_TYPOGRAPHY.md for roles and installation. The logo remains approved artwork. Keep the artwork proportions intact.

Replace all bracketed placeholders before publishing. Dates, contenders, results, scores, download destinations and sponsor data are intentionally blank. The YouTube banner keeps primary content inside a central 1350 x 390 region; preview crops in the destination UI.

Raster source sizes: metallic 2164 x 727, monochrome 1672 x 941, icon 1254 x 1254. Larger exports add layout convenience, not new optical detail. Supplied edge texture and brush roughness are retained. Tiny favicons retain the approved icon but cannot retain subtitle legibility.

The store icon has an opaque square background. Adaptive foreground is an inset version of the entire supplied icon, not a separately extracted boxer. Android mask previews are provided; test in your launcher build.

Print artwork is RGB raster at the listed pixel dimensions. 300 DPI metadata in garment placement sheets does not increase source detail. Final size, color conversion, bleed and garment print process depend on your supplier. The PDF guide is a digital brand reference.

Official typography: Teko SemiBold 600 for headlines; SemiBold 600 for buttons/navigation; Medium 500 for stats; Regular 400 for body copy. The SVG templates embed the full variable Teko font for portable previews. Edit text with Teko installed. Full variable TTF and Latin-subset static TTF/WOFF fonts are included.

Regeneration: run 09_EDITABLE_SOURCES/build_approved_branding.py with Python (Pillow, NumPy, ReportLab, pypdf), Node.js and Playwright. The renderer uses Chromium or installed Microsoft Edge. Set HALGAN_NODE and HALGAN_PLAYWRIGHT_PATH when these runtimes are not on the default paths.

## Official social media branding

Use 04_SOCIAL_MEDIA/OFFICIAL_SOCIAL_MEDIA_KIT for the complete official Teko social identity: platform avatars, YouTube/Facebook/X covers, pinned posts, portrait posts, Stories/Reel covers, thumbnails and Highlight covers. See its 00_START_HERE/README.md, ASSET_CATALOG.csv and SOCIAL_BRAND_GUIDE.md. The kit includes 35 exported designs, embedded-font editable SVGs, source artwork, local font files and crop previews. Generic identity posts are complete; bracketed event/news placeholders need confirmed details before publication. Official account handles have not been supplied, so exports use HALGAN GAME without invented usernames.


Current policy (2026-10-17): HALGAN Red remains primary. Electric Blue is secondary; use the existing brand_tokens.json / brand_tokens.css. Only Teko Regular, Medium, Light and SemiBold are permitted. Teko-Bold and synthetic bold are prohibited. Historical exports and the old PDF guide have not been reissued; the Electric Blue addendum in 01_BRANDING/ELECTRIC_BLUE_2026-10-17 takes precedence for color and font policy.
