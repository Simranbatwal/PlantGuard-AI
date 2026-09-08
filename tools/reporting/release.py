from pathlib import Path
import json,shutil,hashlib,zipfile
from content import BASE,OUT

check=json.loads((Path(__file__).parent/'verification.json').read_text())
assert not check['issues'],check['issues']
current=BASE/'docs/Guide_Review_2026-09-08'
archive=BASE/'docs/archive/Guide_Review_v1_2026-09-08'
archive.parent.mkdir(parents=True,exist_ok=True)
if archive.exists():raise RuntimeError('Earlier archive exists; choose a new archive before another release.')
shutil.copytree(current,archive)
old_zip=BASE/'PlantGuard_Guide_Review_2026-09-08.zip'
if old_zip.exists():shutil.copy2(old_zip,archive/'Original_Guide_Pack.zip')

replaced=[]
for file in OUT.iterdir():
    if file.suffix.lower() in ('.pdf',) or (file.suffix.lower()=='.md' and (file.name[:2] in ('01','02','03','04') or file.name=='Sources_and_Image_Credits.md')):
        dest=current/file.name
        shutil.copy2(file,dest)
        assert hashlib.sha256(file.read_bytes()).digest()==hashlib.sha256(dest.read_bytes()).digest()
        replaced.append(file.name)

(current/'README.md').write_text('''# PlantGuard guide review pack

Student: **Simran Batwal**, roll number **28452500003**. M.Tech, Computer Science, 3rd Semester, Guru Nanak Dev University, Amritsar. Guide: **Dr. Anil Kumar**.

Project title: **AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**. System name: **PlantGuard**.

## Current files

- **01_College_Prototype_Guide_Report.pdf**: 25-page college report in simple first-person English, including previous work, current progress and proposed comparisons.
- **02_Hardware_Funding_Proposal.pdf**: 7-page request, component list, cost alternatives and approval fields.
- **03_Guide_Meeting_and_Viva_Handbook.pdf**: 41-page Hinglish revision handbook. Start with plant and electrical basics, then sensors, networking, software, models and metrics. Meeting scripts and 32 practice questions follow.
- **04_One_Page_Guide_Summary.pdf**: short handout for the guide meeting.

Matching Markdown files are editable copies. Reading, meeting, dataset and quotation templates remain available in this folder.

## Current stage

Topic discussion, initial planning and preliminary reading have started. Detailed reading, dataset preparation, hardware assembly and coding are next. College AI will run on a laptop; a later market service will use VPS/cloud processing.

The hardware estimate remains INR 18,150 plus a 20% reserve of INR 3,630, for a proposed total of INR 21,780. Prices will be confirmed through quotations.

## Revision record

This edition uses simpler student-facing language, removes the wording “existing laptop”, explains previous work versus proposed work, and expands the beginner handbook. Earlier files are preserved in `../archive/Guide_Review_v1_2026-09-08/`.

Sources and image credits are included. The master plan and original references are preserved separately. Future documents should follow the writing preferences in the project's AGENTS.md.
''',encoding='utf-8')

readme=BASE/'README.md'
text=readme.read_text(encoding='utf-8').replace('College AI runs on the existing laptop.','College AI runs on a laptop.')
text+='''

## Updated reports and writing style

The current guide folder contains the revised 25-page college report, 7-page funding proposal, 41-page beginner viva handbook and one-page summary. The formal documents use simple first-person English and separate previous research, current progress and proposed work. The handbook explains project terminology in Hinglish with examples and viva answers.

The earlier guide pack is preserved at `docs/archive/Guide_Review_v1_2026-09-08/`. The main ZIP has been refreshed. Future document preferences are saved in AGENTS.md; use “laptop” and natural language, and state actual progress directly.
'''
readme.write_text(text,encoding='utf-8')

with zipfile.ZipFile(old_zip,'w',zipfile.ZIP_DEFLATED) as z:
    for file in sorted(current.rglob('*')):
        if file.is_file():z.write(file,file.relative_to(current))
with zipfile.ZipFile(old_zip) as z:assert z.testzip() is None
result={'current_folder':str(current),'archive':str(archive),'updated_files':replaced,'zip':str(old_zip),'verified_pages':sum(d['pages'] for d in check['documents'])}
(Path(__file__).parent/'release_record.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
