# HALGAN audio asset report

Updated 2026-10-11. PASS means a downloaded, nonempty file with a verified commercial-use license is present. It does **not** mean the sound has been auditioned in game, normalized, or made seamless. FAIL means the requested sound remains unfilled.

`originals` preserves the downloaded file. `unity_ready` contains every selected game file. Non-OGG files there are direct copies for Unity import; OGG transcode recommended. No conversion, trimming, normalization or seamless-loop editing has been performed.

| # | Asset | Status | File / finding | Notes |
|---:|---|---|---|---|
| 345 | Jab_Punch_SFX | PASS | `originals/345_Jab_Punch_SFX.ogg` | Quick generic punch impact; layer a short swish for glove motion. |
| 346 | Cross_Punch_SFX | PASS | `originals/346_Cross_Punch_SFX.ogg` | Heavy generic punch impact. |
| 347 | Hook_Punch_SFX | PASS | `originals/347_Hook_Punch_SFX.ogg` | Heavy generic punch impact; hook direction needs a separate swish layer. |
| 348 | Uppercut_Punch_SFX | PASS | `originals/348_Uppercut_Punch_SFX.ogg` | Heavy generic punch impact; upward motion needs a separate swish layer. |
| 349 | Body_Shot_SFX | PASS | `originals/349_Body_Shot_SFX.ogg` | Soft/muffled impact suitable for body shot. |
| 350 | Blocked_Punch_SFX | PASS | `originals/350_Blocked_Punch_SFX.ogg` | Padded impact suitable for guard contact. |
| 351 | Punch_Miss_Whoosh_SFX | PASS | `originals/351_Punch_Miss_Whoosh_SFX.wav` | Weapon-style air swish; audition against fist animation. |
| 352 | Dodge_Slip_Movement_SFX | PASS | `originals/352_Dodge_Slip_Movement_SFX.ogg` | Cloth movement suitable as a dodge layer. |
| 353 | Footstep_Ring_Canvas_SFX | PASS | `originals/353_Footstep_Ring_Canvas_SFX.ogg` | Carpet footstep approximates a padded canvas step; audition on ring visuals. |
| 354 | Boxer_Shuffle_Footwork_SFX | PASS | `originals/354_Boxer_Shuffle_Footwork_SFX.mp3` | Four-second sneaker steps on felt carpet; suitable padded-ring footwork candidate. Audition and trim for shuffle timing. |
| 355 | Knockdown_Impact_SFX | PASS | `originals/355_Knockdown_Impact_SFX.ogg` | Heavy soft impact approximates a fall onto mat; body movement layer recommended. |
| 356 | Get_Up_Movement_SFX | PASS | `originals/356_Get_Up_Movement_SFX.ogg` | Cloth rustle for getting-up motion. |
| 357 | KO_Impact_SFX | PASS | `originals/357_KO_Impact_SFX.ogg` | Heavy punch impact; mix with low-frequency layer if needed. |
| 358 | Crowd_Ambience_Loop | PASS | `originals/358_Crowd_Ambience_Loop.mp3` | Arena-type crowd ambience; inspect loop seam before enabling Loop. |
| 359 | Crowd_Cheer_SFX | PASS | `originals/359_Crowd_Cheer_SFX.mp3` | Short strong cheering reaction. |
| 360 | Crowd_Boo_SFX | PASS | `originals/360_Crowd_Boo_SFX.mp3` | Three-second crowd boo/disapproval reaction. |
| 361 | Round_Bell_SFX | PASS | `originals/361_Round_Bell_SFX.ogg` | Metal bell impact; audition for authentic boxing round bell tone. |
| 362 | Countdown_Beep_SFX | PASS | `originals/362_Countdown_Beep_SFX.ogg` | Short digital tone; trigger three times in game for countdown. |
| 363 | Timer_Warning_SFX | PASS | `originals/363_Timer_Warning_SFX.ogg` | Three-tone warning candidate. |
| 364 | UI_Button_Click_SFX | PASS | `originals/364_UI_Button_Click_SFX.ogg` | Clean UI click. |
| 365 | UI_Confirm_SFX | PASS | `originals/365_UI_Confirm_SFX.ogg` | Confirmation UI sound. |
| 366 | UI_Cancel_SFX | PASS | `originals/366_UI_Cancel_SFX.ogg` | Back/cancel UI sound. |
| 367 | Reward_Claim_SFX | PASS | `originals/367_Reward_Claim_SFX.ogg` | Coin handling reward cue. |
| 368 | Energy_Purchase_SFX | PASS | `originals/368_Energy_Purchase_SFX.ogg` | Purchase confirmation cue; add energy effect in game if needed. |
| 369 | Level_Up_SFX | PASS | `originals/369_Level_Up_SFX.ogg` | Power-up sound for level gain. |
| 370 | Skill_Upgrade_SFX | PASS | `originals/370_Skill_Upgrade_SFX.ogg` | Alternate power-up sound for skill gain. |
| 371 | Match_Start_Music_Cue | PASS | `originals/371_Match_Start_Music_Cue.ogg` | Short musical hit; audition for match-start energy. |
| 372 | Victory_Music_Cue | PASS | `originals/372_Victory_Music_Cue.ogg` | Retro-styled victory jingle; sound is original, not a game rip. |
| 373 | Defeat_Music_Cue | PASS | `originals/373_Defeat_Music_Cue.wav` | Short CC0 game-over music cue. |
| 374 | Draw_Result_Cue | PASS | `originals/374_Draw_Result_Cue.mp3` | Eight-second soft neutral musical stinger; AI-generated according to source page. Audition for draw-result fit. |
| 375 | Menu_Background_Music_Loop | PASS | `originals/375_Menu_Background_Music_Loop.mp3` | Upbeat loop, suitable as a menu music candidate; not boxing-specific. |
| 376 | Training_Background_Music_Loop | PASS | `originals/376_Training_Background_Music_Loop.mp3` | Action music loop candidate for training. |
| 377 | City_Ambience_Loop | PASS | `originals/377_City_Ambience_Loop.mp3` | Rainy street traffic ambience; do not assume sample-perfect loop seam. |
| 378 | Garage_Ambience_Loop | PASS | `originals/378_Garage_Ambience_Loop.mp3` | Parking garage with carts, people and reverb. Long recording (5:06); audition for a quiet segment and trim/loop before runtime use. |
| 379 | Voice_Chat_Join_Leave_SFX | PASS | `originals/379_Voice_Chat_Join_Leave_SFX.ogg` + leave cue | Join notification; separate leave sound also included. |
| 380 | Final_Audio_Mix_Reference | PASS | MIX_REFERENCE.md | Notes file created; no copyrighted reference downloaded. |

## Remaining work

- Audition all candidate sounds in game, especially the generic punch variants, sneaker footwork, bell, result cues and music.
- Trim the 5:06 parking-garage recording to a suitable quiet passage, and check loop seams for crowd, city and garage ambience.
- Transcode MP3/WAV files in `unity_ready` to OGG when an encoder is available.
