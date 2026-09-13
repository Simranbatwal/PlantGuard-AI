from pathlib import Path
import re,html,json,csv
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image,PageBreak,Flowable,KeepTogether
from PIL import Image as PILImage
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'docs/Phase_1_2_2026-09-12'
for name,file in [('Body','constan.ttf'),('BodyBold','constanb.ttf'),('BodyItalic','constani.ttf'),('UI','corbel.ttf'),('UIBold','corbelb.ttf'),('Display','BASKVILL.TTF')]:pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='BodyItalic',boldItalic='BodyBold')
GREEN=colors.HexColor('#126447');INK=colors.HexColor('#183344');GRAY=colors.HexColor('#52636b');PALE=colors.HexColor('#edf5f0');W,H=A4;CW=W-100
S={'body':ParagraphStyle('body',fontName='Body',fontSize=10.5,leading=14.8,spaceAfter=8,textColor=INK),'h1':ParagraphStyle('h1',fontName='Display',fontSize=24,leading=28,spaceAfter=18,textColor=GREEN),'h2':ParagraphStyle('h2',fontName='UIBold',fontSize=14,leading=18,spaceBefore=12,spaceAfter=8,textColor=GREEN,keepWithNext=True),'small':ParagraphStyle('small',fontName='UI',fontSize=9,leading=12,spaceAfter=6,textColor=GRAY),'cell':ParagraphStyle('cell',fontName='UI',fontSize=9,leading=12,textColor=INK),'headcell':ParagraphStyle('headcell',fontName='UIBold',fontSize=9,leading=12,textColor=colors.white),'cover':ParagraphStyle('cover',fontName='Display',fontSize=28,leading=34,spaceAfter=18,textColor=GREEN)}
def rich(s):
 s=html.escape(s.replace('\ufeff','').replace('\u2013','-').replace('\u2014','-').replace('\u2011','-'))
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s);s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
 s=re.sub(r'`([^`]+)`',r'\1',s)
 s=re.sub(r'(https?://[^\s<>]+)',r'<link href="\1" color="#126447">\1</link>',s)
 return s

def p(s,style='body'):return Paragraph(rich(s),S[style])
def table(lines):
 rows=[[c.strip() for c in line.strip().strip('|').split('|')] for line in lines if not re.match(r'^\|[\s:\-|]+\|$',line)]
 n=len(rows[0]);fractions={3:[.20,.38,.42],4:[.25,.25,.25,.25],6:[.21,.16,.16,.15,.16,.16]}.get(n,[1/n]*n)
 t=Table([[p(v,'headcell' if i==0 else 'cell') for v in row] for i,row in enumerate(rows)],colWidths=[CW*f for f in fractions],repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),GREEN),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,-1),(-1,-1),.5,colors.HexColor('#b9cfc2'))]));return t
class Bookmark(Flowable):
 def __init__(self,title):Flowable.__init__(self);self.title=title;self.width=0;self.height=0
 def draw(self):
  key='s'+str(self.canv.getPageNumber());self.canv.bookmarkPage(key);self.canv.addOutlineEntry(self.title,key,0)

def parse(text):
 story=[];lines=text.splitlines();i=0
 while i<len(lines):
  line=lines[i].strip();i+=1
  if not line:continue
  if line.startswith('|'):
   rows=[line]
   while i<len(lines) and lines[i].strip().startswith('|'):rows.append(lines[i].strip());i+=1
   story.extend([table(rows),Spacer(1,10)]);continue
  if line.startswith('# '):story.extend([Bookmark(line[2:]),p(line[2:],'h1')]);continue
  if line.startswith('## '):story.append(p(line[3:],'h2'));continue
  story.append(p(line))
 return story

def footer(c,doc):
 c.saveState();c.setStrokeColor(GREEN);c.setLineWidth(.5);c.line(50,43,W-50,43);c.setFont('UI',8);c.setFillColor(GRAY);c.drawString(50,30,'PlantGuard | Phase 1-2 | Simran Batwal');c.drawRightString(W-50,30,str(doc.page));
 if doc.page>1:c.setFont('UI',8);c.drawString(50,H-32,'RESEARCH FOUNDATION AND DATA PREPARATION');c.drawRightString(W-50,H-32,'13 SEPTEMBER 2026')
 c.restoreState()

files=['00_Progress_Summary.md','01_Research_and_Protocol.md','02_Dataset_Audit.md','R1_Detailed_Review.md','R2_Detailed_Review.md','R3_Detailed_Review.md','R4_Detailed_Review.md']
story=[Spacer(1,20),Image(str(ROOT/'docs/Master_Plan_2026-09-08/assets/PlantGuard_Logo.png'),width=360,height=240),Spacer(1,8),p('Research Foundation<br/>and Dataset Preparation','cover')]
# Use explicit line break markup only for this cover title.
story[-1]=Paragraph('Research Foundation<br/>and Dataset Preparation',S['cover'])
story.extend([p('PHASE 1 AND PHASE 2 - PROGRESS REPORT','h2'),p('AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN'),Spacer(1,20),p('Simran Batwal | Roll number 28452500003'),p('M.Tech Computer Science | Semester 3'),p('Guru Nanak Dev University, Amritsar'),p('Under the guidance of Dr. Anil Kumar'),Spacer(1,16),p('Work: 12-13 September 2026 | Software-first college prototype','small'),PageBreak()])
for index,file in enumerate(files):
 if index:story.append(PageBreak())
 story.extend(parse((OUT/file).read_text(encoding='utf-8-sig')))
 # A few actual dataset photos make the data chapter concrete.
 if file=='02_Dataset_Audit.md':
  story.append(PageBreak());story.extend([p('Examples from the prepared benchmark','h1'),p('Original PlantVillage colour photos. Captions show repository labels, not a new laboratory diagnosis. Source: Mohanty et al.; CC BY-SA 3.0 as declared in the saved dataset card.','small')])
  rows=list(csv.DictReader((ROOT/'data/processed/tomato_v1/train.csv').open(encoding='utf-8')));thumbrows=[]
  for label in ['healthy','early_blight','late_blight']:
   samples=sorted([r for r in rows if r['label']==label],key=lambda r:r['image_id'])[:2]
   cells=[]
   for r in samples:cells.append([Image(str(ROOT/r['local_path']),width=170,height=170),p(label.replace('_',' ').title()+' | '+r['image_id'][:8],'small')])
   thumbrows.append(cells)
  t=Table(thumbrows,colWidths=[CW/2]*2);t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),12)]));story.append(t)
filename=OUT/'PlantGuard_Phase_1_2_Progress_Report.pdf'
doc=SimpleDocTemplate(str(filename),pagesize=A4,rightMargin=50,leftMargin=50,topMargin=58,bottomMargin=58,title='PlantGuard - Phase 1 and 2 Progress Report',author='Simran Batwal')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
combined='\n\n---\n\n'.join((OUT/f).read_text(encoding='utf-8-sig') for f in files);(OUT/'PlantGuard_Phase_1_2_Progress_Report.md').write_text(combined,encoding='utf-8')
r=PdfReader(filename);(OUT/'qa/pdf_structure.json').write_text(json.dumps({'pages':len(r.pages),'file':str(filename),'extracted_characters':[len(p.extract_text()) for p in r.pages]},indent=2));print('PDF created:',len(r.pages),'pages')
