// Offline SVG export. Requires Playwright and Chromium or Microsoft Edge.
const fs = require('fs');
const path = require('path');
let pw;
try { pw = require('playwright'); }
catch (_) {
  pw = require(process.env.HALGAN_PLAYWRIGHT_PATH || 'C:/Users/pc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
}
(async () => {
  const tasks = process.argv[2].endsWith('.json')
    ? JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))
    : [{svg:process.argv[2], png:process.argv[3]}];
  let browser;
  try { browser = await pw.chromium.launch({headless:true}); }
  catch (_) { browser = await pw.chromium.launch({headless:true, channel:'msedge'}); }
  try {
    for (const task of tasks) {
      const svg = fs.readFileSync(task.svg, 'utf8');
      const width = Number(svg.match(/\bwidth="([\d.]+)"/)[1]);
      const height = Number(svg.match(/\bheight="([\d.]+)"/)[1]);
      const page = await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
      await page.setContent('<html><head><style>body{margin:0;background:transparent}svg{display:block}</style></head><body>' + svg + '</body></html>');
      await page.evaluate(async () => {
        await Promise.all([document.fonts.load('600 32px Teko'),document.fonts.load('400 32px Teko')]);
        await document.fonts.ready;
      });
      const audit = await page.evaluate(() => {
        const errors=[];
        for (const el of document.querySelectorAll('svg text')) {
          const rect=el.getBoundingClientRect();
          if (!['300','400','500','600'].includes(getComputedStyle(el).fontWeight)) errors.push('Unapproved weight: '+el.textContent);
          if (rect.left < -1 || rect.right > innerWidth+1 || rect.top < -1 || rect.bottom > innerHeight+1) errors.push(el.textContent);
          if (getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g,'').trim() !== 'Teko') errors.push('Wrong font: '+el.textContent);
        }
        if (!document.fonts.check('600 32px Teko') || !document.fonts.check('400 32px Teko')) errors.push('Teko not loaded');
        return errors;
      });
      if (audit.length) throw Error(path.basename(task.svg)+': '+audit.join('; '));
      await page.screenshot({path:task.png,omitBackground:true});
      await page.close();
      console.log(path.basename(task.svg));
    }
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode=1; });
