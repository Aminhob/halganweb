import fs from 'node:fs/promises';
import path from 'node:path';
import {build} from 'esbuild';
import sharp from 'sharp';
import {execFileSync} from 'node:child_process';
import * as t from '../src/templates.mjs';
import {milestones} from '../src/content.mjs';
try{await fs.access('public/assets/logo.webp');}catch{
 const source=process.env.HALGAN_ASSET_ROOT||path.resolve('..');
 await fs.access(path.join(source,'01_BRANDING')).catch(()=>{throw new Error('Official assets missing. Run node scripts/prepare-assets.mjs /path/to/halganweb or set HALGAN_ASSET_ROOT.');});
 execFileSync(process.execPath,['scripts/prepare-assets.mjs',source],{stdio:'inherit'});
}
await fs.rm('dist',{recursive:true,force:true});
await fs.mkdir('dist',{recursive:true});
await fs.cp('public','dist',{recursive:true});
await fs.copyFile('src/styles.css','dist/styles.css');
await build({entryPoints:['src/app.js'],outdir:'dist',bundle:true,format:'esm',splitting:true,chunkNames:'chunks/[name]-[hash]',minify:true,target:['es2022'],logLevel:'warning'});
const routes=[
 ['/', 'The Next Generation of Boxing','Discover HALGAN: a mobile-first Android 3D boxing game in development, with competitive fights and a compact social city.',t.home()],
 ['/game/','The Game','Discover the HALGAN game vision, competitive boxing, character customization and the compact social city.',t.game()],
 ['/fighters/','Fighters & Legends','Explore original HALGAN character development designs and the planned fighter collections.',t.fighters()],
 ['/modes/','Game Modes','Explore Quick Fight, Ranked, Private Fight and the planned Daily Champion competition.',t.modePage()],
 ['/city/','HALGAN City','Explore the concept for HALGAN’s compact social city, centered on boxing.',t.city()],
 ['/shop/','The HALGAN Showroom','Browse HALGAN development designs, compare original assets and inspect interactive 3D models.',t.shop()],
 ['/rewards/','Rewards & Progression','A look at planned HALGAN Coins, Energy, rewards and progression systems.',t.rewards()],
 ['/media/','Media & Gallery','Official HALGAN mascot artwork and character development visuals.',t.media()],
 ['/development/','Development Journey','Follow verified HALGAN asset, branding and animation milestones.',t.development()],
 ['/news/','News & Announcements','Verified HALGAN development notes, identity updates and asset milestones.',t.news()],
 ['/coming-soon/','Coming Soon on Android','HALGAN is in development for Android. No official release date has been announced.',t.coming()],
 ['/about/','About HALGAN','Discover HALGAN GAME, its original identity and boxing-first development vision.',t.about()]
];
for(const item of t.catalog){routes.push([`/shop/${item.slug}/`,item.name,item.description,t.detail(item)]);if(item.category==='Fighters')routes.push([`/fighters/${item.slug}/`,item.name,item.description,t.detail(item,{fighter:true})]);}
for(const m of milestones)routes.push([`/news/${m.slug}/`,m.title,m.body,t.article(m)]);
for(const [route,title,description,body] of routes){const folder='dist'+route;await fs.mkdir(folder,{recursive:true});await fs.writeFile(folder+'index.html',t.layout({title,description,path:route,body,noindex:true}));}
await fs.writeFile('dist/404.html',t.layout({title:'Page Not Found',description:'Return to the HALGAN website.',path:'/404.html',body:t.notFound(),noindex:true}));
// Public artifacts contain no private development records. The current hosting audience is owner-private.
await fs.writeFile('dist/robots.txt','User-agent: *\nDisallow: /\n');
const origin='https://halgan-game.blushcalf9.chatgpt.site';
await fs.writeFile('dist/sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+routes.map(([r])=>`<url><loc>${origin}${r}</loc></url>`).join('')+'</urlset>');
await fs.writeFile('dist/_headers',`/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self'; connect-src 'self'; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; frame-ancestors 'self' https://chatgpt.com; form-action 'none'\n/assets/*\n  Cache-Control: public, max-age=86400\n/chunks/*\n  Cache-Control: public, max-age=31536000, immutable\n`);
// Social artwork uses only the unmodified official logo and mascot, resized for web delivery.
const bg=await sharp({create:{width:1200,height:630,channels:4,background:'#090A0D'}}).png().toBuffer();
const boxer=await sharp('public/assets/hero.webp').resize({height:620}).toBuffer();
const logo=await sharp('public/assets/logo.webp').resize({width:540}).toBuffer();
await sharp(bg).composite([{input:boxer,left:530,top:10},{input:logo,left:45,top:235}]).webp({quality:88}).toFile('dist/assets/social-share.webp');
await fs.writeFile('docs/routes.json',JSON.stringify(routes.map(([route,title])=>({route,title})),null,2));
console.log(`Built ${routes.length} routes + 404. Lazy Three.js chunk; ${t.catalog.length} optimized models.`);
