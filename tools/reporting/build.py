from pathlib import Path
import sys,re,html,json,shutil,math
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image,PageBreak,Flowable
from PIL import Image as PILImage
from pypdf import PdfReader
from content import *

TMP=Path(__file__).parent
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'assets').mkdir(exist_ok=True)
for filename in ['PlantGuard_Logo.png','esp32.jpg','soil.jpg','sht31.jpg','leaf.jpg','bh1750.jpg','enclosure.jpg']:
    shutil.copy2(MASTER/'assets'/filename,OUT/'assets'/filename)
PHOTOS={r['id']:r for r in json.loads((MASTER/'Photo_Sources.json').read_text())}
SELECTED=['esp32','soil','sht31','leaf','bh1750','enclosure']
(OUT/'Photo_Sources.json').write_text(json.dumps([PHOTOS[k] for k in SELECTED],indent=2),encoding='utf-8')

FONTDIR=Path('C:/Windows/Fonts')
for n,f in [('Text','constan.ttf'),('Text-Bold','constanb.ttf'),('Text-Italic','constani.ttf'),('Text-BoldItalic','constanz.ttf'),('Label','corbel.ttf'),('Label-Bold','corbelb.ttf'),('Display','BASKVILL.TTF')]:
    pdfmetrics.registerFont(TTFont(n,str(FONTDIR/f)))
pdfmetrics.registerFontFamily('Text',normal='Text',bold='Text-Bold',italic='Text-Italic',boldItalic='Text-BoldItalic')
pdfmetrics.registerFontFamily('Label',normal='Label',bold='Label-Bold',italic='Label',boldItalic='Label-Bold')
W,H=A4;M=50;CW=W-2*M
GREEN=colors.HexColor('#126447');NAVY=colors.HexColor('#183344');GRAY=colors.HexColor('#59636A');PALE=colors.HexColor('#F3F5F6');INK=colors.HexColor('#191C1D')
S={
 'body':ParagraphStyle('body',fontName='Text',fontSize=11,leading=15.2,spaceAfter=9,textColor=INK),
 'small':ParagraphStyle('small',fontName='Label',fontSize=9.4,leading=12.3,spaceAfter=8,textColor=GRAY),
 'heading':ParagraphStyle('heading',fontName='Display',fontSize=25,leading=28,spaceAfter=18,textColor=colors.black,keepWithNext=True),
 'sub':ParagraphStyle('sub',fontName='Text-Bold',fontSize=12,leading=16,spaceBefore=5,spaceAfter=8,textColor=colors.black,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='Display',fontSize=35,leading=39,spaceAfter=17,textColor=colors.black),
 'project':ParagraphStyle('project',fontName='Text',fontSize=17,leading=24,spaceAfter=18,textColor=colors.black),
 'meta':ParagraphStyle('meta',fontName='Label',fontSize=12,leading=17,spaceAfter=8,textColor=INK),
 'cell':ParagraphStyle('cell',fontName='Label',fontSize=10.2,leading=13.2,spaceAfter=0,textColor=INK),
 'thead':ParagraphStyle('thead',fontName='Label-Bold',fontSize=10.2,leading=13.2,spaceAfter=0,textColor=colors.white),
 'caption':ParagraphStyle('caption',fontName='Label',fontSize=8.8,leading=11.2,spaceAfter=7,textColor=GRAY,alignment=1),
 'summary':ParagraphStyle('summary',fontName='Text',fontSize=10.5,leading=13.8,spaceAfter=7,textColor=INK),
}
source_map={key:url for key,_,url in SOURCES}
source_map.update({key:url for key,_,url in TECH_SOURCES})

def identity(t):
    return (t.replace('Roll number: ____________________',f'Roll number: {ROLL}')
            .replace('Roll no.: ____________________',f'Roll no.: {ROLL}')
            .replace('Guide name / signature: ___________________________________________',f'Guide: {GUIDE}    Signature: ____________________')
            .replace('Guide: ____________________',f'Guide: {GUIDE}')
            .replace('Guide / review date: ____________________',f'Guide: {GUIDE} | Review date: __________')
            .replace('Roll number aur guide name ke blank fields fill karo.',f'Naam, roll number {ROLL} aur guide {GUIDE} ki details check karo.'))

