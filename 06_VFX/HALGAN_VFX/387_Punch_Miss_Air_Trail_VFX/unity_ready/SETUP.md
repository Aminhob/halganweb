# 387 Punch Miss Air Trail VFX

**Status:** Unity setup spec; textures are ready. **Attachment:** glove, local space.
**Duration:** 0.18 s; one-shot. **Total live/burst particles:** 3.
**Visual direction:** Cap opacity at roughly 25%; disable on low graphics tier if needed.

## Particle System setup

Create one Particle System child per texture layer and save the configured root as `VFX_387_Punch_Miss_Air_Trail_VFX.prefab` in Unity. Use the listed PNG as the material base texture. These PNGs already contain color and alpha; set Start Color to white, then fade alpha over lifetime.

| Layer | Texture | Burst/active count | Start lifetime | Start size | Start speed | Texture color |
|---|---|---:|---|---|---|---|
| streak | 387_Punch_Miss_Air_Trail_VFX_streak.png | 3 | 0.09-0.17 s | 0.18-0.32 m | 0.1-0.25 m/s | #DAE7F0 |

- Main: Looping Off; Play On Awake Off; Simulation Space World; Scaling Mode Local; Max Particles 3; Prewarm Off.
- Emission: Rate over Time 0; one burst at t=0 per layer.
- Shape: small sphere or circle at anchor; radius <= 0.06 m unless UI-scaled.
- Color over Lifetime: alpha 0 -> 0.8 -> 0 over the first 15%, middle 30%, and final 55% of each particle lifetime. Limit peak alpha to 0.25.
- Size over Lifetime: 0.6 -> 1.0 -> 0.2.
- Renderer: Billboard, an Unlit particle material with alpha blending, no shadows, no lighting, no soft particles, no distortion. Use a single quad per particle.
- Stop Action: disable and return to pool after all particles die.

## Mobile notes

- Cap simultaneous combat hit roots at 3; drop the oldest low-priority effect when full.
- Pool this effect; avoid instantiating at each hit.
- Keep textures at 256x256 RGBA and disable mipmaps unless the effect occupies world space at many distances.
- Avoid bloom dependency. Check readability at 720p on a low-end Android test device.
- If GPU overdraw spikes, remove secondary layers first and reduce particle count by half.
