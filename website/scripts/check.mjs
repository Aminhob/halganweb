import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import sharp from 'sharp';
import {parseHTML} from 'linkedom';
import {NodeIO} from '@gltf-transform/core';
import {ALL_EXTENSIONS} from '@gltf-transform/extensions';
import {zones} from '../src/content.mjs';
const catalog=JSON.parse(await fs.readFile('src/catalog.json','utf8'));
const routes=JSON.parse(await fs.readFile('docs/routes.json','utf8'));
let links=0,images=0;
for(const {route} of routes){
 const html=await fs.readFile('dist'+route+'index.html','utf8');const {document}=parseHTML(html);
 assert.equal(document.querySelectorAll('h1').length,1,route+' must have one h1');
 assert(document.querySelector('main#main'),route+' semantic main');assert(document.querySelector('title')?.textContent.includes('HALGAN'));
 assert(document.querySelector('meta[name="description"]')?.getAttribute('content').length>20);
 assert(document.querySelector('meta[name="robots"]').content.includes('noindex'));
 for(const img of document.querySelectorAll('img')){assert(img.hasAttribute('alt'),route+' image alt');images++;}
 for(const el of document.querySelectorAll('[href],[src],[data-model]')){
  const ref=el.getAttribute('href')||el.getAttribute('src')||el.getAttribute('data-model');
  if(!ref||/^(https:|data:|blob:|mailto:)/.test(ref))continue;
  if(ref.startsWith('#')){assert(document.getElementById(ref.slice(1)),`${route} missing anchor ${ref}`);continue;}
  const [pathname,hash]=ref.split('#');let file='dist'+pathname;
  if(pathname.endsWith('/'))file+='index.html';
  await fs.access(file).catch(()=>assert.fail(`${route} missing asset/link ${ref}`));
  if(hash&&pathname.endsWith('/')){const {document:target}=parseHTML(await fs.readFile(file,'utf8'));assert(target.getElementById(hash),`${route} missing cross-page anchor ${ref}`)}
  links++;
 }
 assert(!/font-weight\s*:\s*(700|800|900|bold)/i.test(html));
 assert(!/stripe|paypal|buy now|checkout|top.up|\$\d/i.test(html),'Unapproved storefront data on '+route);
}
const io=new NodeIO().registerExtensions(ALL_EXTENSIONS);
for(const item of catalog){
 assert.equal(item.coins,null);assert.equal(item.rarity,null);assert.equal(item.publicApproved,false);
 assert(!['REF044','REF118'].includes(item.id),'Partial robe leaked');
 const model=await io.read('dist'+item.model);const root=model.getRoot();
 assert(root.listMeshes().length>0,item.id+' mesh missing');assert(root.listScenes().length>0,item.id+' scene missing');
 for(const mesh of root.listMeshes())for(const primitive of mesh.listPrimitives()){
 const position=primitive.getAttribute('POSITION');assert(position&&position.getCount()>0,item.id+' empty geometry');
 for(const v of position.getMin([]))assert(Number.isFinite(v));for(const v of position.getMax([]))assert(Number.isFinite(v));}
 for(const tex of root.listTextures()){assert(tex.getImage()?.length>0,item.id+' missing embedded texture');const {width,height}=await sharp(Buffer.from(tex.getImage())).metadata();assert(width<=1024&&height<=1024,item.id+' oversized web texture');}
}
const script=(await fs.readFile('src/app.js','utf8')).replace("import {zones} from './content.mjs';",'').replace("import catalog from './catalog.json';",'');
function harness(route){const {window,document}=parseHTML(globalThis.htmlByRoute[route]);const store=new Map();const medias=new Map();
 const matchMedia=q=>{if(!medias.has(q))medias.set(q,{matches:false,addEventListener(){}});return medias.get(q)};
 for(const select of document.querySelectorAll('select')){let value=select.querySelector('option')?.getAttribute('value')||select.querySelector('option')?.textContent;Object.defineProperty(select,'value',{get:()=>value,set:v=>value=v,configurable:true});}
 const dialog=document.querySelector('dialog');dialog.showModal=()=>{dialog.open=true};dialog.close=()=>{dialog.open=false;dialog.dispatchEvent(new window.Event('close'))};
 const context={window,document,zones,catalog,matchMedia,localStorage:{getItem:k=>store.get(k)||null,setItem:(k,v)=>store.set(k,v)},location:{pathname:route},CustomEvent:window.CustomEvent,console,setTimeout:()=>1,clearTimeout(){}};
 vm.runInNewContext(script,context);return {window,document,store,click:el=>el.dispatchEvent(new window.Event('click',{bubbles:true})),change:el=>el.dispatchEvent(new window.Event('change',{bubbles:true})),input:el=>el.dispatchEvent(new window.Event('input',{bubbles:true}))};}
