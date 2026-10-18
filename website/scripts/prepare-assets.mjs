import fs from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';
import {NodeIO} from '@gltf-transform/core';
import {ALL_EXTENSIONS} from '@gltf-transform/extensions';
import {dedup,prune,textureCompress} from '@gltf-transform/functions';
const root=process.argv[2];
if(!root) throw new Error('Usage: node scripts/prepare-assets.mjs /absolute/path/to/halganweb');
const brand=path.join(root,'01_BRANDING/HALGAN_FULL_BRANDING_APPROVED_2026');
await fs.mkdir('public/assets/fonts',{recursive:true});
for(const weight of [300,400,500,600]) await fs.copyFile(`${brand}/11_OFFICIAL_FONTS/web/teko-latin-${weight}-normal.woff`,`public/assets/fonts/teko-${weight}.woff`);
await fs.copyFile(`${brand}/11_OFFICIAL_FONTS/OFL.txt`,'public/assets/fonts/OFL.txt');
const images={logo:`${brand}/06_WEBSITE_MARKETING/header_logo.png`,icon:`${root}/01_BRANDING/ICONS_FINAL_V2/halgan-icon-256.png`,hero:`${root}/01_BRANDING/MASCOT_FINAL/04-guard-pose-transparent.png`,punch:`${root}/01_BRANDING/MASCOT_FINAL/06-punch-action-transparent.png`,portrait:`${root}/01_BRANDING/MASCOT_FINAL/02-hero-portrait-transparent.png`,neutral:`${root}/01_BRANDING/MASCOT_FINAL/08-full-body-neutral-transparent.png`,turnaround:`${root}/01_BRANDING/MASCOT_FINAL/01-turnaround-transparent.png`};
for(const [name,src] of Object.entries(images)) await sharp(src).resize({width:name==='logo'?900:name==='icon'?192:1400,withoutEnlargement:true}).webp({quality:88}).toFile(`public/assets/${name}.webp`);
const io=new NodeIO().registerExtensions(ALL_EXTENSIONS);
// Only these original HALGAN static assets are allowed into the development showroom.
// Real-person identities, partial robes, raw manifests and Unity packages are never copied.
const entries=[];
const clean=`${root}/04_3D_ASSETS/02_CLEAN_STATIC_MODELS`;
for(const dir of (await fs.readdir(clean)).sort()){
 const match=dir.match(/^(REF\d+)_/); if(!match)continue;
 const id=match[1]; if(['REF044','REF118'].includes(id))continue;
 const src=`${clean}/${dir}`;
 try{
 const validation=JSON.parse(await fs.readFile(`${src}/CLEANUP_VALIDATION.json`,'utf8'));
 if(validation.status!=='CLEANUP_VISUAL_PASS') continue;
 const folder=`public/assets/models`; await fs.mkdir(folder,{recursive:true});
 const doc=await io.read(`${src}/${id}_CLEAN.glb`);
 await doc.transform(dedup(),prune(),textureCompress({encoder:sharp,targetFormat:'webp',resize:[1024,1024]}));
 await io.write(`${folder}/${id}.glb`,doc);
 await sharp(`${src}/AFTER_FRONT.png`).resize({height:780}).webp({quality:85}).toFile(`public/assets/${id}.webp`);
 const name=dir.replace(/^REF\d+_/,'').replaceAll('_',' ');
 const category=id==='REF017'?'Boxing Gloves':id==='REF072'?'Arenas':id==='REF079'?'Arena Art':'Fighters';
 entries.push({id,slug:id.toLowerCase(),name,category,collection:'Development collection',rarity:null,coins:null,releaseStatus:'Development preview',publicApproved:false,model:`/assets/models/${id}.glb`,image:`/assets/${id}.webp`,triangles:validation.triangles,description:category==='Fighters'?'An original HALGAN character study. This static model previews the character design; final identity, abilities and unlock requirements are unannounced.':category==='Arenas'?'An original HALGAN boxing ring with red, white and blue ropes. A development asset preview, presented independently of gameplay.':category==='Boxing Gloves'?'A black and gold boxing glove from the HALGAN asset collection. Preview its materials and silhouette in 360 degrees.':'A framed red shadow-boxer design from the HALGAN environment collection.',compatibility:'Final in-game compatibility unannounced'});
 }catch(error){throw new Error(`${id}: ${error.message}`);}
}
await fs.writeFile('src/catalog.json',JSON.stringify(entries,null,2));
console.log(`Prepared ${entries.length} development assets; no sale eligibility or prices inferred.`);
