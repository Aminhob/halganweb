# HALGAN VFX integration guide

## Naming and project layout

- Prefab: `VFX_<number>_<Name>.prefab`; material: `M_VFX_<blend>_<Name>`; texture: supplied `<number>_<Name>_<layer>.png`.
- Put combat prefabs under `Assets/HALGAN/VFX/Combat`, UI prefabs under `Assets/HALGAN/VFX/UI`, and markers under `Assets/HALGAN/VFX/City`.
- Each numbered `unity_ready/SETUP.md` defines the precise layers and particle values for authoring its prefab.

## Particle System baseline

- Use Unity Particle System modules Main, Emission, Shape, Color over Lifetime, Size over Lifetime and Renderer only where needed. Set Rate over Time to zero for one-shots and use a single emission burst.
- Use Billboard quads and an Unlit particle material. Use additive for sparks/rings, alpha blend for dust, droplets, air trails and the city marker.
- Disable shadows, lighting, soft particles, collision, trails, sub-emitters, custom vertex streams and bloom dependency by default.
- A one-shot root returns to the pool after the longest particle lifetime. The city marker is the only looping effect.

## Texture and render limits

- Supplied textures are 256x256 transparent PNGs. Keep most textures at 256; 512x512 is an upper limit only when a specific effect visibly requires it.
- Prefer bilinear filtering and Clamp wrap for streaks/arcs; use Clamp for the other textures unless a tiled effect is built.
- Disable Read/Write after import. Disable mipmaps for fixed-size UI; enable only for world particles that shrink significantly with distance.
- Consider platform compression after visual testing; preserve alpha edges.
- Render world effects after boxer meshes and before screen UI. Attach glove/body effects to hit anchors; ring dust to canvas contact; city marker on the ground plane.
- UI reward/energy/level-up systems should render above panels but below text/icons. Use the canvas sorting layer/order or a dedicated UI particle renderer compatible with the project pipeline.
- Keep blended layers shallow: usually one or two quads per pixel; reduce ring/flash overlap on Android.

## Attachment, lifetime and priority

| Assets | Anchor | Playback | Priority |
|---|---|---|---|
| 381-384, 386-388 | glove/contact | one-shot | high |
| 385, 391-392 | body/hit | one-shot | medium |
| 389-390 | ring canvas/shoe | one-shot | low |
| 393-396 | UI or pickup/icon | one-shot | medium |
| 397 | city marker | looped | low |

- #392 blood is OFF by default and enabled only by an explicit content setting. No blood decals or persistent stains.
- On low graphics tier, suppress #390 and the secondary KO/UI layers before lowering core hit readability.

## Pooling and budget

- Prewarm a small pool per combat effect, then recycle on particle completion. Keep no more than 3 combat hit VFX roots active at once.
- Target light hits at 4-8 particles, heavy hits at 10-18, reward/level-up at 20-40, and city marker at 6-12 active particles. The supplied specs stay within these ranges.
- Treat 1-3 ms GPU VFX time at 30 fps as a starting validation target, not a guarantee; profile on representative low and mid Android devices.
- Avoid per-frame allocations and per-hit material instantiation. Share materials by blend mode when the same texture/color setup permits.
- Distance-cull city markers and hide effects behind UI panels or off-camera.

## Unity implementation checklist

1. Import the supplied PNGs as Default textures with alpha preserved.
2. Create Unlit alpha/additive particle materials for the project render pipeline.
3. Configure each Particle System from its numbered `SETUP.md` and save the prefab.
4. Wire hit, reward and city events; pool one-shots and stop out-of-range markers.
5. Test color, scale, sorting and alpha on Android at 720p/30 fps and with reduced graphics settings.

Unity references: https://docs.unity3d.com/Manual/ParticleSystemModules.html and https://docs.unity3d.com/ScriptReference/ParticleSystem.TextureSheetAnimationModule.html.