def rich(t):
    t=identity(t).replace('–','-').replace('—','-').replace('‑','-').replace('₹','INR ')
    t=html.escape(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<link href="\2" color="#126447">\1</link>',t)
    t=re.sub(r'\[((?:[RDHT]\d+)(?:, [RDHT]\d+)*)\]',lambda m:'['+', '.join('<link href="'+source_map.get(x,'')+'" color="#126447">'+x+'</link>' for x in m[1].split(', '))+']',t)
    return t
def p(t,style='body'):return Paragraph(rich(str(t)),S[style])
def pic(path,h,w=CW):
    with PILImage.open(path) as im:iw,ih=im.size
    scale=min(w/iw,h/ih)
    im=Image(str(path),width=iw*scale,height=ih*scale);im.hAlign='CENTER';return im

class Mark(Flowable):
    def __init__(self,title):super().__init__();self.title=title;self.height=0;self.width=0
    def draw(self):
        c=self.canv;key='section'+str(len(c.section_pages))
        c.bookmarkPage(key);c.addOutlineEntry(self.title,key,0,False)
        c.section_pages.append((self.title,c.getPageNumber()))

class PageCanvas(canvas.Canvas):
    def __init__(self,*a,**k):super().__init__(*a,**k);self.section_pages=[]

def table(rows,widths=None):
    n=len(rows[0]);
    if widths is None:
        widths={2:[.36,.64],3:[.24,.39,.37],4:[.24,.28,.25,.23]}.get(n,[1/n]*n)
    widths=[v*CW for v in widths]
    data=[[p(c,'thead' if i==0 else 'cell') for c in row] for i,row in enumerate(rows)]
    ob=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    cmds=[('BACKGROUND',(0,0),(-1,0),NAVY),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#D7DDE0')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]
    for i in range(1,len(rows)):
        if i%2==0:cmds.append(('BACKGROUND',(0,i),(-1,i),PALE))
    ob.setStyle(TableStyle(cmds));return ob

def photo_table(ids):
    labels={'esp32':'ESP32 DevKitC family','soil':'Capacitive soil probe','sht31':'SHT31 air sensor','leaf':'Artificial wetness plate','bh1750':'BH1750 - optional','enclosure':'Prototype enclosure'}
    data=[]
    for i in range(0,len(ids),3):
        row=[]
        for key in ids[i:i+3]:
            row.append([pic(OUT/'assets'/f'{key}.jpg',93,CW/3-18),Spacer(1,6),p(labels[key],'caption'),p(f'[Source / product reference]({PHOTOS[key]["page"]})','caption')])
        data.append(row)
    t=Table(data,colWidths=[CW/3]*3)
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'BOTTOM'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),12)]))
    return t

class Architecture(Flowable):
    def __init__(self,mini=False):super().__init__();self.width=CW;self.height=65 if mini else 185;self.mini=mini
    def draw(self):
        c=self.canv
        def box(x,y,w,h,lines):
            c.setFillColor(PALE);c.setStrokeColor(colors.HexColor('#B4C5BD'));c.roundRect(x,y,w,h,4,fill=1,stroke=1)
            for i,l in enumerate(lines):
                c.setFillColor(INK);c.setFont('Label-Bold' if i==0 else 'Label',10 if i==0 else 9)
                c.drawCentredString(x+w/2,y+h/2+(len(lines)-1)*6-i*12-3,l)
        def arrow(x,y,xx,yy):
            c.setStrokeColor(GREEN);c.setFillColor(GREEN);c.setLineWidth(1.4);c.line(x,y,xx,yy)
            a=math.atan2(yy-y,xx-x);q=c.beginPath();q.moveTo(xx,yy);q.lineTo(xx-6*math.cos(a-.5),yy-6*math.sin(a-.5));q.lineTo(xx-6*math.cos(a+.5),yy-6*math.sin(a+.5));q.close();c.drawPath(q,fill=1,stroke=0)
        if self.mini:
            box(0,13,136,45,['Sensors + ESP32','Two wireless nodes']);box(181,13,136,45,['Local Wi-Fi','Image linked by zone']);box(362,13,CW-362,45,['Laptop','AI + data + dashboard']);arrow(136,35,181,35);arrow(317,35,362,35)
            return
        box(0,124,137,55,['Node A and Node B','Sensors + ESP32','Read and transmit'])
        box(179,124,137,55,['Local Wi-Fi','Existing access point','Wireless telemetry'])
        box(358,124,CW-358,55,['Laptop service','Broker + database','Validate and store'])
        arrow(137,151,179,151);arrow(316,151,358,151)
        box(0,24,137,55,['Phone / USB camera','Close-up leaf image','Plant + time + zone'])
        box(179,12,CW-179,79,['Laptop AI and dashboard','Image result + relevant environmental history','Quality checks, uncertainty and reviewed next action'])
        arrow(137,51,179,51);arrow(426,124,426,91)

