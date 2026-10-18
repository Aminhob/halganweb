# 384 Uppercut Hit Burst VFX

**Status:** Unity setup spec; textures are ready. **Attachment:** glove contact point, up axis aligned to world up.
**Duration:** 0.20 s; one-shot. **Total live/burst particles:** 7.
**Visual direction:** Use a narrow upward cone, not a screen-wide flash.

## Particle System setup

Create one Particle System child per texture layer and save the configured root as `VFX_384_Uppercut_Hit_Burst_VFX.prefab` in Unity. Use the listed PNG as the material base texture. These PNGs already contain color and alpha; set Start Color to white, then fade alpha over lifetime.

| Layer | Texture | Burst/active count | Start lifetime | Start size | Start speed | Texture color |
|---|---|---:|---|---|---|---|
| burst | 384_Uppercut_Hit_Burst_VFX_burst.png | 6 | 0.12-0.19 s | 0.09-0.20 m | 0.5-1.0 m/s | #FFEBCB |
| flash | 384_Uppercut_Hit_Burst_VFX_flash.png | 1 | 0.08 s | 0.12 m | 0 m/s | #FFF9E8 |

- Main: Looping Off; Play On Awake Off; Simulation Space World; Scaling Mode Local; Max Particles 7; Prewarm Off.
- Emission: Rate over Time 0; one burst at t=0 per layer.
- Shape: narrow upward cone; radius <= 0.06 m unless UI-scaled.
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
