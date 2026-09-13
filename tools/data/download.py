"""Download pinned, selected public dataset files; verify Git blob hashes; resume safely."""
import concurrent.futures,csv,hashlib,json,time,urllib.request,urllib.parse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SOURCES=ROOT/'data/sources'
def get(url):
 for attempt in range(4):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PlantGuard-academic-dataset-audit'}),timeout=45) as r:return r.read()
  except Exception:
   if attempt==3:raise
   time.sleep(2**attempt)
def api(repo,path):return json.loads(get('https://api.github.com/repos/'+repo+path))
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def main():
 jobs=[]
 for tag,repo in [('plantvillage','spMohanty/PlantVillage-Dataset'),('plantdoc','pratikkayal/PlantDoc-Dataset')]:
  root=json.loads((SOURCES/(tag+'_root.json')).read_text()); commit=root['sha']
  if tag=='plantvillage':
   raw=api(repo,'/git/trees/'+next(x['sha'] for x in root['tree'] if x['path']=='raw'))
   color=api(repo,'/git/trees/'+next(x['sha'] for x in raw['tree'] if x['path']=='color'))
   mapping={'Tomato___healthy':'healthy','Tomato___Early_blight':'early_blight','Tomato___Late_blight':'late_blight','Tomato___Septoria_leaf_spot':'unsupported','Potato___healthy':'unsupported','Apple___healthy':'unsupported'}
   for cls,label in mapping.items():
    tree=api(repo,'/git/trees/'+next(x['sha'] for x in color['tree'] if x['path']==cls))
    assert not tree.get('truncated'); (SOURCES/('pv_'+cls+'.json')).write_text(json.dumps(tree),encoding='utf-8')
    entries=[x for x in tree['tree'] if x['type']=='blob']
    if label=='unsupported':entries=sorted(entries,key=lambda x:hashlib.sha256(x['path'].encode()).hexdigest())[:60]
    for x in entries: jobs.append(dict(dataset=tag,commit=commit,repo=repo,source_path='raw/color/'+cls+'/'+x['path'],label=label,original_class=cls,blob_sha=x['sha'],size=x['size'],original_split='unsplit',role='ood' if label=='unsupported' else 'benchmark'))
  else:
   tree=json.loads((SOURCES/(tag+'_tree.json')).read_text()); assert not tree.get('truncated')
   mapping={'Tomato leaf':'healthy','Tomato Early blight leaf':'early_blight','Tomato leaf late blight':'late_blight'}
   for x in tree['tree']:
    parts=x['path'].split('/')
    if x['type']=='blob' and len(parts)==3 and parts[1] in mapping:
     jobs.append(dict(dataset=tag,commit=commit,repo=repo,source_path=x['path'],label=mapping[parts[1]],original_class=parts[1],blob_sha=x['sha'],size=x['size'],original_split=parts[0],role='external'))
 for j in jobs:
  local=j['source_path']
  if any(c in Path(local).name for c in '<>:"|?*') or len(local)>170:
   local=str(Path(local).parent.as_posix())+'/'+hashlib.sha256(local.encode()).hexdigest()[:24]+'.jpg'
  j['local_path']='data/raw/'+j['dataset']+'/'+local; j['source_url']='https://raw.githubusercontent.com/'+j['repo']+'/'+j['commit']+'/'+urllib.parse.quote(j['source_path'])
 with (SOURCES/'download_manifest.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(jobs[0]));w.writeheader();w.writerows(jobs)
 print('Selected',len(jobs),'files;',round(sum(j['size'] for j in jobs)/1024**2,1),'MiB',flush=True)
 def download(j):
  p=ROOT/j['local_path']; p.parent.mkdir(parents=True,exist_ok=True)
  try:
   if p.exists() and blob(p.read_bytes())==j['blob_sha']:return None
   b=get(j['source_url'])
   if blob(b)!=j['blob_sha']:raise ValueError('Git blob checksum mismatch')
   q=p.with_name(p.name+'.partial');q.write_bytes(b);q.replace(p);return None
  except Exception as e:return {'path':j['source_path'],'error':str(e)}
 errors=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for i,result in enumerate(ex.map(download,jobs),1):
   if result:errors.append(result)
   if i%250==0:print('Verified/downloaded',i,'/',len(jobs),'errors',len(errors),flush=True)
 (SOURCES/'download_status.json').write_text(json.dumps({'selected':len(jobs),'errors':errors,'finished_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())},indent=2))
 print('Finished; errors:',len(errors),flush=True)
 if errors:raise SystemExit(1)
if __name__=='__main__':main()
