# 394 Reward Claim VFX

**Status:** Unity setup spec; textures are ready. **Attachment:** reward icon, UI overlay.
**Duration:** 0.90 s; one-shot. **Total live/burst particles:** 28.
**Visual direction:** Burst once after claim confirmation; no continuous glitter.

## Particle System setup

Create one Particle System child per texture layer and save the configured root as `VFX_394_Reward_Claim_VFX.prefab` in Unity. Use the listed PNG as the material base texture. These PNGs already contain color and alpha; set Start Color to white, then fade alpha over lifetime.

| Layer | Texture | Burst/active count | Start lifetime | Start size | Start speed | Texture color |
|---|---|---:|---|---|---|---|
| spark | 394_Reward_Claim_VFX_spark.png | 26 | 0.40-0.85 s | 0.03-0.07 m or UI-scaled equivalent | 0.3-0.9 m/s | #FFD369 |
| ring | 394_Reward_Claim_VFX_ring.png | 2 | 0.45-0.75 s | 0.20-0.35 m or UI-scaled equivalent | 0 m/s | #FFE59E |

- Main: Looping Off; Play On Awake Off; Simulation Space Local; Scaling Mode Local; Max Particles 28; Prewarm Off.
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
