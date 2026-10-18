from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import numpy as np, io, base64, html, csv, json, hashlib, shutil, zipfile
import subprocess, os, xml.etree.ElementTree as ET
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader, simpleSplit
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'HALGAN_FULL_BRANDING_APPROVED_2026'
TMP=ROOT/'__pycache__'/'approved_branding_qa'; TMP.mkdir(parents=True,exist_ok=True)
DL=Path(r'C:\Users\pc\Downloads')
sources={k:OUT/'01_OFFICIAL_LOGOS'/('APPROVED_SOURCE_'+k+'.png') for k in ['metallic','monochrome','icon']}
folders=['00_START_HERE','01_OFFICIAL_LOGOS','02_ANDROID_APP_ICONS','03_UNITY_GAME_ASSETS','04_SOCIAL_MEDIA','05_LIVESTREAM','06_WEBSITE_MARKETING','07_MERCHANDISE_PRINT','08_BRAND_GUIDELINES','09_EDITABLE_SOURCES','10_PREVIEWS','11_OFFICIAL_FONTS']
for f in folders:(OUT/f).mkdir(parents=True,exist_ok=True)
BLACK='#090A0D'; PANEL='#171A20'; RED='#E50909'; SILVER='#C8CBD0'; WHITE='#F4F5F7'; MUTED='#A5ABB6'
records={}; layouts=[]

def save(im,rel,purpose='',dpi=None):
 p=OUT/rel; im.save(p,**({'dpi':dpi} if dpi else {})); records[rel]=purpose; return p
def fit(im,w,h):
 k=min(w/im.width,h/im.height); return im.resize((max(1,round(im.width*k)),max(1,round(im.height*k))),Image.Resampling.LANCZOS)
def place(canvas,im,box):
 x,y,w,h=box; s=fit(im,w,h); canvas.alpha_composite(s,(round(x+(w-s.width)/2),round(y+(h-s.height)/2)))
def color(im,col):
 result=Image.new('RGBA',im.size,col); result.putalpha(im.getchannel('A')); return result
def data(im):
 b=io.BytesIO(); im.save(b,format='PNG'); return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
def font(size,bold=True):
 return ImageFont.truetype(str(OUT/'11_OFFICIAL_FONTS/static'/('Teko-SemiBold.ttf' if bold else 'Teko-Regular.ttf')),int(size))
def label(d,xy,s,size,fill=WHITE,anchor=None,bold=True):
 d.text(xy,s,font=font(size,bold),fill=fill,anchor=anchor)

metal=Image.open(sources['metallic']).convert('RGBA')
master=metal.crop(metal.getchannel('A').getbbox())
mono_src=Image.open(sources['monochrome']).convert('RGB')
lum=np.array(ImageOps.grayscale(mono_src)).astype(np.float32)
alpha=np.clip((225-lum)*255/140,0,255).astype(np.uint8)
alpha[alpha<28]=0
mono=Image.new('RGBA',mono_src.size,'black'); mono.putalpha(Image.fromarray(alpha)); mono=mono.crop(mono.getchannel('A').getbbox())
white=color(mono,'white'); silver=color(mono,SILVER)
app=Image.open(sources['icon']).convert('RGBA')
# Preserve originals exactly, including alpha and their pixel dimensions.
for role,p in sources.items():
 dst=OUT/'01_OFFICIAL_LOGOS'/('APPROVED_SOURCE_'+role+p.suffix)
 if p.resolve()!=dst.resolve():shutil.copy2(p,dst)
for name,im in [('metallic',master),('black',mono),('white',white),('silver',silver)]:
 save(im,f'01_OFFICIAL_LOGOS/HALGAN_{name}_native.png',f'Approved {name} artwork; mono colors derive from supplied mono image')
 for w in [4096,2048,1024,512]:
  size=(w,round(w*.42)); sheet=Image.new('RGBA',size,(0,0,0,0)); place(sheet,im,(w*.075,size[1]*.1,w*.85,size[1]*.8))
  save(sheet,f'01_OFFICIAL_LOGOS/HALGAN_{name}_{w}.png','Transparent artwork with clear space; enlargement adds no source detail')
for tag,bg in [('dark',BLACK),('light',WHITE),('red',RED)]:
 p=Image.new('RGBA',(1920,800),bg); place(p,master if tag=='dark' else mono if tag=='light' else white,(140,120,1640,550)); save(p,f'01_OFFICIAL_LOGOS/HALGAN_on_{tag}.png','Background usage preview')

# Approved illustration is the sole app/profile icon artwork.
def icon(n,opaque=False,round_mask=False):
 p=Image.new('RGBA',(n,n),BLACK if opaque else (0,0,0,0))
 place(p,app,(0,0,n,n))
 if round_mask:
  p=Image.new('RGBA',(n,n),BLACK); place(p,app,(n*.1,n*.1,n*.8,n*.8))
  mask=Image.new('L',(n,n));ImageDraw.Draw(mask).ellipse((0,0,n-1,n-1),fill=255);p.putalpha(mask)
 return p
