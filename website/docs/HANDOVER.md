# HALGAN website handover

## Implementation

The site uses static generation for 52 independent routes with page-specific metadata. A shared template establishes navigation, footer, dialogs and accessibility. The content architecture separates editorial records (`src/content.mjs`), sanitized development models (`src/catalog.json`), templates, UI interactions and a lazy Three.js viewer. It can later accept an approved backend feed without exposing raw game records.

The lightweight rendering stack fits a presentation/catalog experience with no accounts or server state. Server frameworks, payment SDKs and animation libraries are unnecessary for the currently verified scope. Assets are self-hosted. The optimized site is approximately 15 MB in total, including all twenty models; only requested models load. The initial application script is about 18 KB before transfer compression; the 3D chunk is approximately 580 KB and loads on demand. These are file sizes, not measured network performance or Lighthouse results.

## Information architecture

See `routes.json`. Every major requested section has its own route. Character detail pages share a model with catalog detail pages. Draft fighter collections preserve the supplied 4/7/30 plan while withholding unapproved identities. The city is an accessible interactive concept diagram; it is explicitly not an in-game map. The development record uses actual repository dates and qualifies asset-import approval separately from gameplay completion. The 100-day developer series remains planned.

## Integrations still required

1. **Public art approval:** verify marketing approval and likeness rights per character/model. `publicApproved: false` means no public-market approval is inferred from model cleanup. Keep the first hosted site owner-private. Do not equate Unity import validation with marketing approval.
2. **Official catalog:** approved item IDs (REF labels are audit references), Coins prices, rarity tiers, collections, compatibility, availability, descriptions and acquisition rules. Only render published items from a server-validated public feed. Enable price/rarity filtering once actual values exist.
3. **Fighter content:** approved names, biographies, power/speed/stamina, styles, signature abilities, unlock requirements and cosmetics. Verify all real-person likeness rights before including their identities.
4. **Gameplay media:** approved screenshots, video trailers and development footage. Replace the informative trailer-status dialog with a real captioned video only when an approved file exists.
5. **Game status:** authoritative feature status, device-performance evidence, release date and Play Store URL. No fake countdown is present.
6. **Official identity statements:** company structure, HALGAN ecosystem and the exact eTacab relationship; verified social handles. The supplied brief alone does not establish legal ownership.
7. **Account-backed wishlist:** authenticated user identity, durable storage, access checks and deletion/export policies. No fake account or wishlist interface is shown.
8. **Waitlist/notifications:** verified email provider, consent text, retention policy, double opt-in, rate limits and a real endpoint. Do not collect email addresses until it exists.
9. **Commerce:** account binding, inventory/fulfillment, validation and payment approvals. Current site has no checkout, Coins top-up UI or purchase endpoint. If authorized paid offers are later added, the server must return them only while an administrator has explicitly enabled the offer; when disabled, omit every paid-offer reference and reject stale requests. Do not expose secrets or payment credentials in browser code.
10. **Production QA:** real desktop/mobile viewport screenshots, touch/keyboard/screen-reader checks, GLB inspection on Android GPUs, Core Web Vitals/Lighthouse runs, HTTP cache/security-header verification and publication approval for art. Change noindex only after the public-content review.

## 3D behavior

The real GLBs are lazy loaded with original static-render fallbacks. The viewer normalizes presentation scale without editing source models, frames bounds, uses local material textures, caps pixel ratio, reduces quality on smaller/lower-memory devices and pauses off-screen/hidden rendering. At most two contexts stay active. Rotation/zoom/reset/fullscreen and keyboard alternatives are exposed. Native fullscreen failure is announced while the embedded viewer remains functional. A paused-motion setting disables auto rotation and scroll-camera effects. The ring includes a small scroll-linked camera movement until manually controlled. Static character models are not claimed to be rigged or animated.

## Deployment

Build: `npm run build`. Output: `dist/`. Serve directory indexes and `404.html`. `_headers` contains suggested static-host security/cache settings; verify the selected host honors them. The owner-private Sites publication uses `.openai/hosting.json`; preserve its exact project identity. Generic hosts do not need that file. Deployed files contain only sanitized pages, bundled code, approved-brand web derivatives and development-preview assets, not internal reports.

## Known limits

The supported browser automation capability is unavailable, so there are no verified viewport screenshots, WebGL runtime results or Lighthouse scores. DOM tests do not validate WebGL drawing. Static fallback images are original development renders with their original neutral backgrounds. Collection/rules/economy placeholders are explicit. No backend-dependent functions are simulated.