class Setup(Flowable):
    def __init__(self):super().__init__();self.width=CW;self.height=220
    def draw(self):
        c=self.canv
        for x,zone in [(64,'Zone A'),(249,'Zone B')]:
            c.setFillColor(colors.HexColor('#B56F49'));q=c.beginPath();q.moveTo(x-38,51);q.lineTo(x+38,51);q.lineTo(x+29,5);q.lineTo(x-29,5);q.close();c.drawPath(q,fill=1,stroke=0)
            c.setFillColor(colors.HexColor('#493D2D'));c.ellipse(x-38,45,x+38,57,fill=1,stroke=0)
            c.setStrokeColor(GREEN);c.setLineWidth(3);c.line(x,53,x,160)
            for off,y,angle in [(-22,85,-30),(20,113,28),(-18,136,-20),(17,155,25)]:
                c.line(x,y-5,x+off,y+9);c.saveState();c.translate(x+off,y+10);c.rotate(angle);c.setFillColor(colors.HexColor('#56915C'));c.ellipse(-17,-7,17,7,fill=1,stroke=0);c.restoreState()
            c.setFillColor(NAVY);c.rect(x-23,28,6,38,fill=1,stroke=0)
            c.setStrokeColor(GRAY);c.setLineWidth(1.2);c.line(x+50,7,x+50,129)
            c.setFillColor(PALE);c.setStrokeColor(GRAY);c.roundRect(x+38,96,24,31,3,fill=1,stroke=1)
            c.setFillColor(GREEN);c.rect(x+41,144,24,13,fill=1,stroke=0);c.line(x+53,144,x+53,129)
            c.setFillColor(PALE);c.roundRect(x+77,15,57,38,4,fill=1,stroke=1)
            c.setFillColor(INK);c.setFont('Label-Bold',9);c.drawCentredString(x+105,37,'ESP32');c.setFont('Label',8);c.drawCentredString(x+105,24,zone)
            c.setStrokeColor(GRAY);c.line(x-20,65,x+83,53);c.line(x+49,97,x+92,53)
            c.setFillColor(INK);c.setFont('Label-Bold',11);c.drawCentredString(x,183,zone)
        c.setFillColor(GRAY);c.setFont('Label',9)
        c.drawString(14,204,'Two labelled pots with matched sensing hardware')
        # Explicit legend avoids implying precise sensor dimensions or electrical connections.
        c.setFillColor(NAVY);c.rect(390,147,7,14,fill=1,stroke=0);c.setFillColor(INK);c.drawString(403,151,'Soil probe')
        c.setFillColor(PALE);c.roundRect(388,116,12,16,2,fill=1,stroke=1);c.setFillColor(INK);c.drawString(403,120,'Air shield')
        c.setFillColor(GREEN);c.rect(388,90,12,7,fill=1,stroke=0);c.setFillColor(INK);c.drawString(403,90,'Wetness plate')
        c.setFont('Label',9);c.drawString(388,65,'Shared camera');c.drawString(388,51,'on a stable stand');c.drawString(388,24,'Laptop via Wi-Fi')

def bom_table(start,end):
    rows=[['Item / configuration','Qty','Unit INR','Total INR']]
    for name,q,c,note in BOM[start:end]:
        if note not in ('Core',):name+=' ('+note.lower()+')'
        rows.append([name,str(q),f'{c:,}',f'{q*c:,}'])
    return table(rows,[.60,.08,.16,.16])

