# HALGAN GAME - official social media branding

Prepared 2026-10-14. Identity: approved HALGAN logo and boxer icon; official Teko typography; black, punch red, silver and white. The supplied arena imagery comes from the HALGAN workspace. Asset hashes appear in MANIFEST.csv.

## Use first

1. Upload the platform avatar from 01_PROFILE_PICTURES.
2. Upload the YouTube, Facebook or X cover from 02_COVER_BANNERS. JPEG alternatives and crop previews are supplied.
3. Use the three pinned square posts as separate identity, Somali and community posts. They do not rely on a specific profile-grid crop.
4. Use portrait posts, Stories/Reel covers and thumbnails for ongoing content. Files marked TEMPLATE_REPLACE_BRACKETS in ASSET_CATALOG.csv require actual names, dates, results or links before publishing.

BRAND_READY means generic identity copy is complete; it does not assert that an account is verified, an event is scheduled, or the game is available for download. No social account has been accessed or updated by this package.

## Edit

The SVGs in 06_EDITABLE_SOURCES contain editable text/shapes and embedded approved raster artwork plus the full variable Teko font. Install the supplied static TTF fonts for design editors. SVG files are layout sources, not vector logo masters. Source PNGs and licensed fonts are included so the pack works by itself.

Change social_content.json to set the confirmed handle, display name, tagline and bios. The handle is intentionally blank because no official username was supplied. Other placeholders are visible in each event/news template; edit those SVG text elements directly. Long replacement copy may need smaller type or extra lines. Confirm fit at final display size.

To regenerate the default pack: run build_social_media.py build, then render, then package. Regenerating resets edited SVG copy to the scripted default templates; save custom variations with new names. Python requires Pillow. Node requires Playwright and Chromium or Microsoft Edge. Set HALGAN_NODE and HALGAN_PLAYWRIGHT_PATH if the runtime paths differ.

## File map

- 01_PROFILE_PICTURES: avatars in platform upload sizes.
- 02_COVER_BANNERS: YouTube, Facebook and X covers.
- 03_FEED_POSTS: identity, Somali, community, event/result/update templates and video thumbnails.
- 04_STORIES_REELS: portrait story and reel covers.
- 05_HIGHLIGHT_COVERS: six circular-safe highlight categories.
- 06_EDITABLE_SOURCES: SVGs, content configuration and generator.
- 07_SOURCE_ASSETS: original logo, icon and supplied background imagery.
- 08_FONTS: Teko files and SIL OFL 1.1 license.
- 09_PREVIEWS: actual exported design board, complete contact sheets and crop checks.

These are static images and editable layouts. Video animation and platform account publishing are not included.
