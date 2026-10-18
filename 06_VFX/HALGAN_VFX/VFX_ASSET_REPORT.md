# HALGAN VFX asset report

Generated 2026-10-11. PASS means each numbered folder contains nonempty, valid 256x256 transparent PNG source texture(s) and a Unity Particle System setup specification, or the #398 integration guide. Prefabs still require creation and validation in the HALGAN Unity project.

| # | Asset | Status | Deliverable | Remaining Unity work |
|---:|---|---|---|---|
| 381 | Jab_Hit_Spark_VFX | PASS | 2 PNG textures; setup spec | One-shot; 6 particles; prefab creation and in-editor audition required. |
| 382 | Cross_Hit_Impact_VFX | PASS | 2 PNG textures; setup spec | One-shot; 5 particles; prefab creation and in-editor audition required. |
| 383 | Hook_Hit_Swipe_VFX | PASS | 2 PNG textures; setup spec | One-shot; 6 particles; prefab creation and in-editor audition required. |
| 384 | Uppercut_Hit_Burst_VFX | PASS | 2 PNG textures; setup spec | One-shot; 7 particles; prefab creation and in-editor audition required. |
| 385 | Body_Shot_Dust_VFX | PASS | 1 PNG texture; setup spec | One-shot; 6 particles; prefab creation and in-editor audition required. |
| 386 | Block_Guard_Impact_VFX | PASS | 2 PNG textures; setup spec | One-shot; 5 particles; prefab creation and in-editor audition required. |
| 387 | Punch_Miss_Air_Trail_VFX | PASS | 1 PNG texture; setup spec | One-shot; 3 particles; prefab creation and in-editor audition required. |
| 388 | Heavy_KO_Impact_VFX | PASS | 3 PNG textures; setup spec | One-shot; 16 particles; prefab creation and in-editor audition required. |
| 389 | Knockdown_Dust_VFX | PASS | 1 PNG texture; setup spec | One-shot; 10 particles; prefab creation and in-editor audition required. |
| 390 | Footstep_Dust_VFX | PASS | 1 PNG texture; setup spec | One-shot; 3 particles; prefab creation and in-editor audition required. |
| 391 | Sweat_Splash_VFX | PASS | 1 PNG texture; setup spec | One-shot; 8 particles; prefab creation and in-editor audition required. |
| 392 | Blood_Tiny_Hit_VFX | PASS | 1 PNG texture; setup spec | One-shot; 4 particles; prefab creation and in-editor audition required. |
| 393 | Energy_Gain_VFX | PASS | 2 PNG textures; setup spec | One-shot; 20 particles; prefab creation and in-editor audition required. |
| 394 | Reward_Claim_VFX | PASS | 2 PNG textures; setup spec | One-shot; 28 particles; prefab creation and in-editor audition required. |
| 395 | Level_Up_VFX | PASS | 3 PNG textures; setup spec | One-shot; 30 particles; prefab creation and in-editor audition required. |
| 396 | Skill_Upgrade_VFX | PASS | 2 PNG textures; setup spec | One-shot; 14 particles; prefab creation and in-editor audition required. |
| 397 | City_Interaction_Marker_VFX | PASS | 2 PNG textures; setup spec | Looped; 10 particles; prefab creation and in-editor audition required. |
| 398 | VFX_Integration_Guide | PASS | `unity_ready/VFX_INTEGRATION_GUIDE.md` | Apply settings and profile in project. |

**Count:** 18 PASS, 0 FAIL.

## In-editor work

- Create prefabs and Unlit particle materials for #381-#397 using each `unity_ready/SETUP.md`.
- Wire anchors, pooling, content toggle for #392, and city marker distance culling.
- Audition every effect on Android and adjust scale/opacity; no Unity project was available for in-editor setup or device profiling.

## Rejected sources

None. All textures were generated from scratch; no external art was used.