globalThis.htmlByRoute={};for(const r of ['/shop/','/fighters/','/city/','/media/','/'])htmlByRoute[r]=await fs.readFile('dist'+r+'index.html','utf8');
{
 const h=harness('/shop/'),d=h.document;const input=d.querySelector('#catalog-search'),category=d.querySelector('#catalog-category');
 input.value='glove';h.input(input);assert.equal(d.querySelectorAll('.asset-card:not([hidden])').length,1,'search glove');
 category.value='Arenas';h.change(category);assert.equal(d.querySelectorAll('.asset-card:not([hidden])').length,0,'combined filtering');assert.equal(d.querySelector('#empty-results').hidden,false);
 h.click(d.querySelector('#clear-filters'));assert.equal(d.querySelectorAll('.asset-card:not([hidden])').length,20,'reset filters');
 category.value='Fighters';h.change(category);assert.equal(d.querySelectorAll('.asset-card:not([hidden])').length,17,'fighter category');
 const compare=[...d.querySelectorAll('[data-compare]')];h.click(compare[0]);h.click(compare[1]);h.click(compare[2]);h.click(compare[3]);assert.equal(d.querySelectorAll('[data-compare][aria-pressed="true"]').length,3,'compare limit');
 h.click(d.querySelector('#compare-open'));assert(d.querySelector('dialog').open);assert.equal(d.querySelectorAll('.comparison-table thead th').length,4,'three-column comparison');h.click(d.querySelector('[data-close]'));assert(!d.querySelector('dialog').open);
 h.click(d.querySelector('#compare-clear'));assert(d.querySelector('#compare-bar').hidden,'compare clear');
 h.click(d.querySelector('[data-motion]'));assert(d.documentElement.classList.contains('motion-paused'));assert.equal(h.store.get('halgan-motion'),'paused');
 h.click(d.querySelector('.menu-toggle'));assert(!d.querySelector('#mobile-nav').hidden);assert.equal(d.querySelector('.menu-toggle').getAttribute('aria-expanded'),'true');
}
{
 const h=harness('/fighters/'),d=h.document;const input=d.querySelector('#catalog-search');input.value='REF012';h.input(input);assert.equal(d.querySelectorAll('.asset-card:not([hidden])').length,1,'fighter search');
}
{
 const h=harness('/city/'),d=h.document;h.click(d.querySelector('[data-zone="garage"]'));assert.equal(d.querySelector('#district-title').textContent,'GARAGE & STREETS');assert.equal(d.querySelectorAll('[data-zone="garage"][aria-pressed="true"]').length,2);
}
{
 const h=harness('/media/'),d=h.document;h.click(d.querySelector('[data-lightbox]'));assert(d.querySelector('dialog').open);assert(d.querySelector('.lightbox-image').alt.includes('not a gameplay capture'));h.click(d.querySelector('[data-close]'));h.click(d.querySelector('[data-trailer]'));assert(d.querySelector('#dialog-content').textContent.includes('not available yet'));
}
assert.equal(routes.length,52);assert.equal(catalog.length,20);
const css=await fs.readFile('src/styles.css','utf8');assert(!/font-weight\s*:\s*(700|800|900|bold)/i.test(css));assert(css.includes('prefers-reduced-motion'));assert(css.includes('font-synthesis:none'));
console.log(`PASS: ${routes.length} routes; ${links} local references; ${images} image alt attributes; ${catalog.length} valid GLBs; DOM interaction checks for filters, comparison, motion, menu, map, lightbox and trailer status.`);
console.log('LIMIT: no browser/GPU visual run or Lighthouse measurement available in this environment.');