def parse(text,summary=False):
    out=[];ls=text.splitlines();i=0
    while i<len(ls):
        l=ls[i].strip()
        if not l:i+=1;continue
        if l.startswith('@photos '):out += [photo_table(l.split()[1:]),Spacer(1,4)]
        elif l.startswith('@diagram'):out += [Architecture(),Spacer(1,7)]
        elif l=='@miniarch':out += [Architecture(True),Spacer(1,5)]
        elif l=='@setup':out += [Setup(),Spacer(1,6)]
        elif l.startswith('@bom '):a,b=map(int,l.split()[1:]);out += [bom_table(a,b),Spacer(1,13)]
        elif l=='@totals':out += [table([['Budget summary','INR'],['Physical-parts subtotal','18,150'],['20% procurement contingency','3,630'],['Requested planning ceiling','21,780']],[.76,.24]),Spacer(1,11)]
        elif l.startswith('|'):
            rows=[]
            while i<len(ls) and ls[i].strip().startswith('|'):
                row=[x.strip() for x in ls[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',x) for x in row):rows.append(row)
                i+=1
            out += [table(rows),Spacer(1,11)];continue
        elif l.startswith('## '):out.append(p(l[3:],'sub'))
        else:
            para=l
            while i+1<len(ls) and ls[i+1].strip() and not ls[i+1].startswith(('#','@','|')) and not re.match(r'\d+\.',ls[i+1]):
                i+=1;para+=' '+ls[i].strip()
            sty='small' if para.startswith('Figure ') else ('summary' if summary else 'body')
            out.append(p(para,sty))
        i+=1
    return out

def furniture(c,doc):
    c.saveState();c.setFillColor(GRAY);c.setFont('Label',9)
    if doc.page>1 or doc.kind=='summary':
        c.drawString(M,H-32,'PLANTGUARD  /  '+doc.short.upper())
        c.drawRightString(W-M,H-32,'SIMRAN BATWAL')
    c.setFont('Label',8.5);c.drawString(M,28,DATE+'  |  Initial-stage proposal')
    c.drawRightString(W-M,28,f'{doc.page:02d}')
    c.restoreState()

def cover(kind):
    labels={'report':('College Prototype','Initial project report for guide review'),
            'fund':('Hardware Funding','Procurement and financial-support proposal'),
            'hand':('Guide Meeting','Preparation and viva handbook in Hinglish')}
    title,sub=labels[kind]
    out=[Spacer(1,3),p(INSTITUTE,'meta'),p('Computer Science | M.Tech | 3rd Semester','small'),Spacer(1,5),pic(OUT/'assets/PlantGuard_Logo.png',175,360),Spacer(1,11),p(title,'title'),p(sub,'sub'),Spacer(1,10),p(TITLE,'project'),Spacer(1,20),p('Prepared by','small'),p(f'**{STUDENT}**  |  Roll number: {ROLL}','meta'),p(f'Under the guidance of **{GUIDE}**','meta'),Spacer(1,17),p('Review edition | '+DATE,'small')]
    notes={'report':'Proposed architecture, literature briefs, research methodology and milestone plan. Prepared before implementation and experimental validation.',
           'fund':'Physical-parts estimate: INR 18,150. Requested ceiling with a 20% contingency: INR 21,780. Actual procurement subject to quotations and institutional approval.',
           'hand':'Simple explanations, a meeting script, 32 likely questions, paper-reading guidance and an action record. Use this handbook for preparation; submit the formal report to the guide.'}
    out += [p(notes[kind],'body')]
    return out

def source_pages():
    a=[]
    for title,items in [('References: research literature',SOURCES[:8]),('References: data and hardware',SOURCES[8:])]:
        text=''
        for key,desc,url in items:text+=f'**{key}.** {desc} [Open primary source]({url})\n\n'
        text+='These sources support the proposed design and literature notes. I will continue the detailed study of their methods during the next phase.'
        a.append((title,text))
    return a

def build(kind,name,sections):
    path=OUT/name
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=M,leftMargin=M,topMargin=58,bottomMargin=48,title=TITLE+' | '+kind,author=STUDENT,subject='PlantGuard initial-stage college review',pageCompression=1)
    doc.kind=kind;doc.short={'report':'College prototype report','fund':'Hardware funding proposal','hand':'Guide preparation','summary':'Guide review summary'}[kind]
    flow=[];expected=[]
    if kind!='summary':
        flow+=cover(kind)+[PageBreak()];expected.append(('Cover',1))
    if kind in ('report','hand'):
        capacity=25
        count=math.ceil(len(sections)/capacity)
        for chunk in range(count):
            title='Contents' if chunk==0 else 'Contents continued'
            flow+=[Mark(title),p(title,'heading')]
            rows=[['Section','Page']]
            for idx,(stitle,_) in enumerate(sections[chunk*capacity:(chunk+1)*capacity],chunk*capacity):
                rows.append([stitle,str(2+count+idx)])
            flow += [table(rows,[.88,.12]),PageBreak()]
            expected.append((title,len(expected)+1))
    for idx,(title,body) in enumerate(sections):
        if idx:flow.append(PageBreak())
        flow+=[Mark(title),p(title,'heading')]+parse(body,summary=kind=='summary')
        expected.append((title,len(expected)+1))
    doc.build(flow,onFirstPage=furniture,onLaterPages=furniture,canvasmaker=PageCanvas)
    actual=doc.canv.section_pages
    pages=len(PdfReader(path).pages)
    state={'file':name,'pages':pages,'expected_pages':len(expected),'sections':actual}
    (TMP/(path.stem+'_map.json')).write_text(json.dumps(state,indent=2))
    md=f'# {TITLE}\n\nSystem: PlantGuard\n\n{STUDENT} | Roll number: {ROLL}\n\n{DETAILS}\n\n{INSTITUTE}\n\nGuide: {GUIDE}\n\n{DATE} | Initial-stage proposal\n\n'
    for title,body in sections:
        md+='\n# '+title+'\n\n'+identity(body)+'\n'
    # Render directives into meaningful editable Markdown references.
    md=md.replace('@diagram college','**Architecture:** sensors -> ESP32 nodes A/B -> local Wi-Fi -> laptop broker/database -> laptop AI/dashboard. Camera -> zone/time-linked image intake on laptop.')
    md=md.replace('@miniarch','**Flow:** two sensing nodes -> local Wi-Fi -> laptop AI, database and dashboard.')
    md=md.replace('@setup','**Setup:** two labelled tomato pots with soil probes, shielded air sensors and separate supported wetness plates; a shared stable camera and laptop.')
    md=re.sub(r'@photos ([^\n]+)',lambda m:'\n'.join(f'![{k}](assets/{k}.jpg)\n\n[Product-family source]({PHOTOS[k]["page"]})\n' for k in m[1].split()),md)
    def bommd(m):
        a,b=map(int,m.groups());s='| Item | Qty | Unit INR | Total INR |\n|---|---:|---:|---:|\n'
        for n,q,c,note in BOM[a:b]:s+=f'| {n} ({note}) | {q} | {c:,} | {q*c:,} |\n'
        return s
    md=re.sub(r'@bom (\d+) (\d+)',bommd,md).replace('@totals','**Subtotal INR 18,150 + 20% contingency INR 3,630 = ceiling INR 21,780.**')
    for k,_,url in SOURCES+TECH_SOURCES:md=md.replace('['+k+']',f'[{k}]({url})')
    (OUT/(path.stem+'.md')).write_text(md,encoding='utf-8')
    print(json.dumps(state))
    return state

def extras():
    tracker=f'# Paper-reading tracker\n\nStudent: {STUDENT} | Roll: {ROLL} | Guide: {GUIDE}\n\nMark actual reading depth only. Prepared literature briefs do not equal a completed full reading.\n\n'
    for key,desc,url in SOURCES[:8]:
        tracker+=f'## {key}. {desc}\n\nSource: {url}\n\nStatus: not yet recorded / abstract read / methods reviewed / full read / reproduced\n\nDate: ______\n\nProblem in my words:\n\nDataset and independent sample unit:\n\nMethod in five steps:\n\nSplit, baselines and metrics:\n\nMain finding with evaluation setting:\n\nLimitations / questions:\n\nPlantGuard design implication:\n\nWhat I can explain without notes:\n\n'
    (OUT/'Paper_Reading_Tracker.md').write_text(tracker,encoding='utf-8')
    (OUT/'Meeting_Feedback.md').write_text(f'# PlantGuard guide review\n\nStudent: {STUDENT}\nRoll: {ROLL}\nGuide: {GUIDE}\nMeeting date: ______\nNext review: ______\n\n## Agreed scope\n\n## Guide feedback\n\n## Features deferred\n\n## Budget / procurement decision\n\n## Action register\n\n| Action | Owner | Due date | Evidence | Status |\n|---|---|---|---|---|\n| | | | | |\n| | | | | |\n| | | | | |\n\n## Change log\n\nRecord the actual decision. This blank template does not imply approval.\n',encoding='utf-8')
    (OUT/'Dataset_Manifest_Template.csv').write_text('dataset_name,version,source_url,licence,retrieval_date,crop,class,raw_file_count,unique_file_count,split_unit,split,checksum_manifest,label_source,exclusions,notes\n',encoding='utf-8')
    # A usable inventory list; all quote and receipt fields deliberately empty.
    import csv
    with (OUT/'Procurement_Quote_Comparison.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f);w.writerow(['Item','Required qty','Planning unit INR','Exact model','Supplier','Quoted unit INR','Tax INR','Shipping INR','Landed total INR','Quote date','Received qty','Invoice / asset reference'])
        for n,q,c,note in BOM:w.writerow([n,q,c]+['']*9)
    sources='# Source register\n\nPrimary research / product references; checked for the planning pack on 8 September 2026.\n\n'
    for key,desc,url in SOURCES+TECH_SOURCES:sources+=f'- {key}. {desc} [{url}]({url})\n'
    sources+='\n## Images\n\nPlantGuard logo: previously generated project artwork. Hardware photographs are reference images from the original manufacturer/product pages below; they do not identify guaranteed suppliers or prices.\n\n'
    for key in SELECTED:sources+=f'- {key}: [{PHOTOS[key]["title"]}]({PHOTOS[key]["page"]})\n'
    (OUT/'Sources_and_Image_Credits.md').write_text(sources,encoding='utf-8')
    (OUT/'README.md').write_text(f'''# PlantGuard guide review pack

Prepared for **{STUDENT}**, roll number **{ROLL}**, M.Tech Computer Science, 3rd Semester, {INSTITUTE}. Guide: **{GUIDE}**.

Exact title: **{TITLE}**. System name: **PlantGuard**.

## What to open

1. **04_One_Page_Guide_Summary.pdf** - take this to the meeting first.
2. **01_College_Prototype_Guide_Report.pdf** - formal scope, literature, design and evaluation report.
3. **02_Hardware_Funding_Proposal.pdf** - separate physical-parts funding request.
4. **03_Guide_Meeting_and_Viva_Handbook.pdf** - detailed beginner explanations, model tutorials, worked metrics and 32 practice questions.

Matching `.md` files are editable text copies. `Paper_Reading_Tracker.md`, `Meeting_Feedback.md`, `Dataset_Manifest_Template.csv` and `Procurement_Quote_Comparison.csv` support the next steps.

## Status and budget

Initial discussion / planning and some preliminary reading. Dataset download and coding remain planned. No model accuracy, experiments, publication or guide approval is claimed.

Physical parts: INR 18,150 + 20% reserve INR 3,630 = INR 21,780. These are indicative allowances, not live quotations. The older master budget included an optional INR 2,000 compute reserve plus its INR 400 contingency; this college hardware request excludes both. Existing camera reuse and optional light-sensor omission can reduce the amount.

College AI runs on a laptop. Any later market service runs main AI on VPS/cloud; sensor boxes and gateways only handle sensing / communications.

The logo and hardware photos support presentation. Source and image credits are supplied. Reference visuals are not wiring diagrams. Typography: embedded Baskerville Old Face, Constantia and Corbel.

## Before the meeting

Read the one-page summary, rehearse the architecture, prepare genuine notes for R1/R2, and take the separate expense proposal. After the meeting, record agreed scope and due dates before implementation.
''',encoding='utf-8')

if __name__=='__main__':
    assert sum(q*c for _,q,c,_ in BOM)==18150
    maps=[]
    maps.append(build('report','01_College_Prototype_Guide_Report.pdf',REPORT+source_pages()))
    maps.append(build('fund','02_Hardware_Funding_Proposal.pdf',FUND))
    maps.append(build('hand','03_Guide_Meeting_and_Viva_Handbook.pdf',HANDBOOK))
    maps.append(build('summary','04_One_Page_Guide_Summary.pdf',[('PlantGuard: guide review summary',SUMMARY)]))
    extras()
    (TMP/'build_maps.json').write_text(json.dumps(maps,indent=2))
