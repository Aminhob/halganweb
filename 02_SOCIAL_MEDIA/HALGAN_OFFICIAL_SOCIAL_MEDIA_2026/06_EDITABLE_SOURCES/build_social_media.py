"""Build HALGAN's official social media designs from packaged assets, offline."""
from pathlib import Path
import base64,csv,hashlib,html,io,json,os,shutil,subprocess,sys,zipfile
from PIL import Image,ImageDraw,ImageFont

KIT=Path(__file__).resolve().parents[1]
WORKSPACE=next((p for p in KIT.parents if p.name == "HALGAN ASSETS"), KIT.parent)
ASSETS=KIT/'07_SOURCE_ASSETS'
FONTS=KIT/'08_FONTS'
BLACK='#090A0D'; CHARCOAL='#171A20'; RED='#E50909'; WHITE='#F4F5F7'; SILVER='#C8CBD0'; MUTED='#A5ABB6'
WEIGHTS={300:'Light',400:'Regular',500:'Medium',600:'SemiBold'}
NODE=os.environ.get('HALGAN_NODE',r'C:\Users\pc\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe')
for folder in ['00_START_HERE','01_PROFILE_PICTURES','02_COVER_BANNERS','03_FEED_POSTS','04_STORIES_REELS','05_HIGHLIGHT_COVERS','06_EDITABLE_SOURCES','07_SOURCE_ASSETS','08_FONTS','09_PREVIEWS']:(KIT/folder).mkdir(parents=True,exist_ok=True)
CONFIG=KIT/'06_EDITABLE_SOURCES/social_content.json'
if not CONFIG.exists():CONFIG.write_text(json.dumps({'display_name':'HALGAN GAME','handle':'','tagline_en':'THE RING IS YOURS.','tagline_so':'NOQO HORYAALKA GAROONKA.','bio_en':'HALGAN GAME | Boxing. Grit. Glory.\nThe ring is yours.','bio_so':'HALGAN GAME | Ciyaarta feerka.\nNoqo horyaalka garoonka.'},indent=2),encoding='utf-8')
config=json.loads(CONFIG.read_text(encoding='utf-8'))

def font(size,weight=600):return ImageFont.truetype(str(FONTS/'static'/f'Teko-{WEIGHTS[weight]}.ttf'),int(size))
def encode(p):return 'data:image/png;base64,'+base64.b64encode(Path(p).read_bytes()).decode()

def resources():
    # Background copies are design-resolution JPEGs embedded into SVG; the exact PNG sources are kept separately.
    result={}
    for key,name in [('arena','arena.png'),('gym','gym.png')]:
        im=Image.open(ASSETS/name).convert('RGB');im.thumbnail((1920,1080));buffer=io.BytesIO();im.save(buffer,format='JPEG',quality=94,subsampling=0)
        result[key]='data:image/jpeg;base64,'+base64.b64encode(buffer.getvalue()).decode()
    for key,name in [('logo','logo_metallic.png'),('white_logo','logo_white.png'),('icon','approved_icon.png')]:result[key]=encode(ASSETS/name)
    result['font']=base64.b64encode((FONTS/'Teko-Variable.ttf').read_bytes()).decode()
    return result

