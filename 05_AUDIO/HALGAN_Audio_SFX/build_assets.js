const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const root = __dirname;
const packs = path.join(root, '_source_packs');
const kenney = slug => ({page:`https://kenney.nl/assets/${slug}`, license:'CC0 1.0', author:'Kenney', attribution:'No'});
const oga = (page, author, license='CC0 1.0', attribution='No') => ({page:`https://opengameart.org/content/${page}`, license, author, attribution});
const pixabay = (page, author) => ({page:`https://pixabay.com/sound-effects/${page}/`, license:'Pixabay Content License', author, attribution:'No'});
const data = [
  [345,'Jab_Punch_SFX','impact-sounds/Audio/impactPunch_medium_000.ogg',kenney('impact-sounds'),'Quick generic punch impact; layer a short swish for glove motion.'],
  [346,'Cross_Punch_SFX','impact-sounds/Audio/impactPunch_heavy_000.ogg',kenney('impact-sounds'),'Heavy generic punch impact.'],
  [347,'Hook_Punch_SFX','impact-sounds/Audio/impactPunch_heavy_001.ogg',kenney('impact-sounds'),'Heavy generic punch impact; hook direction needs a separate swish layer.'],
  [348,'Uppercut_Punch_SFX','impact-sounds/Audio/impactPunch_heavy_002.ogg',kenney('impact-sounds'),'Heavy generic punch impact; upward motion needs a separate swish layer.'],
  [349,'Body_Shot_SFX','impact-sounds/Audio/impactSoft_medium_000.ogg',kenney('impact-sounds'),'Soft/muffled impact suitable for body shot.'],
  [350,'Blocked_Punch_SFX','impact-sounds/Audio/impactSoft_heavy_000.ogg',kenney('impact-sounds'),'Padded impact suitable for guard contact.'],
  [351,'Punch_Miss_Whoosh_SFX','swishes/swishes/swish-1.wav',oga('swishes-sound-pack','artisticdude'),'Weapon-style air swish; audition against fist animation.'],
  [352,'Dodge_Slip_Movement_SFX','rpg-audio/Audio/cloth1.ogg',kenney('rpg-audio'),'Cloth movement suitable as a dodge layer.'],
  [353,'Footstep_Ring_Canvas_SFX','impact-sounds/Audio/footstep_carpet_000.ogg',kenney('impact-sounds'),'Carpet footstep approximates a padded canvas step; audition on ring visuals.'],
  [354,'Boxer_Shuffle_Footwork_SFX','sneaker-felt.mp3',pixabay('people-schritte-sneaker-auf-filzteppich-113039','mywald'),'Four-second sneaker steps on felt carpet; suitable padded-ring footwork candidate. Audition and trim for shuffle timing.'],
  [355,'Knockdown_Impact_SFX','impact-sounds/Audio/impactSoft_heavy_001.ogg',kenney('impact-sounds'),'Heavy soft impact approximates a fall onto mat; body movement layer recommended.'],
  [356,'Get_Up_Movement_SFX','rpg-audio/Audio/cloth2.ogg',kenney('rpg-audio'),'Cloth rustle for getting-up motion.'],
  [357,'KO_Impact_SFX','impact-sounds/Audio/impactPunch_heavy_003.ogg',kenney('impact-sounds'),'Heavy punch impact; mix with low-frequency layer if needed.'],
  [358,'Crowd_Ambience_Loop','crowd-cheers/Gregor Quendel - Free Crowd Cheering Sounds - MP3/Gregor Quendel - Crowd Cheering Sounds - 10 - Ambience.mp3',oga('free-crowd-cheering-sounds','Gregor Quendel','CC BY 4.0','Yes'),'Arena-type crowd ambience; inspect loop seam before enabling Loop.'],
  [359,'Crowd_Cheer_SFX','crowd-cheers/Gregor Quendel - Free Crowd Cheering Sounds - MP3/Gregor Quendel - Crowd Cheering Sounds - 04 - Strong cheering - II - Short.mp3',oga('free-crowd-cheering-sounds','Gregor Quendel','CC BY 4.0','Yes'),'Short strong cheering reaction.'],
  [360,'Crowd_Boo_SFX','crowd-boo.mp3',pixabay('people-crowd-boo-disapproval-demo-309882','Olivia_Parker'),'Three-second crowd boo/disapproval reaction.'],
  [361,'Round_Bell_SFX','impact-sounds/Audio/impactBell_heavy_000.ogg',kenney('impact-sounds'),'Metal bell impact; audition for authentic boxing round bell tone.'],
  [362,'Countdown_Beep_SFX','digital-audio/Audio/tone1.ogg',kenney('digital-audio'),'Short digital tone; trigger three times in game for countdown.'],
  [363,'Timer_Warning_SFX','digital-audio/Audio/lowThreeTone.ogg',kenney('digital-audio'),'Three-tone warning candidate.'],
  [364,'UI_Button_Click_SFX','interface-sounds/Audio/click_001.ogg',kenney('interface-sounds'),'Clean UI click.'],
  [365,'UI_Confirm_SFX','interface-sounds/Audio/confirmation_001.ogg',kenney('interface-sounds'),'Confirmation UI sound.'],
  [366,'UI_Cancel_SFX','interface-sounds/Audio/back_001.ogg',kenney('interface-sounds'),'Back/cancel UI sound.'],
  [367,'Reward_Claim_SFX','rpg-audio/Audio/handleCoins.ogg',kenney('rpg-audio'),'Coin handling reward cue.'],
  [368,'Energy_Purchase_SFX','interface-sounds/Audio/confirmation_002.ogg',kenney('interface-sounds'),'Purchase confirmation cue; add energy effect in game if needed.'],
  [369,'Level_Up_SFX','digital-audio/Audio/powerUp1.ogg',kenney('digital-audio'),'Power-up sound for level gain.'],
  [370,'Skill_Upgrade_SFX','digital-audio/Audio/powerUp2.ogg',kenney('digital-audio'),'Alternate power-up sound for skill gain.'],
  [371,'Match_Start_Music_Cue','music-jingles/Audio/Hit jingles/jingles_HIT00.ogg',kenney('music-jingles'),'Short musical hit; audition for match-start energy.'],
  [372,'Victory_Music_Cue','victory-jingle.ogg',oga('sega-mega-drivegenesis-victory-jingle','Spring Spring / Julie Damsgaard'),'Retro-styled victory jingle; sound is original, not a game rip.'],
  [373,'Defeat_Music_Cue','game_over.wav',oga('game-over-8','Umplix'),'Short CC0 game-over music cue.'],
  [374,'Draw_Result_Cue','neutral-cue.mp3',pixabay('musical-podcast-stinger-soft-neutral-branding-cue-469090','OpenMindAudio'),'Eight-second soft neutral musical stinger; AI-generated according to source page. Audition for draw-result fit.'],
  [375,'Menu_Background_Music_Loop','city-loop.mp3',oga('city-loop-0','wipics'),'Upbeat loop, suitable as a menu music candidate; not boxing-specific.'],
  [376,'Training_Background_Music_Loop','music-action/Action_B.mp3',oga('music-loops-0','drakzlin'),'Action music loop candidate for training.'],
  [377,'City_Ambience_Loop','city-traffic.mp3',oga('free-general-ambience-sounds','Gregor Quendel','CC BY-SA 4.0','Yes'),'Rainy street traffic ambience; do not assume sample-perfect loop seam.'],
  [378,'Garage_Ambience_Loop','parking-garage.mp3',pixabay('city-amb-s-parking-garage-grocery1-51717','conleec (Freesound), via Pixabay'),'Parking garage with carts, people and reverb. Long recording (5:06); audition for a quiet segment and trim/loop before runtime use.'],
  [379,'Voice_Chat_Join_Leave_SFX','interface-sounds/Audio/confirmation_003.ogg',kenney('interface-sounds'),'Join notification; separate leave sound also included.', 'interface-sounds/Audio/back_002.ogg'],
  [380,'Final_Audio_Mix_Reference',null,null,'Mix notes only, as requested.']
];

