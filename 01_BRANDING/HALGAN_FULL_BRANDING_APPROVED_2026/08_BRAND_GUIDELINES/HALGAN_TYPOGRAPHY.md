# Teko - official HALGAN GAME typography

Approved by the user on 2026-10-14.

- Headlines / posters / victory messages: Teko SemiBold, 600.
- Buttons / navigation / player names: Teko SemiBold, 600.
- Scoreboards / round labels / stats: Teko Medium, 500.
- Body copy / descriptions: Teko Regular, 400.
- Decorative large secondary text only: Teko Light, 300.

Use clear size hierarchy and preserve natural letter shapes. Keep tracking close to normal for body copy. Test body text at final phone size; start at 20-24 px with 1.25-1.4 line height. Use 24-32 px for buttons and 48 px or larger for major display headlines. These are starting values, not rigid minimums.

Install only the four approved static TTF files (Regular, Medium, Light, SemiBold) for desktop design. The original variable TTF is retained as source material; only weights 300, 400, 500 and 600 are permitted. Static TTF and WOFF files are Latin-subset builds distributed by Fontsource, appropriate for English and Somali. Use the full variable font for its wider original script coverage. Keep OFL.txt with distributed font files.

Website: load 09_EDITABLE_SOURCES/brand_tokens.css; its @font-face URLs are relative to that CSS file and load included local WOFF files. Unity / TextMeshPro: import the static TTF files and create TMP Font Assets; assign weights per role and include required characters. No TMP assets are claimed to have been generated without a Unity project.

The approved HALGAN logo remains its approved artwork. Teko defines campaign, interface, and editorial typography; it is not an identification of the font used in the original logo.

Sources:
- Full variable font and license: https://github.com/google/fonts/tree/main/ofl/teko
- Latin static and webfont distributions: https://fontsource.org/fonts/teko
- Specimen: https://fonts.google.com/specimen/Teko
License: SIL Open Font License 1.1; see OFL.txt for the full terms.


Current policy (2026-10-17): HALGAN Red remains primary. Electric Blue is secondary; use the existing brand_tokens.json / brand_tokens.css. Only Teko Regular, Medium, Light and SemiBold are permitted. Teko-Bold and synthetic bold are prohibited. Historical exports and the old PDF guide have not been reissued; the Electric Blue addendum in 01_BRANDING/ELECTRIC_BLUE_2026-10-17 takes precedence for color and font policy.
