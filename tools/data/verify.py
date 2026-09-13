"""Independent checks of the frozen dataset release; no model fitting."""
import csv,hashlib,json,sys
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 out=ROOT/'data/processed/tomato_v1';rows=list(csv.DictReader((out/'manifest.csv').open(encoding='utf-8')));audit=json.loads((out/'audit.json').read_text())
 assert len({r['image_id'] for r in rows})==len(rows)==audit['downloaded']
 for r in rows:
  assert hashlib.sha256((ROOT/r['local_path']).read_bytes()).hexdigest()==r['sha256'],r['local_path']
 counts=dict(Counter(r['dataset']+'/'+r['label']+'/'+r['split'] for r in rows));assert counts==audit['counts']
 for key in ['sha256','pixel_sha256','group_id']:
  seen=defaultdict(set)
  for r in rows:
   if r['split']!='excluded':seen[r[key]].add(r['split'])
  assert all(len(v)==1 for v in seen.values()),key
 known={r['image_id']:r for r in rows}
 for r in csv.DictReader((out/'quality_cases.csv').open(encoding='utf-8')):
  assert known[r['parent_id']]['split']==r['parent_split']; assert (ROOT/r['local_path']).exists()
 computed=hashlib.sha256('\n'.join(sorted(r['image_id']+','+r['sha256']+','+r['split']+','+r['group_id'] for r in rows)).encode()).hexdigest();assert computed==audit['split_sha256']
 for split in {r['split'] for r in rows}:
  expected={r['image_id'] for r in rows if r['split']==split};actual={r['image_id'] for r in csv.DictReader((out/(split+'.csv')).open(encoding='utf-8'))};assert expected==actual
 print(json.dumps({'status':'PASS','raw_files_verified':len(rows),'split_sha256':computed,'checks':['SHA256 of every raw file','unique image IDs','counts match audit','byte/pixel/group disjointness','split CSV membership','quality-case parent separation']},indent=2))
if __name__=='__main__':main()
