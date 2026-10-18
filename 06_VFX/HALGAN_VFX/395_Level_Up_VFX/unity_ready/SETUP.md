# 395 Level Up VFX

**Status:** Unity setup spec; textures are ready. **Attachment:** level-up UI panel.
**Duration:** 1.35 s; one-shot. **Total live/burst particles:** 30.
**Visual direction:** One pulse plus upward rays; keep text legible.

## Particle System setup

Create one Particle System child per texture layer and save the configured root as `VFX_395_Level_Up_VFX.prefab` in Unity. Use the listed PNG as the material base texture. These PNGs already contain color and alpha; set Start Color to white, then fade alpha over lifetime.

| Layer | Texture | Burst/active count | Start lifetime | Start size | Start speed | Texture color |
|---|---|---:|---|---|---|---|
| ray | 395_Level_Up_VFX_ray.png | 8 | 0.75-1.20 s | 0.12-0.22 m or UI-scaled equivalent | 0.2-0.6 m/s | #70B5F5 |
| spark | 395_Level_Up_VFX_spark.png | 20 | 0.50-1.15 s | 0.03-0.07 m or UI-scaled equivalent | 0.4-0.9 m/s | #F9D17D |
| ring | 395_Level_Up_VFX_ring.png | 2 | 0.55-0.90 s | 0.20-0.42 m or UI-scaled equivalent | 0 m/s | #97CBF5 |

- Main: Looping Off; Play On Awake Off; Simulation Space Local; Scaling Mode Local; Max Particles 30; Prewarm Off.
- Emission: Rate over Time 0; one burst at t=0 per layer.
- Shape: small sphere or circle at anchor; radius <= 0.06 m unless UI-scaled.
- Color over Lifetime: alpha 0 -> 0.8 -> 0 over the first 15%, middle 30%, and final 55% of each particle lifetime. 
- Size over Lifetime: 0.6 -> 1.0 -> 0.2.
- Renderer: Billboard, an Unlit particle material with additive blending, no shadows, no lighting, no soft particles, no distortion. Use a single quad per particle.
- Stop Action: disable and return to pool after all particles die.

## Mobile notes

- Cap simultaneous combat hit roots at 3; drop the oldest low-priority effect when full.
- Pool this effect; avoid instantiating at each hit.
- Keep textures at 256x256 RGBA and disable mipmaps unless the effect occupies world space at many distances.
- Avoid bloom dependency. Check readability at 720p on a low-end Android test device.
- If GPU overdraw spikes, remove secondary layers first and reduce particle count by half.