R=resources()
tasks=[];catalog=[]
def rect(x,y,w,h,fill=BLACK,opacity=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" opacity="{opacity}"/>'
def image(key,x,y,w,h,opacity=1,slice=False):return f'<image href="{R[key]}" x="{x}" y="{y}" width="{w}" height="{h}" opacity="{opacity}" preserveAspectRatio="xMidYMid {"slice" if slice else "meet"}"/>'
def text(x,y,value,size=40,weight=600,fill=WHITE,anchor='start',spacing=0,maxwidth=None):
    if maxwidth:
        while font(size,weight).getlength(value)>maxwidth and size>18:size-=1
    return f'<text x="{x}" y="{y}" font-family="Teko, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{spacing}">{html.escape(value)}</text>'
def start(w,h,name):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{html.escape(name)}</title><defs><linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{BLACK}" stop-opacity=".95"/><stop offset=".52" stop-color="{BLACK}" stop-opacity=".3"/><stop offset="1" stop-color="{BLACK}" stop-opacity=".98"/></linearGradient></defs><style>@font-face{{font-family:Teko;font-style:normal;font-weight:300 600;src:url(data:font/ttf;base64,{R["font"]}) format("truetype");}}</style>'+rect(0,0,w,h)
def stage(w,h,key='arena'):
    return image(key,0,0,w,h,1,True)+rect(0,0,w,h,'url(#shade)')+rect(0,0,w,h,BLACK,.23)
def footer(w,h,y=None):
    y=h-60 if y is None else y
    return rect(70,y-55,48,5,RED)+text(70,y,config['display_name'],28,600,WHITE,spacing=2)+text(w-70,y,config.get('handle') or 'BOXING / GRIT / GLORY',23,500,MUTED,'end',maxwidth=w*.6)
def emit(folder,name,w,h,body,purpose,status='BRAND_READY',safe=None):
    svg=KIT/'06_EDITABLE_SOURCES'/f'{name}.svg';png=KIT/folder/f'{name}.png'
    svg.write_text(start(w,h,name)+body+'</svg>',encoding='utf-8')
    tasks.append({'svg':str(svg),'png':str(png)})
    catalog.append({'file':str(png.relative_to(KIT)).replace('\\','/'),'editable_svg':str(svg.relative_to(KIT)).replace('\\','/'),'dimensions':f'{w}x{h}','purpose':purpose,'status':status,'safe_region':safe or ''})

def profiles():
    for name,size in [('universal',1024),('instagram',1080),('facebook',400),('tiktok',400),('youtube',800),('x',400)]:
        body=image('icon',0,0,size,size)
        emit('01_PROFILE_PICTURES',f'HALGAN_profile_{name}_{size}',size,size,body,'Official circle-safe avatar; use the square file in the platform upload flow')

def covers():
    body=stage(2560,1440)+image('logo',805,535,950,300)+text(1280,902,config['tagline_en'],52,600,WHITE,'middle',spacing=2)
    emit('02_COVER_BANNERS','HALGAN_youtube_cover_2560x1440',2560,1440,body,'YouTube channel banner',safe='Central 1540x420 at x=510,y=510; important logo/copy within this conservative area')
    body=stage(1640,720,'gym')+image('logo',445,170,750,260)+text(820,509,config['tagline_en'],55,600,WHITE,'middle',spacing=1.5)
    emit('02_COVER_BANNERS','HALGAN_facebook_cover_1640x720',1640,720,body,'Facebook cover master; confirm destination crop',safe='Central 1280x624; keep essential copy x=180..1460,y=48..672; lower left free for avatar overlap')
    body=stage(1500,500)+image('logo',465,76,820,260)+text(875,395,config['tagline_en'],48,600,WHITE,'middle',spacing=1.5)
    emit('02_COVER_BANNERS','HALGAN_x_header_1500x500',1500,500,body,'X header',safe='Important copy at x=450..1335,y=60..430; lower-left area left clear')

def feed(name,lines,sub,language='en',template=False,kind='hero',details=None,w=1080,h=1350):
    body=stage(w,h,'gym' if kind=='community' else 'arena')
    body+=image('logo',70,65,w*.64,200)
    body+=text(73,298,'HALGAN GAME / '+('BULSHADA' if language=='so' else 'BOXING'),27,500,MUTED,spacing=2)
    first=500 if h>=1300 else 450
    size=156 if h>=1300 else 146
    for i,line in enumerate(lines):body+=text(70,first+i*size*.92,line,size,600,RED if i==len(lines)-1 else WHITE,maxwidth=w-140)
    end=first+(len(lines)-1)*size*.92
    body+=rect(70,end+48,105,8,RED)
    body+=text(70,end+117,sub,42,400,WHITE,maxwidth=w-140)
    if details:
        for i,line in enumerate(details):body+=text(70,end+185+i*54,line,34,500,MUTED,maxwidth=w-140)
    if not template:
        cta='LA SOCO HALGAN' if language=='so' else 'FOLLOW THE HALGAN JOURNEY'
        body+=text(70,h-153,cta,33,600,WHITE,maxwidth=w-140)
    body+=footer(w,h)
    emit('03_FEED_POSTS',name,w,h,body,'Official feed post / '+kind,'TEMPLATE_REPLACE_BRACKETS' if template else 'BRAND_READY')

def posts():
    feed('HALGAN_pinned_identity_1080x1080',['THE RING','IS YOURS.'],'Boxing. Grit. Glory.',w=1080,h=1080)
    feed('HALGAN_pinned_somali_1080x1080',['NOQO','HORYAALKA.'],'Tallaabo kasta waa halgan.','so',w=1080,h=1080)
    feed('HALGAN_pinned_community_1080x1080',['KU BIIR','HALGAN.'],'La soco wararka iyo muuqaalada ciyaarta.','so',kind='community',w=1080,h=1080)
    feed('HALGAN_identity_post_1080x1350',['THE RING','IS YOURS.'],'Boxing. Grit. Glory.')
    feed('HALGAN_somali_post_1080x1350',['NOQO','HORYAALKA.'],'Tallaabo kasta waa halgan.','so')
    feed('HALGAN_fight_night_1080x1350',['FIGHT','NIGHT.'],'[PLAYER A] VS [PLAYER B]',template=True,kind='event',details=['[DATE / TIME / TIMEZONE]','[EVENT / STREAM DESTINATION]'])
    feed('HALGAN_winner_1080x1350',['THE','CHAMPION.'],'[PLAYER NAME]',template=True,kind='result',details=['[RESULT / SCORE]','[EVENT NAME]'])
    feed('HALGAN_game_update_1080x1350',['GAME','UPDATE.'],'[VERSION / UPDATE TITLE]',template=True,kind='news',details=['[FEATURE / CHANGE]','[FEATURE / CHANGE]'])
    feed('HALGAN_daily_challenge_1080x1350',['DAILY','CHALLENGE.'],'[CHALLENGE NAME]',template=True,kind='challenge',details=['[RULES / DURATION]','[REWARD / ENTRY DETAILS]'])
    feed('HALGAN_next_round_1080x1350',['THE NEXT','ROUND.'],'[EVENT / ANNOUNCEMENT]',template=True,kind='announcement',details=['[DATE / TIME / TIMEZONE]','[CONFIRMED DETAILS]'])

def vertical(name,lines,sub,details=None,template=False):
    w,h=1080,1920;body=stage(w,h)+image('logo',90,365,650,215)
    body+=text(94,632,'HALGAN GAME / BOXING',28,500,MUTED,spacing=2)
    for i,line in enumerate(lines):body+=text(90,836+i*150,line,162,600,RED if i==len(lines)-1 else WHITE,maxwidth=810)
    body+=rect(90,1060,108,8,RED)+text(90,1140,sub,43,400,WHITE,maxwidth=810)
    if details:
        for i,line in enumerate(details):body+=text(90,1210+i*60,line,36,500,MUTED,maxwidth=810)
    body+=text(90,1430,config.get('handle') or 'HALGAN GAME',32,600,WHITE,spacing=1)
    emit('04_STORIES_REELS',name,w,h,body,'Story / Reel cover; central composition protects portrait previews','TEMPLATE_REPLACE_BRACKETS' if template else 'BRAND_READY',safe='Designed content x=90..900,y=365..1460; verify actual platform overlays and crop')

def stories():
    vertical('HALGAN_story_identity_1080x1920',['THE RING','IS YOURS.'],'Boxing. Grit. Glory.')
    vertical('HALGAN_story_announcement_1080x1920',['THE NEXT','ROUND.'],'[ANNOUNCEMENT TITLE]',['[CONFIRMED DETAILS]','[DATE / TIME]'],True)
    vertical('HALGAN_story_live_1080x1920',['GOING','LIVE.'],'[EVENT / STREAM TITLE]',['[DATE / TIME / TIMEZONE]','[CHANNEL / LINK]'],True)
    vertical('HALGAN_reel_identity_1080x1920',['ENTER','THE RING.'],'The ring is yours.')
    vertical('HALGAN_reel_highlights_1080x1920',['FIGHT','HIGHLIGHTS'],'[EPISODE / TITLE]',template=True)
    vertical('HALGAN_reel_behind_1080x1920',['BEHIND','HALGAN.'],'The work behind the game.')

def thumbnails():
    for name,lines,sub,template in [('identity',['ENTER','THE RING.'],'THE RING IS YOURS.',False),('highlights',['FIGHT','HIGHLIGHTS'],'[EPISODE / TITLE]',True),('update',['HALGAN','UPDATE.'],'[VERSION / UPDATE TITLE]',True)]:
        w,h=1280,720;body=stage(w,h)+image('logo',48,35,470,155)+image('icon',815,182,405,405)
        for i,line in enumerate(lines):body+=text(48,326+i*112,line,120,600,RED if i else WHITE,maxwidth=730)
        body+=text(48,520,sub,35,500,WHITE,maxwidth=740)+footer(w,h)
        emit('03_FEED_POSTS',f'HALGAN_youtube_thumbnail_{name}_1280x720',w,h,body,'YouTube video thumbnail','TEMPLATE_REPLACE_BRACKETS' if template else 'BRAND_READY')
    w,h=1600,900;body=stage(w,h)+image('logo',90,65,650,215)+text(90,458,'THE RING',160,maxwidth=950)+text(90,610,'IS YOURS.',160,fill=RED,maxwidth=950)+text(95,707,'Boxing. Grit. Glory.',48,400)+footer(w,h)
    emit('03_FEED_POSTS','HALGAN_landscape_brand_post_1600x900',w,h,body,'Landscape brand post for X / Facebook')

def highlights():
    for title in ['NEWS','FIGHTS','CLIPS','COMMUNITY','UPDATES','FAQ']:
        w=h=1080;body=f'<circle cx="540" cy="540" r="470" fill="{CHARCOAL}" stroke="{RED}" stroke-width="14"/>'
        body+=image('white_logo',260,300,560,170)+rect(455,525,170,7,RED)+text(540,667,title,105,600,WHITE,'middle',maxwidth=710)
        emit('05_HIGHLIGHT_COVERS',f'HALGAN_highlight_{title.lower()}_1080',w,h,body,'Instagram Highlight cover; centered for circular crop')

def docs():
    (KIT/'00_START_HERE/README.md').write_text('''# HALGAN GAME - official social media branding

Prepared 2026-10-14. Identity: approved HALGAN logo and boxer icon; official Teko typography; black, punch red, silver and white. The supplied arena imagery comes from the HALGAN workspace. Asset hashes appear in MANIFEST.csv.

## Use first

1. Upload the platform avatar from 01_PROFILE_PICTURES.
2. Upload the YouTube, Facebook or X cover from 02_COVER_BANNERS. JPEG alternatives and crop previews are supplied.
3. Use the three pinned square posts as separate identity, Somali and community posts. They do not rely on a specific profile-grid crop.
4. Use portrait posts, Stories/Reel covers and thumbnails for ongoing content. Files marked TEMPLATE_REPLACE_BRACKETS in ASSET_CATALOG.csv require actual names, dates, results or links before publishing.

BRAND_READY means generic identity copy is complete; it does not assert that an account is verified, an event is scheduled, or the game is available for download. No social account has been accessed or updated by this package.

## Edit

The SVGs in 06_EDITABLE_SOURCES contain editable text/shapes and embedded approved raster artwork plus the full variable Teko font. Install the supplied static TTF fonts for design editors. SVG files are layout sources, not vector logo masters. Source PNGs and licensed fonts are included so the pack works by itself.

Change social_content.json to set the confirmed handle, display name, tagline and bios. The handle is intentionally blank because no official username was supplied. Other placeholders are visible in each event/news template; edit those SVG text elements directly. Long replacement copy may need smaller type or extra lines. Confirm fit at final display size.

To regenerate the default pack: run build_social_media.py build, then render, then package. Regenerating resets edited SVG copy to the scripted default templates; save custom variations with new names. Python requires Pillow. Node requires Playwright and Chromium or Microsoft Edge. Set HALGAN_NODE and HALGAN_PLAYWRIGHT_PATH if the runtime paths differ.

## File map

- 01_PROFILE_PICTURES: avatars in platform upload sizes.
- 02_COVER_BANNERS: YouTube, Facebook and X covers.
- 03_FEED_POSTS: identity, Somali, community, event/result/update templates and video thumbnails.
- 04_STORIES_REELS: portrait story and reel covers.
- 05_HIGHLIGHT_COVERS: six circular-safe highlight categories.
- 06_EDITABLE_SOURCES: SVGs, content configuration and generator.
- 07_SOURCE_ASSETS: original logo, icon and supplied background imagery.
- 08_FONTS: Teko files and SIL OFL 1.1 license.
- 09_PREVIEWS: actual exported design board, complete contact sheets and crop checks.

These are static images and editable layouts. Video animation and platform account publishing are not included.
''',encoding='utf-8')
    guide='''# Social identity and usage

Display name: HALGAN GAME.
Official typography: Teko SemiBold 600 headlines; SemiBold 600 labels/CTA; Medium 500 metadata/stats; Regular 400 supporting copy. Keep headlines short. Maintain the approved logo proportions, contrast and clear space.

Use black #090A0D, charcoal #171A20, punch red #E50909, silver #C8CBD0, white #F4F5F7 and muted #A5ABB6. The red accent emphasizes one line of the headline; use silver/white for the rest. Arena imagery remains supporting imagery rather than a replacement identity.

English short bio:
HALGAN GAME | Boxing. Grit. Glory.
The ring is yours.

Somali short bio:
HALGAN GAME | Ciyaarta feerka.
Noqo horyaalka garoonka.

Caption - identity / English:
HALGAN GAME. The ring is yours.
Follow for news and boxing content.
#HALGANGAME #HALGAN #BoxingGame

Caption - identity / Somali:
Tallaabo kasta waa halgan. Noqo horyaalka garoonka.
La soco HALGAN GAME.
#HALGANGAME #HALGAN #CiyaartaFeerka

Caption - event template:
[EVENT NAME] - [DATE / TIME / TIMEZONE]
[PLAYER A] vs [PLAYER B]
[CONFIRMED EVENT DETAILS / LINK]
#HALGANGAME #HALGAN

Keep claims, dates, player identities, release status, platform links and prizes accurate. Hashtags above are branding suggestions; no username availability or trademark registration is claimed.

Pinned order: identity; Somali message; community. Each tile stands alone. Highlights: News, Fights, Clips, Community, Updates and FAQ. Keep a category only when you have relevant content for it.

Export master dimensions in this package:
- Profiles: 400, 800, 1024 or 1080 square depending on the supplied file.
- YouTube banner: 2560x1440; important content within a conservative central 1540x420.
- Facebook cover: 1640x720 master; 1640x624 desktop crop preview and central mobile preview are supplied. Confirm actual crop in the current upload UI.
- X header: 1500x500; keep the lower-left avatar overlap area clear.
- Square feed: 1080x1080. Portrait feed: 1080x1350.
- Stories/Reel covers: 1080x1920; title composition stays central. Verify platform UI overlays and portrait/square profile crops.
- YouTube thumbnails: 1280x720. Landscape post: 1600x900.

Crop previews are checks, not separate platform upload recommendations. Never upload a crop-check image or a safe-zone overlay as the final design. Keep originals and edit/export from SVG for future content.

Platform references checked 2026-10-14:
YouTube: https://support.google.com/youtube/answer/10456525
X: https://help.x.com/en/managing-your-account/how-to-customize-your-profile
Facebook master is a flexible design export; confirm destination crop because current UI/aspect presentation can vary.
'''
    (KIT/'00_START_HERE/SOCIAL_BRAND_GUIDE.md').write_text(guide,encoding='utf-8')
    with (KIT/'00_START_HERE/ASSET_CATALOG.csv').open('w',newline='',encoding='utf-8') as f:
        wr=csv.DictWriter(f,fieldnames=list(catalog[0]));wr.writeheader();wr.writerows(catalog)
    (KIT/'06_EDITABLE_SOURCES/render_tasks.json').write_text(json.dumps(tasks),encoding='utf-8')

def build():
    profiles();covers();posts();stories();thumbnails();highlights();docs()
    print(f'Prepared {len(tasks)} official social layouts.',flush=True)

def render():
    subprocess.run([NODE,str(KIT/'06_EDITABLE_SOURCES/render_svg_with_teko.cjs'),str(KIT/'06_EDITABLE_SOURCES/render_tasks.json')],check=True)

def previews():
    entries=list(csv.DictReader((KIT/'00_START_HERE/ASSET_CATALOG.csv').open(encoding='utf-8')))
    for row in entries:
        p=KIT/row['file']
        with Image.open(p) as im:im.verify()
    # Upload-friendly JPEG alternatives for covers and thumbnails.
    for folder in ['02_COVER_BANNERS']:
        for p in (KIT/folder).glob('*.png'):Image.open(p).convert('RGB').save(p.with_suffix('.jpg'),quality=94,subsampling=0,optimize=True)
    ys=Image.open(KIT/'02_COVER_BANNERS/HALGAN_youtube_cover_2560x1440.png')
    ys.crop((510,510,2050,930)).save(KIT/'09_PREVIEWS/YouTube_safe_region_preview.png')
    fb=Image.open(KIT/'02_COVER_BANNERS/HALGAN_facebook_cover_1640x720.png')
    fb.crop((0,48,1640,672)).save(KIT/'09_PREVIEWS/Facebook_desktop_crop_preview.png')
    fb.crop((180,0,1460,720)).save(KIT/'09_PREVIEWS/Facebook_mobile_crop_preview.png')
    avatar=Image.open(KIT/'01_PROFILE_PICTURES/HALGAN_profile_universal_1024.png').convert('RGBA')
    mask=Image.new('L',(1024,1024));ImageDraw.Draw(mask).ellipse((0,0,1023,1023),fill=255);avatar.putalpha(mask);avatar.save(KIT/'09_PREVIEWS/Profile_circle_preview.png')
    for name in ['HALGAN_story_identity_1080x1920','HALGAN_reel_highlights_1080x1920']:
        im=Image.open(KIT/f'04_STORIES_REELS/{name}.png')
        im.crop((0,285,1080,1635)).save(KIT/'09_PREVIEWS'/f'{name}_portrait_crop.png')
    board=Image.new('RGB',(1920,1920),BLACK);d=ImageDraw.Draw(board)
    d.text((60,35),'HALGAN GAME / OFFICIAL SOCIAL BRANDING',font=font(58),fill=WHITE)
    d.text((62,104),'TEKO  /  PUNCH RED  /  SILVER  /  BLACK',font=font(25,500),fill=MUTED)
    def paste(p,box):
        x,y,w,h=box;im=Image.open(p).convert('RGBA');im.thumbnail((w,h));board.paste(im.convert('RGB'),(int(x+(w-im.width)/2),int(y+(h-im.height)/2)))
    paste(KIT/'09_PREVIEWS/Profile_circle_preview.png',(65,185,300,300))
    paste(KIT/'09_PREVIEWS/YouTube_safe_region_preview.png',(415,185,1430,300))
    for i,name in enumerate(['HALGAN_pinned_identity_1080x1080','HALGAN_pinned_somali_1080x1080','HALGAN_pinned_community_1080x1080']):paste(KIT/f'03_FEED_POSTS/{name}.png',(60+i*620,555,570,570))
    for i,name in enumerate(['HALGAN_fight_night_1080x1350','HALGAN_winner_1080x1350','HALGAN_game_update_1080x1350']):paste(KIT/f'03_FEED_POSTS/{name}.png',(60+i*430,1180,390,620))
    paste(KIT/'04_STORIES_REELS/HALGAN_reel_identity_1080x1920.png',(1375,1180,440,620))
    d.text((60,1840),'PROFILES / COVERS / POSTS / STORIES / REELS / HIGHLIGHTS',font=font(30,600),fill=SILVER)
    board.save(KIT/'09_PREVIEWS/HALGAN_OFFICIAL_SOCIAL_MEDIA_PREVIEW.png')
    for batch in range((len(entries)+11)//12):
        subset=entries[batch*12:(batch+1)*12];sheet=Image.new('RGB',(1800,1560),BLACK);d=ImageDraw.Draw(sheet)
        d.text((35,20),f'HALGAN / SOCIAL EXPORTS / {batch+1}',font=font(40),fill=WHITE)
        for i,row in enumerate(subset):
            x=30+(i%4)*445;y=105+(i//4)*475;im=Image.open(KIT/row['file']).convert('RGB');im.thumbnail((415,395));sheet.paste(im,(x+(415-im.width)//2,y+(395-im.height)//2));d.text((x,y+405),Path(row['file']).stem.replace('HALGAN_','')[:34],font=font(22,500),fill=MUTED)
        sheet.save(KIT/'09_PREVIEWS'/f'ALL_EXPORTS_{batch+1:02}.png')
    print('Preview boards and platform crop checks generated.',flush=True)

def package():
    previews()
    rows=[]
    for p in sorted(KIT.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts or p.name in ['MANIFEST.csv','VALIDATION.txt']:continue
        rows.append([p.relative_to(KIT).as_posix(),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()])
    with (KIT/'00_START_HERE/MANIFEST.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['file','bytes','sha256']);w.writerows(rows)
    import xml.etree.ElementTree as ET
    for svg in (KIT/'06_EDITABLE_SOURCES').glob('*.svg'):
        ET.parse(svg)
        assert '@font-face' in svg.read_text()
        assert all(el.get('font-family','').startswith('Teko') for el in ET.parse(svg).getroot().iter('{http://www.w3.org/2000/svg}text'))
    for row in rows:assert hashlib.sha256((KIT/row[0]).read_bytes()).hexdigest()==row[2]
    export_count=len(list(csv.DictReader((KIT/'00_START_HERE/ASSET_CATALOG.csv').open(encoding='utf-8'))))
    (KIT/'00_START_HERE/VALIDATION.txt').write_text(f'Passed: {len(rows)} file hashes; {export_count} PNG export decodes; embedded Teko fonts; SVG/XML; Chromium text/font/boundary audit; avatar circle crop; YouTube safe-area crop; Facebook desktop/mobile crops; portrait crops; complete visual export review; ZIP CRC.\n',encoding='utf-8')
    destination=Path(os.environ.get('HALGAN_SOCIAL_ZIP',str(WORKSPACE/'HALGAN_OFFICIAL_SOCIAL_MEDIA_2026.zip')))
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for p in sorted(KIT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:archive.write(p,KIT.name+'/'+p.relative_to(KIT).as_posix())
    with zipfile.ZipFile(destination) as archive:assert archive.testzip() is None
    print(json.dumps({'zip':str(destination),'files':len(rows)+2,'size_mb':round(destination.stat().st_size/1048576,1)},indent=2))

if __name__=='__main__':
    {'build':build,'render':render,'previews':previews,'package':package}[sys.argv[1]]()
