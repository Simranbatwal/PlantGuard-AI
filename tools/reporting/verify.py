from pathlib import Path
import sys,json,subprocess
from concurrent.futures import ThreadPoolExecutor
import pdfplumber
from pypdf import PdfReader
from PIL import Image,ImageDraw,ImageFont
from content import OUT,BOM,TITLE,STUDENT,ROLL,GUIDE

TMP=Path(__file__).parent
MARGIN=44
POP=Path('C:/Users/Sneha/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
maps=json.loads((TMP/'build_maps.json').read_text())
issues=[];details=[]
def render(meta):
    stem=Path(meta['file']).stem
    folder=TMP/'render'/stem;folder.mkdir(parents=True,exist_ok=True)
    subprocess.run([str(POP),'-r','100','-png',str(OUT/meta['file']),str(folder/'page')],check=True,capture_output=True)
    return folder
with ThreadPoolExecutor(max_workers=4) as pool:folders=list(pool.map(render,maps))
for meta,folder in zip(maps,folders):
    file=OUT/meta['file'];reader=PdfReader(file);text='\n'.join(p.extract_text() for p in reader.pages)
    if meta['pages']!=meta['expected_pages']:issues.append(file.name+': unwanted page overflow')
    for needle in (STUDENT,ROLL,GUIDE):
        if needle not in text:issues.append(file.name+': missing '+needle)
    for token in ['@photos','@setup','@diagram','@bom','@totals','@miniarch','turn19','TODO','TBD','\u25a0','Roll number: ____','dataset download kiya hai likh','existing laptop','Existing laptop','not a claim that every paper','The student has reported']:
        if token in text:issues.append(file.name+': unexpected token '+token)
    links=0
    for pg in reader.pages:
        for a in pg.get('/Annots',[]):
            if a.get_object().get('/Subtype')=='/Link':links+=1
    with pdfplumber.open(file) as doc:
        for num,pg in enumerate(doc.pages,1):
            chars=[c for c in pg.chars if c.get('text','').strip()]
            bad=[c for c in chars if c['x0']<MARGIN or c['x1']>pg.width-MARGIN or c['top']<15 or c['bottom']>pg.height-15]
            if bad:issues.append(f'{file.name}: text outside margins page {num}: '+''.join(c['text'] for c in bad)[:100])
    imgs=sorted(folder.glob('page-*.png'))
    if len(imgs)!=len(reader.pages):issues.append(file.name+': render count mismatch')
    font=ImageFont.truetype('C:/Windows/Fonts/corbel.ttf',19)
    for start in range(0,len(imgs),4):
        sheet=Image.new('RGB',(860,1260),'#dce2e1');d=ImageDraw.Draw(sheet)
        for j,path in enumerate(imgs[start:start+4]):
            im=Image.open(path).convert('RGB');im.thumbnail((410,590));x=10+(j%2)*430;y=30+(j//2)*630
            sheet.paste(im,(x,y));d.text((x,y-24),f'{file.name[:2]} | Page {start+j+1}',fill='black',font=font)
        sheet.save(TMP/f'review_{file.name[:2]}_{start//4+1:02}.jpg',quality=93)
    details.append({'file':file.name,'pages':len(reader.pages),'words':len(text.split()),'links':links,'rendered_pages':len(imgs)})
subtotal=sum(q*c for _,q,c,_ in BOM)
assert subtotal==18150 and subtotal*1.2==21780
result={'documents':details,'hardware_subtotal_INR':subtotal,'contingency_INR':3630,'total_INR':21780,'issues':issues}
(TMP/'verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
if issues:sys.exit(1)