for n in [48,72,96,144,192,256,512,1024]:save(icon(n),f'02_ANDROID_APP_ICONS/HALGAN_launcher_{n}.png','Supplied approved icon resized, with transparency')
save(icon(512,opaque=True).convert('RGB'),'02_ANDROID_APP_ICONS/HALGAN_store_icon_512.png','Opaque square export of approved app icon')
save(icon(1024,opaque=True).convert('RGB'),'02_ANDROID_APP_ICONS/HALGAN_store_icon_1024.png','Opaque square store source')
save(icon(512,round_mask=True),'02_ANDROID_APP_ICONS/HALGAN_round_preview_512.png','Circular-mask preview, using entire supplied artwork within safe area')
fg=Image.new('RGBA',(432,432),(0,0,0,0));place(fg,app,(84,84,264,264));save(fg,'02_ANDROID_APP_ICONS/HALGAN_adaptive_foreground_432.png','Safe inset raster artwork; not a separated photo subject')
save(Image.new('RGB',(432,432),BLACK),'02_ANDROID_APP_ICONS/HALGAN_adaptive_background_432.png','Opaque black adaptive background')
for n in [800,400]:save(icon(n),f'04_SOCIAL_MEDIA/HALGAN_profile_{n}.png','Approved illustration for profile image')
for n in [16,32,48,180,192]:save(icon(n,opaque=True),f'06_WEBSITE_MARKETING/HALGAN_favicon_{n}.png','Approved app artwork; smallest sizes are identification-only')
icon(256,opaque=True).save(OUT/'06_WEBSITE_MARKETING/favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])

# All layout SVGs embed the approved artwork and contain editable text/shapes.
# No SVG is presented as a vector reconstruction of the raster logos.
logo_url=data(master); white_url=data(white); icon_url=data(app)
def esc(s):return html.escape(str(s))
def txt(x,y,s,size=40,fill=WHITE,weight=600,spacing=0,anchor='start'):
 return f'<text x="{x}" y="{y}" fill="{fill}" font-family="Teko, sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" text-anchor="{anchor}">{esc(s)}</text>'
def image_tag(url,x,y,w,h):return f'<image href="{url}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>'
def rect(x,y,w,h,fill=PANEL,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"/>'
def teko_svg_style():
 encoded=base64.b64encode((OUT/'11_OFFICIAL_FONTS/Teko-Variable.ttf').read_bytes()).decode()
 return '<style>@font-face {font-family:Teko; font-style:normal; font-weight:300 600; src:url(data:font/ttf;base64,'+encoded+') format("truetype");}</style>'

def export_svg(svg,folder,name,w,h,purpose):
 svg=svg.replace('><title>', '>'+teko_svg_style()+'<title>',1) if '<title>' in svg else svg.replace('>', '>'+teko_svg_style(),1)
 sp=OUT/f'09_EDITABLE_SOURCES/{name}.svg';sp.write_text(svg,encoding='utf-8');records[sp.relative_to(OUT).as_posix()]='Self-contained editable layout; embedded approved raster artwork'
 p=OUT/f'{folder}/{name}.png'; subprocess.run([os.environ.get('HALGAN_NODE','node'),str(OUT/'09_EDITABLE_SOURCES/render_svg_with_teko.cjs'),str(sp),str(p)],check=True)
 records[p.relative_to(OUT).as_posix()]=purpose;layouts.append((name,p))
 return p

def layout(folder,name,w,h,title,details='[EVENT / DATE]',category='HALGAN BOXING GAME',style='poster',rows=None):
 # Typography is supporting content. The approved logo remains unchanged.
 m=w*.075; tall=h>w*1.12; scale=w/1080
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{esc(name)}</title><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#22262E"/><stop offset=".5" stop-color="#090A0D"/><stop offset="1" stop-color="#180608"/></linearGradient><linearGradient id="accent"><stop stop-color="#7C0000"/><stop offset="1" stop-color="#E50909"/></linearGradient></defs>'
 svg+=rect(0,0,w,h,'url(#bg)')
 # Restrained ring-line motif and a sweeping red band echo the approved punch.
 svg+=f'<path d="M{w*.56} 0 L{w*.32} {h} M{w*.77} 0 L{w*.53} {h} M{w*.98} 0 L{w*.74} {h}" stroke="#ffffff" stroke-opacity=".035" stroke-width="{w*.08}"/>'
 svg+=rect(m,h*.075,w*.055,max(4,h*.006),RED)
 svg+=txt(m+w*.075,h*.083,category,16*scale,MUTED,600,2.5*scale)
 if style=='youtube-banner':
  # All essential material fits the central channel-banner safe region.
  svg+=image_tag(logo_url,(w-1350)/2,(h-390)/2-40,1350,390)
  svg+=txt(w/2,h/2+155,'THE RING IS YOURS',38,WHITE,600,5,'middle')
 elif style=='wide':
  svg+=image_tag(logo_url,m,h*.16,w*.52,h*.29)
  sz=min(w*.048,h*.11)
  if len(title)>22:sz*=.76
  while font(sz).getlength(title)>w*.55:sz*=.95
  svg+=txt(m,h*.61,title,sz,WHITE)
  svg+=txt(m,h*.71,details,min(w*.02,h*.044),MUTED,400)
  svg+=image_tag(icon_url,w*.68,h*.15,w*.26,h*.67)
  svg+=rect(m,h*.8,w*.22,h*.058,RED,3)+txt(m+w*.11,h*.839,'[CALL TO ACTION]',w*.012,WHITE,600,0,'middle')
 else:
  svg+=image_tag(logo_url,m,h*.125,w*.85,h*(.2 if tall else .22))
  top=h*(.43 if tall else .5); sz=w*.071
  if len(title)>20:sz*=.69
  elif len(title)>15:sz*=.83
  svg+=txt(m,top,title,sz,WHITE)
  svg+=rect(m,top+h*.035,w*.07,max(4,h*.006),RED)
  svg+=txt(m,top+h*.093,details,w*.026,MUTED,400)
  if rows:
   start=top+h*.14; rowh=min(h*.075,(h*.87-start)/len(rows)); fs=min(w*.026,rowh*.31)
   for i,r in enumerate(rows):
    svg+=rect(m,start+i*rowh,w*.85,rowh*.79,'#1C2027',3)
    svg+=rect(m,start+i*rowh,w*.006,rowh*.79,RED)
    svg+=txt(m+w*.025,start+i*rowh+rowh*.5,r,fs,WHITE,500 if '[SCORE]' in r else 400)
  else:
   # Supporting icon is present below the title in tall campaign layouts.
   if tall:svg+=image_tag(icon_url,w*.57,h*.61,w*.33,h*.26)
   svg+=txt(m,h*.8,'[CAMPAIGN MESSAGE]',w*.026,WHITE,400)
  svg+=f'<path d="M0 {h*.93} Q{w*.51} {h*.83} {w} {h*.97} L{w} {h} L0 {h} Z" fill="url(#accent)"/>'
 svg+=txt(m,h*.965,'HALGAN',max(12,w*.018),WHITE,600,3*scale)
 svg+=txt(w-m,h*.965,'[WEBSITE / SOCIAL HANDLE]',max(11,w*.014),WHITE,400,0,'end')
 svg+='</svg>'
 return export_svg(svg,folder,name,w,h,'Branded template: replace bracketed text before publishing')

for name,title,rows in [
 ('daily_challenge','DAILY CHALLENGE',['[CHALLENGE / RULES]','[REWARD / ENTRY]']),
 ('top_32_qualifiers','TOP 32 QUALIFIERS',['[PLAYER 01]  /  [PLAYER 02]  /  [PLAYER 03]','[ADD QUALIFIER LIST IN EDITABLE SOURCE]']),
 ('championship_final','CHAMPIONSHIP FINAL',['[CONTENDER A]  VS  [CONTENDER B]','[TIME / STREAM PLATFORM]']),
 ('winner','CHAMPION',['[PLAYER NAME]','[EVENT / RESULT]']),
 ('leaderboard','LEADERBOARD',['01  [PLAYER]                      [SCORE]','02  [PLAYER]                      [SCORE]','03  [PLAYER]                      [SCORE]','04  [PLAYER]                      [SCORE]']),
 ('game_update','GAME UPDATE',['[VERSION / FEATURE]','[ADDITIONAL PATCH NOTES]'])]:
 layout('04_SOCIAL_MEDIA',name+'_1080x1350',1080,1350,title,rows=rows,category='COMPETITION / COMMUNITY')
for name,w,h,title in [('square_post',1080,1080,'[HEADLINE]'),('portrait_post',1080,1350,'[HEADLINE]'),('story',1080,1920,'[HEADLINE]'),('reel_cover',1080,1920,'[REEL TITLE]')]:
 layout('04_SOCIAL_MEDIA',name+f'_{w}x{h}',w,h,title)
layout('04_SOCIAL_MEDIA','youtube_banner_2560x1440',2560,1440,'',style='youtube-banner')
for name,title in [('youtube_thumbnail','[VIDEO TITLE]'),('livestream_thumbnail','LIVE IN THE RING')]:layout('04_SOCIAL_MEDIA',name+'_1280x720',1280,720,title,style='wide')
for name,title in [('starting_soon','STARTING SOON'),('be_right_back','BE RIGHT BACK'),('stream_ending','STREAM ENDING'),('champion_announcement','CHAMPION')]:layout('05_LIVESTREAM',name+'_1920x1080',1920,1080,title,style='wide',category='HALGAN LIVE')
for name,title in [('android_splash','ENTER THE RING'),('landscape_loading','LOADING'),('maintenance','MAINTENANCE'),('update_announcement','GAME UPDATE')]:layout('02_ANDROID_APP_ICONS',name+'_1920x1080',1920,1080,title,style='wide',category='HALGAN / ANDROID')
for name,w,h,title in [('social_share',1200,630,'ENTER THE RING'),('promotional_banner',1920,600,'THE RING IS YOURS'),('game_launch',1080,1350,'ENTER THE RING'),('download_promotion',1080,1350,'PLAY HALGAN'),('sponsor_placement',1920,1080,'CHAMPIONSHIP')]:
 layout('06_WEBSITE_MARKETING',name+f'_{w}x{h}',w,h,title,style='wide' if w>h else 'poster',rows=['[SPONSOR LOGO / NAME]'] if name=='sponsor_placement' else None)

# Real transparent overlays leave gameplay and webcam openings unpainted.
def overlay_svg(w,h,body):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">{body}</svg>'
export_svg(overlay_svg(1920,1080,rect(0,0,1920,118,BLACK)+rect(0,0,1920,6,RED)+image_tag(logo_url,30,18,360,90)+txt(442,75,'LIVE',34,RED)+txt(1860,73,'[EVENT / ROUND]',26,MUTED,400,0,'end')),'05_LIVESTREAM','HALGAN_live_overlay_1920x1080',1920,1080,'Transparent gameplay overlay')
export_svg(overlay_svg(700,440,'<rect x="4" y="4" width="692" height="432" fill="none" stroke="#E50909" stroke-width="8"/>'+rect(0,392,600,48,BLACK)+txt(24,423,'HALGAN  /  [CREATOR]',22)),'05_LIVESTREAM','HALGAN_webcam_frame_700x440',600,440,'Transparent webcam frame')
export_svg(overlay_svg(1500,180,rect(3,3,1494,174,BLACK,10)+rect(3,3,1494,5,RED)+txt(48,105,'[PLAYER A]',37,WHITE,600)+txt(750,111,'[00]   :   [00]',54,WHITE,500,0,'middle')+txt(1452,105,'[PLAYER B]',37,WHITE,600,0,'end')),'05_LIVESTREAM','HALGAN_scoreboard_1500x180',1500,180,'Transparent scoreboard overlay')
for n,im,w in [('stream_watermark',white,350),('title_screen_logo',master,2048),('ui_logo',master,1024),('ui_logo_small',master,512),('loading_logo',master,1024),('hud_logo_white',white,512),('hud_logo_silver',silver,512),('watermark_logo',white,320)]:
 folder='05_LIVESTREAM' if n=='stream_watermark' else '03_UNITY_GAME_ASSETS';save(fit(im,w,w),f'{folder}/{n}_{w}.png','Transparent source-derived UI artwork; preserve aspect ratio')
save(icon(512),'03_UNITY_GAME_ASSETS/app_icon_512.png','Supplied approved icon')
for n,im,w in [('header_logo',master,900),('footer_logo_white',white,650),('press_kit_master_logo',master,2164)]:save(fit(im,w,w),f'06_WEBSITE_MARKETING/{n}.png','Approved artwork export')

for name,w,h,im in [('tshirt_front',3600,3600,master),('hoodie_front',3600,3600,master),('cap_front',1800,900,white),('gloves_mark',1200,1200,white)]:
 p=Image.new('RGBA',(w,h),(0,0,0,0));place(p,im,(w*.12,h*.2,w*.76,h*.6));save(p,f'07_MERCHANDISE_PRINT/{name}_flat_transparent.png','Flat print placement; not a garment photo or vector master',(300,300))
for name,w,h,title in [('event_backdrop',3840,2160,'HALGAN CHAMPIONSHIP'),('promotional_poster',2400,3600,'ENTER THE RING'),('championship_banner',3840,1440,'CHAMPIONSHIP')]:layout('07_MERCHANDISE_PRINT',name,w,h,title,'[EVENT / VENUE / DATE]',style='wide' if w>h else 'poster',category='HALGAN / EVENT')

# Include the exact generator so every raster layout can be regenerated.
tokens={'colors':{'black':BLACK,'charcoal':PANEL,'punch_red':RED,'silver':SILVER,'white':WHITE,'muted':MUTED},'official_typography':{'family':'Teko','approved_on':'2026-10-14','headline_weight':600,'navigation_weight':600,'stats_weight':500,'body_weight':400,'font_folder':'11_OFFICIAL_FONTS'},'supporting_typography':{'headline':'Teko SemiBold','body':'Teko Regular'},'logo_type':'Approved raster artwork. Never typeset the HALGAN logo.'}
# Retain the secondary color and semantic roles from the existing canonical tokens.
existing_tokens=json.loads((OUT/'09_EDITABLE_SOURCES/brand_tokens.json').read_text(encoding='utf-8'))
tokens['colors']['electric_blue']=existing_tokens['colors']['electric_blue']
tokens['brand_color_roles']=existing_tokens['brand_color_roles']
tokens['official_typography'].update({k:existing_tokens['official_typography'][k] for k in ['allowed_variants','policy_updated_on']})
(OUT/'09_EDITABLE_SOURCES/brand_tokens.json').write_text(json.dumps(tokens,indent=2),encoding='utf-8')
(OUT/'09_EDITABLE_SOURCES/brand_tokens.css').write_text('\n'.join('@font-face { font-family: "Teko"; font-style: normal; font-weight: '+str(w)+'; font-display: swap; src: url("../11_OFFICIAL_FONTS/web/teko-latin-'+str(w)+'-normal.woff") format("woff"); }' for w in [300,400,500,600])+'\n:root {\n'+''.join(f'  --halgan-{k.replace("_","-")}: {v};\n' for k,v in tokens['colors'].items())+'  --halgan-primary: var(--halgan-punch-red);\n  --halgan-secondary: var(--halgan-electric-blue);\n  --halgan-font-family: "Teko", sans-serif;\n  --halgan-headline-weight: 600;\n  --halgan-navigation-weight: 600;\n  --halgan-stats-weight: 500;\n  --halgan-body-weight: 400;\n}\n',encoding='utf-8')
(OUT/'03_UNITY_GAME_ASSETS/IMPORT_SETTINGS.md').write_text('Import as Sprite (2D and UI), Single. Enable alpha transparency. Disable mipmaps for screen-space UI. Preserve aspect ratio. Test compression at actual display size; use uncompressed RGBA if fine subtitle edges degrade. The provided PNGs are raster art. Do not stretch sprites.\n\nOfficial font: Teko. Import TTF files from 11_OFFICIAL_FONTS/static, generate TextMeshPro Font Assets, and assign Regular 400, Medium 500, SemiBold 600; Light 300 for decorative secondary text according to HALGAN_TYPOGRAPHY.md. Include required characters and check text at actual mobile size.\n',encoding='utf-8')
source_info={k:{'file':str(v),'sha256':hashlib.sha256(v.read_bytes()).hexdigest(),'size':Image.open(v).size} for k,v in sources.items()}
(OUT/'00_START_HERE/APPROVED_SOURCES.json').write_text(json.dumps(source_info,indent=2),encoding='utf-8')
(OUT/'00_START_HERE/README.md').write_text('''# HALGAN approved branding kit

This kit uses the three images approved in the current chat: metallic cutout logo, supplied monochrome logo, and supplied boxing app icon. They replace the earlier reconstruction candidate and previous kit identities. No logo reconstruction is used here.

The exact originals are in 01_OFFICIAL_LOGOS. Full-color exports preserve the supplied silver material, red brush stroke and boxer. Black, white and silver flat versions derive from the supplied monochrome artwork, with its white image background removed. The app and profile icons use the supplied boxer illustration.

Folders 02 and 03 contain Android and Unity exports; 04 social templates; 05 livestream cards and transparent overlays; 06 web and marketing; 07 flat print assets and event art; 08 the PDF guide; 09 self-contained editable SVG layouts and color tokens; 10 previews; 11 official Teko fonts. See MANIFEST.csv for every file.

Edit text and shapes in the SVG templates with an SVG-capable editor. The approved logos and icon remain embedded raster images. These are editable layout files, not vector logo masters. Teko is the official HALGAN GAME font. See 11_OFFICIAL_FONTS for installable fonts, webfonts and the SIL OFL license. The logo remains approved artwork. Keep the artwork proportions intact.

Replace all bracketed placeholders before publishing. Dates, contenders, results, scores, download destinations and sponsor data are intentionally blank. The YouTube banner keeps primary content inside a central 1350 x 390 region; preview crops in the destination UI.

Raster source sizes: metallic 2164 x 727, monochrome 1672 x 941, icon 1254 x 1254. Larger exports add layout convenience, not new optical detail. Supplied edge texture and brush roughness are retained. Tiny favicons retain the approved icon but cannot retain subtitle legibility.

The store icon has an opaque square background. Adaptive foreground is an inset version of the entire supplied icon, not a separately extracted boxer. Android mask previews are provided; test in your launcher build.

Print artwork is RGB raster at the listed pixel dimensions. 300 DPI metadata in garment placement sheets does not increase source detail. Final size, color conversion, bleed and garment print process depend on your supplier. The PDF guide is a digital brand reference.
''',encoding='utf-8')

# Brand guide: designed pages, with bounded text flow and reference artwork.
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
for face in ['Light','Regular','Medium','SemiBold']:
 pdfmetrics.registerFont(TTFont('Teko-'+face,str(OUT/'11_OFFICIAL_FONTS/static'/('Teko-'+face+'.ttf'))))
pdf=OUT/'08_BRAND_GUIDELINES/HALGAN_APPROVED_BRAND_GUIDE.pdf'
c=canvas.Canvas(str(pdf),pagesize=(720,960)); c.setTitle('HALGAN - Approved Brand Guide'); c.setAuthor('HALGAN')
page_no=0
def page(kicker,title):
 global page_no
 page_no+=1;c.setFillColor(BLACK);c.rect(0,0,720,960,fill=1,stroke=0);c.setFillColor(RED);c.rect(48,875,42,5,fill=1,stroke=0)
 c.setFillColor(MUTED);c.setFont('Teko-SemiBold',14);c.drawString(104,874,kicker)
 c.setFillColor(WHITE);c.setFont('Teko-SemiBold',38);c.drawString(48,817,title)
 c.setStrokeColor('#30343D');c.line(48,62,672,62);c.setFont('Teko-Regular',12);c.setFillColor(MUTED);c.drawString(48,40,'HALGAN / APPROVED BRAND SYSTEM / 2026');c.drawRightString(672,40,f'{page_no:02d}')
def prose(title,body,y):
 c.setFillColor(WHITE);c.setFont('Teko-SemiBold',19);c.drawString(48,y,title);y-=22
 c.setFillColor(MUTED);c.setFont('Teko-Regular',15)
 for ln in simpleSplit(body,'Teko-Regular',15,624):c.drawString(48,y,ln);y-=17
 return y-22
def pic(im,x,y,w,h):
 s=fit(im,w,h);c.drawImage(ImageReader(s),x+(w-s.width)/2,y+(h-s.height)/2,width=s.width,height=s.height,mask='auto')
page('01 / THE IDENTITY','The ring is yours.')
pic(master,48,585,624,200);pic(app,430,120,235,220)
y=535;y=prose('HALGAN BOXING GAME','A cinematic boxing identity built around silver, punch red and black. The supplied metallic logo, flat logo and boxer icon are the approved visual assets.',y)
prose('Identity hierarchy','Use the full logo for title screens and major announcements. Use the supplied illustration for app and profile icons. Use the supplied monochrome mark when one color or stronger contrast is needed.',y)
c.showPage()
page('02 / APPROVED ASSETS','One identity. Three source assets.')
pic(master,48,598,624,160);c.setFillColor(WHITE);c.rect(48,370,624,180,fill=1,stroke=0);pic(mono,68,385,584,145)
pic(app,48,100,150,130);prose('The supplied boxer icon','Use the approved full composition. Do not substitute a cropped letter, a new boxer or another app symbol.',315)
c.showPage()
page('03 / USE AND CLEAR SPACE','Keep the mark intact.')
pic(master,92,600,536,150);c.setStrokeColor(RED);c.setDash(5,4);c.rect(48,565,624,220,fill=0,stroke=1);c.setDash()
y=510
for a,b in [('Clear space','Keep at least 10% of the visible logo width free on each side. Measure from the outer artwork, including the red stroke.'),('Recommended minimums','Use the complete metallic mark at 320 px wide or larger. Use the flat mark at 240 px wide or larger. Check the BOXING GAME subtitle at actual size. Below this, use the approved icon.'),('Backgrounds','Metallic on black or charcoal; black flat mark on light surfaces; white flat mark on dark or red surfaces. Avoid placing silver over bright imagery without a dark field.'),('Preserve','Keep aspect ratio, custom letters, boxer placement and red stroke. Do not replace the logo with typed letters, add outlines, recolor the metallic master, rotate or stretch it.')]:y=prose(a,b,y)
c.showPage()
page('04 / COLOR AND TYPE','Red energy. Silver precision.')
y=736
for name,hx in tokens['colors'].items():
 c.setFillColor(hx);c.rect(48,y-27,74,42,fill=1,stroke=0);c.setFillColor(WHITE);c.setFont('Teko-SemiBold',17);c.drawString(145,y,name.replace('_',' ').upper());c.setFont('Teko-Regular',15);c.setFillColor(MUTED);c.drawString(380,y,hx);y-=72
y=prose('Official typography - Teko','Teko SemiBold (600) for headlines; SemiBold (600) for buttons; Medium (500) for stats; Regular (400) for body copy. Installable fonts and the SIL OFL license are in 11_OFFICIAL_FONTS. Use a clear hierarchy with short, direct headings. The HALGAN wordmark is artwork and must never be recreated with a font.',y-5)
prose('Material','Silver is a support color, not a substitute for the brushed metallic master. The supplied highlights, bevels and surface texture remain part of the approved full-color mark.',y)
c.showPage()
page('05 / MOBILE AND GAME','Ready for the title screen.')
pic(app,48,520,235,255);pic(Image.open(OUT/'02_ANDROID_APP_ICONS/android_splash_1920x1080.png'),314,525,358,250)
y=465
for a,b in [('App icon','Use the supplied boxer illustration. Opaque square store exports and transparent launcher sizes are included. Adaptive foreground contains the entire artwork inset against a black background; test masking in your Android build.'),('Unity UI','Use provided PNG sprites with alpha transparency. Import as Sprite, Single; disable mipmaps for screen-space UI. Preserve aspect ratio and test compression on the subtitle.'),('Loading and splash','The provided screens are templates. Implement loading progress, buttons and live status using game UI; replace bracketed copy before release.'),('Small placements','Use the flat white mark for overlays and HUD. The supplied icon becomes identification-only at favicon sizes; tiny subtitle detail is not expected.')]:y=prose(a,b,y)
c.showPage()
page('06 / CONTENT AND BROADCAST','Make every placement consistent.')
pic(Image.open(OUT/'04_SOCIAL_MEDIA/daily_challenge_1080x1350.png'),48,422,244,350)
pic(Image.open(OUT/'05_LIVESTREAM/starting_soon_1920x1080.png'),320,530,352,210)
y=363
for a,b in [('Social templates','Use the metallic mark, a dark field, strong headlines and restrained red accents. Square, portrait, story, channel banner and thumbnail layouts are included.'),('Live broadcast','Full-screen cards, transparent gameplay bar, webcam frame, scoreboard and watermark are included. Keep gameplay, faces and live scores unobstructed.'),('Editable content','Replace bracketed names, scores, dates, links, sponsors and campaign text. The SVG templates contain editable text and shapes with embedded approved raster assets.')]:y=prose(a,b,y)
c.showPage()
page('07 / PRINT AND MERCHANDISE','The approved mark, on material.')
pic(master,48,585,624,175)
y=525
for a,b in [('Flat art','Transparent front placement sheets are supplied for T-shirts, hoodies, caps and gloves. These are flat artwork assets, not garment mockups.'),('Use the right mark','Use the metallic raster for full-color digital or transfer printing. Use the supplied monochrome-derived mark for a single-color treatment. Stitching and screen printing require a vendor-specific proof.'),('Raster resolution','The metallic source is 2164 x 727 pixels. Enlarged layouts and 300 DPI metadata do not create new artwork detail. Ask the printer to confirm whether the chosen physical width is suitable.'),('Event art','Backdrop, banner and poster templates use RGB colors. Final physical dimensions, color conversion, trim and bleed must be set for the actual supplier and substrate.')]:y=prose(a,b,y)
c.showPage()
page('08 / DELIVERY AND QA','Use the approved files.')
y=738
for a,b in [('Source of truth','The three user-supplied source images are preserved byte-for-byte. Their hashes and native dimensions appear in APPROVED_SOURCES.json. Earlier reconstructed logos and older kit versions are not used.'),('Editable source','The SVGs are layout files with editable copy, shapes and embedded PNG artwork. They are self-contained. No vector logo master is claimed.'),('Review checks','PNG files are decoded; logo and overlay transparency is checked; SVG XML and image embedding are checked; PDF pages are rendered for review; manifest file sizes and ZIP integrity are verified.'),('Known limits','Supplied cutout edge roughness and textured red stroke remain unchanged. Transparent mono versions remove the white source background by luminance. Larger raster exports preserve source detail only.'),('Before publishing','Replace every placeholder. Confirm actual dates, names, scores, links and sponsor content. Check destination crops and export settings. Inspect text at final display size.'),('Package navigation','00 start here; 01 logos; 02 Android; 03 Unity; 04 social; 05 livestream; 06 web; 07 print; 08 guide; 09 editable sources; 10 previews; 11 official Teko fonts.')]:y=prose(a,b,y)
c.showPage()
page('09 / OFFICIAL TYPOGRAPHY','Teko. The voice of HALGAN.')
c.setFillColor(WHITE);c.setFont('Teko-SemiBold',76);c.drawString(48,716,'HALGAN GAME')
c.setFillColor(RED);c.setFont('Teko-SemiBold',43);c.drawString(48,648,'FIGHT FOR GLORY')
for label_text,face,weight,y_pos in [('HEADLINES','SemiBold',600,562),('BUTTONS / NAVIGATION','SemiBold',600,495),('SCORE / ROUND / STATS','Medium',500,428),('BODY / DESCRIPTIONS','Regular',400,361),('LARGE SECONDARY DISPLAY','Light',300,294)]:
 c.setFillColor(MUTED);c.setFont('Teko-Regular',14);c.drawString(48,y_pos,label_text+' / '+str(weight))
 c.setFillColor(WHITE);c.setFont('Teko-'+face,31);c.drawString(48,y_pos-34,'Noqo horyaalka HALGAN. 0123456789')
prose('Installation and license','Desktop: install static TTF files. Web: load brand_tokens.css. Unity: import TTF and generate TextMeshPro font assets. Font files and SIL OFL 1.1 license are in 11_OFFICIAL_FONTS.',190)
c.showPage();c.save()

# Preview boards reflect actual exported assets rather than invented mockups.
preview=Image.new('RGBA',(2400,1700),BLACK);d=ImageDraw.Draw(preview)
label(d,(100,85),'HALGAN / APPROVED BRANDING',55)
label(d,(102,165),'METALLIC LOGO   /   FLAT MARK   /   BOXER ICON',24,MUTED)
place(preview,master,(100,230,2200,520))
cards=[('APP ICON',app),('SOCIAL',Image.open(OUT/'04_SOCIAL_MEDIA/daily_challenge_1080x1350.png')),('LIVESTREAM',Image.open(OUT/'05_LIVESTREAM/starting_soon_1920x1080.png'))]
for i,(name,im) in enumerate(cards):
 x=100+i*760;d.rounded_rectangle((x,825,x+680,1460),radius=12,fill=PANEL);place(preview,im.convert('RGBA'),(x+35,855,610,525));label(d,(x+340,1420),name,25,anchor='mm')
for i,cx in enumerate([RED,SILVER,PANEL,WHITE]):d.rectangle((100+i*150,1540,215+i*150,1585),fill=cx)
label(d,(840,1562),'APPROVED ARTWORK / EDITABLE LAYOUTS / FULL ASSET KIT',23,MUTED,anchor='lm')
save(preview,'10_PREVIEWS/HALGAN_full_branding_preview.png','Overview of actual approved kit assets')
sheet=Image.new('RGB',(2400,1800),BLACK);d=ImageDraw.Draw(sheet)
label(d,(60,40),'HALGAN / EXPORTED ASSET CONTACT SHEET',38)
selected=[p for n,p in layouts if 'live_overlay' not in n and 'webcam' not in n and 'scoreboard' not in n][:24]
for i,p in enumerate(selected):
 x=40+(i%6)*395;y=130+(i//6)*410;im=Image.open(p).convert('RGBA');panel=Image.new('RGBA',(365,320),PANEL);place(panel,im,(10,10,345,300));sheet.paste(panel.convert('RGB'),(x,y));label(d,(x,y+340),p.stem[:28],15,MUTED)
save(sheet,'10_PREVIEWS/HALGAN_asset_contact_sheet.png','Actual layout QA contact sheet')

def finalize():
 rows=[];errors=[]
 for p in sorted(OUT.rglob('*')):
  if not p.is_file() or OUT.name in p.relative_to(OUT).parts or '__pycache__' in p.relative_to(OUT).parts or p.name in ['MANIFEST.csv','VALIDATION.txt']:continue
  rel=p.relative_to(OUT).as_posix();dims='';mode=''
  if p.suffix=='.png':
   with Image.open(p) as im:dims=f'{im.width}x{im.height}';mode=im.mode;im.verify()
  if p.suffix=='.svg':
   root=ET.parse(p).getroot()
   for im in root.findall('{http://www.w3.org/2000/svg}image'):
    if not im.attrib.get('href','').startswith(('data:image/png;base64,','data:image/jpeg;base64,')):errors.append('Nonportable image link: '+rel)
  rows.append([rel,p.suffix[1:],dims,mode,records.get(rel,'Approved source or package documentation'),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()])
 for k,src in sources.items():
  copy=OUT/'01_OFFICIAL_LOGOS'/('APPROVED_SOURCE_'+k+src.suffix)
  assert src.read_bytes()==copy.read_bytes()
 for p in ['01_OFFICIAL_LOGOS/HALGAN_metallic_4096.png','01_OFFICIAL_LOGOS/HALGAN_white_2048.png','05_LIVESTREAM/HALGAN_webcam_frame_700x440.png','05_LIVESTREAM/HALGAN_live_overlay_1920x1080.png']:
  im=Image.open(OUT/p);assert im.mode=='RGBA' and im.getchannel('A').getextrema()==(0,255),p
 assert Image.open(OUT/'02_ANDROID_APP_ICONS/HALGAN_store_icon_512.png').mode=='RGB'
 assert len(PdfReader(pdf).pages)==9
 assert not errors,errors
 with (OUT/'00_START_HERE/MANIFEST.csv').open('w',newline='',encoding='utf-8') as f:
  wr=csv.writer(f);wr.writerow(['file','format','dimensions_px','color_mode','purpose','bytes','sha256']);wr.writerows(rows)
 (OUT/'00_START_HERE/VALIDATION.txt').write_text(f'Passed: {len(rows)} manifest entries; PNG decode; exact approved source hashes; alpha on logos and overlays; opaque store icon; self-contained SVG image links; SVG parsing; 9-page PDF; official Teko fonts included. PDF visual review recorded after rendering. No previous reconstructed logos used.\n',encoding='utf-8')
 zp=ROOT/'HALGAN_FULL_BRANDING_APPROVED_2026.zip'
 with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(OUT.rglob('*')):
   if p.is_file() and OUT.name not in p.relative_to(OUT).parts and '__pycache__' not in p.relative_to(OUT).parts:z.write(p,p.relative_to(ROOT).as_posix())
 with zipfile.ZipFile(zp) as z:assert z.testzip() is None
 print(json.dumps({'files':len(rows)+2,'layouts':len(layouts),'zip':str(zp),'zip_mb':round(zp.stat().st_size/1048576,1),'guide':str(pdf)},indent=2))

if Path(__file__).resolve()!=(OUT/'09_EDITABLE_SOURCES/build_approved_branding.py').resolve():
 shutil.copy2(Path(__file__),OUT/'09_EDITABLE_SOURCES/build_approved_branding.py')
finalize()