const fallback = ['https://freesound.org/','https://opengameart.org/','https://pixabay.com/sound-effects/'];
let licenses = ['# HALGAN audio licenses','','All paths below are relative to `HALGAN_Audio_SFX`. CC0 does not require attribution. CC BY and CC BY-SA credits must be carried into the released game. Pixabay Content License permits commercial game use without required attribution, subject to its restrictions, including no standalone redistribution. Source pack ZIP files in `_source_packs` are retained for audit.','','| Asset | File | Source page | License | Author/source | Attribution | SHA-256 |','|---|---|---|---|---|---|---|'];
let report = ['# HALGAN audio asset report','','Updated 2026-10-11. PASS means a downloaded, nonempty file with a verified commercial-use license is present. It does **not** mean the sound has been auditioned in game, normalized, or made seamless. FAIL means the requested sound remains unfilled.','','`originals` preserves the downloaded file. `unity_ready` contains every selected game file. Non-OGG files there are direct copies for Unity import; OGG transcode recommended. No conversion, trimming, normalization or seamless-loop editing has been performed.','','| # | Asset | Status | File / finding | Notes |','|---:|---|---|---|---|'];
for (const [n,name,src,lic,note,second] of data) {
  const folder = path.join(root,`${n}_${name}`);
  const originals = path.join(folder,'originals');
  const ready = path.join(folder,'unity_ready');
  fs.mkdirSync(originals,{recursive:true}); fs.mkdirSync(ready,{recursive:true});
  if (n===380) {
    fs.writeFileSync(path.join(folder,'MIX_REFERENCE.md'), '# Final audio mix reference\n\nSuggested starting fader levels relative to full scale (adjust by listening on a phone speaker):\n\n| Bus | Starting level |\n|---|---:|\n| Punch impacts | -6 dB |\n| UI | -12 dB |\n| Crowd ambience | -24 dB |\n| Music | -18 dB |\n| Voice chat | -9 dB |\n\nDuck music 3-6 dB during heavy impacts and voice chat. Keep voice chat intelligible above ambience, and check the final master for clipping and device loudness. These are starting points, not measured loudness targets.\n');
    report.push(`| ${n} | ${name} | PASS | MIX_REFERENCE.md | Notes file created; no copyrighted reference downloaded. |`); continue;
  }
  if (!src) { report.push(`| ${n} | ${name} | FAIL | No file | ${note} Search alternatives: ${fallback.join(', ')} |`); continue; }
  for (const [index,rel] of [src,second].filter(Boolean).entries()) {
    const from=path.join(packs,...rel.split('/'));
    if(!fs.existsSync(from) || fs.statSync(from).size===0) throw new Error(`Missing source: ${from}`);
    const ext=path.extname(from).toLowerCase();
    const label=index===0?'':('_leave');
    const file=`${n}_${name}${label}${ext}`;
    const dest=path.join(originals,file);
    fs.copyFileSync(from,dest);
    fs.copyFileSync(from,path.join(ready,file));
    const hash=crypto.createHash('sha256').update(fs.readFileSync(dest)).digest('hex');
    const relfile=`${n}_${name}/originals/${file}`;
    licenses.push(`| ${n} | \`${relfile}\` | ${lic.page} | ${lic.license} | ${lic.author} | ${lic.attribution} | \`${hash}\` |`);
  }
  report.push(`| ${n} | ${name} | PASS | \`originals/${n}_${name}${path.extname(src)}\`${second?' + leave cue':''} | ${note} |`);
}
licenses.push('','## Credit text for release','','- Crowd ambience and cheer: **Gregor Quendel**, [Free Crowd Cheering Sounds](https://opengameart.org/content/free-crowd-cheering-sounds), CC BY 4.0.','- City traffic ambience: **Gregor Quendel**, [Free General Ambience Sounds](https://opengameart.org/content/free-general-ambience-sounds), CC BY-SA 4.0. If modified, retain the applicable share-alike terms and indicate changes.','','License references: https://creativecommons.org/publicdomain/zero/1.0/ · https://creativecommons.org/licenses/by/4.0/ · https://creativecommons.org/licenses/by-sa/4.0/ · https://pixabay.com/service/license-summary/');
report.push('','## Remaining work','','- Audition all candidate sounds in game, especially the generic punch variants, sneaker footwork, bell, result cues and music.','- Trim the 5:06 parking-garage recording to a suitable quiet passage, and check loop seams for crowd, city and garage ambience.','- Transcode MP3/WAV files in `unity_ready` to OGG when an encoder is available.');
fs.writeFileSync(path.join(root,'LICENSES.md'),licenses.join('\n')+'\n');
fs.writeFileSync(path.join(root,'AUDIO_ASSET_REPORT.md'),report.join('\n')+'\n');
console.log(`Wrote ${data.length} asset folders, ${data.filter(x=>!x[2]&&x[0]!==380).length} FAIL entries`);
