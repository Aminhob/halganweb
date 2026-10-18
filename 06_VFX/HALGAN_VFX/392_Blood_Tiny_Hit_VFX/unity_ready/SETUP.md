# 392 Blood Tiny Hit VFX

**Status:** Unity setup spec; textures are ready. **Attachment:** body hit point.
**Duration:** 0.17 s; one-shot. **Total live/burst particles:** 4.
**Visual direction:** OFF by default. Gate behind an age-rating/content toggle; no decals or persistent stains.

## Particle System setup

Create one Particle System child per texture layer and save the configured root as `VFX_392_Blood_Tiny_Hit_VFX.prefab` in Unity. Use the listed PNG as the material base texture. These PNGs already contain color and alpha; set Start Color to white, then fade alpha over lifetime.

| Layer | Texture | Burst/active count | Start lifetime | Start size | Start speed | Texture color |
|---|---|---:|---|---|---|---|
| droplet | 392_Blood_Tiny_Hit_VFX_droplet.png | 4 | 0.10-0.17 s | 0.020-0.040 m | 0.4-0.8 m/s | #992527 |

- Main: Looping Off; Play On Awake Off; Simulation Space World; Scaling Mode Local; Max Particles 4; Prewarm Off.
- Emission: Rate over Time 0; one burst at t=0 per layer.
- Shape: narrow cone away from hit; radius <= 0.06 m unless UI-scaled.
- Color over Lifetime: alpha 0 -> 0.8 -> 0 over the first 15%, middle 30%, and final 55% of each particle lifetime. 
- Size over Lifetime: 0.6 -> 1.0 -> 0.2.
- Renderer: Billboard, an Unlit particle material with alpha blending, no shadows, no lighting, no soft particles, no distortion. Use a single quad per particle.
- Stop Action: disable and return to pool after all particles die.

## Mobile notes

- Cap simultaneous combat hit roots at 3; drop the oldest low-priority effect when full.
- Pool this effect; avoid instantiating at each hit.
- Keep textures at 256x256 RGBA and disable mipmaps unless the effect occupies world space at many distances.
- Avoid bloom dependency. Check readability at 720p on a low-end Android test device.
- If GPU overdraw spikes, remove secondary layers first and reduce particle count by half.
