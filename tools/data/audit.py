"""Audit downloaded bytes, decode images, group leaves/duplicates, and freeze splits."""
import csv,hashlib,json,random,struct,time,sys
from collections import Counter,defaultdict
from pathlib import Path
import imagehash
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont,ImageFilter,ImageEnhance
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'data/processed/tomato_v1'; OUT.mkdir(parents=True,exist_ok=True)
SEED=284525; NEAR_DISTANCE=6

def writecsv(path,rows,fields=None):
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def digest(b):return hashlib.sha256(b).hexdigest()
class Groups:
 def __init__(self,n):self.p=list(range(n))
 def find(self,x):
  while self.p[x]!=x:self.p[x]=self.p[self.p[x]];x=self.p[x]
  return x
 def join(self,a,b):self.p[self.find(b)]=self.find(a)
def main():
 rows=list(csv.DictReader((ROOT/'data/sources/download_manifest.csv').open(encoding='utf-8-sig')))
 leafmap=json.loads((ROOT/'data/sources/plantvillage_leaf-map.json').read_text()); seenbytes={};seenpixels={};seenleaf={}; good=[]; excludes=[]
 overrides_path=ROOT/'data/sources/visual_review.csv'
 overrides={r['local_path']:r['reason'] for r in csv.DictReader(overrides_path.open(encoding='utf-8'))} if overrides_path.exists() else {}
 for j in rows:
  p=ROOT/j['local_path']; b=p.read_bytes()
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==j['blob_sha'],p
  j.update(image_id=digest(j['local_path'].encode())[:16],sha256=digest(b),exclusion='',leaf_group='')
  try:
   with Image.open(p) as im:im.verify()
   with Image.open(p) as im:
    im=ImageOps.exif_transpose(im).convert('RGB'); im.load();w,h=im.size
    j.update(width=w,height=h,pixel_sha256=digest(struct.pack('>II',w,h)+im.tobytes()),phash=str(imagehash.phash(im)),mirror_phash=str(imagehash.phash(ImageOps.mirror(im))))
    g=np.asarray(im.resize((128,128)).convert('L'),dtype=float); j['brightness']=round(float(g.mean()),2);j['edge_variance']=round(float((g[1:-1,:-2]+g[1:-1,2:]+g[:-2,1:-1]+g[2:,1:-1]-4*g[1:-1,1:-1]).var()),2)
    if min(w,h)<64:j['exclusion']='minimum_dimension_below_64'
  except Exception as e:
   j['exclusion']='decode_error:'+str(e);excludes.append(j);continue
  if j['dataset']=='plantvillage':
   key=Path(j['source_path']).stem.split('___',1)[-1].lower()
   groups=[s for s in leafmap.get(key,[]) if s.startswith(j['original_class']+':::')]
   j['leaf_group']='|'.join(sorted(groups))
  if j['local_path'] in overrides:j['exclusion']='visual_review:'+overrides[j['local_path']]
  good.append(j)
 print('Decoded',len(good),'files',flush=True)
 uf=Groups(len(good)); pairs=[]
 for i,r in enumerate(good):
  for field,seen in [('sha256',seenbytes),('pixel_sha256',seenpixels),('leaf_group',seenleaf)]:
   key=r[field]
   if key:
    if key in seen:uf.join(i,seen[key])
    else:seen[key]=i
 review_file=ROOT/'data/sources/pair_review.csv'
 decisions={frozenset((r['image_a'],r['image_b'])):r['decision'] for r in csv.DictReader(review_file.open(encoding='utf-8'))} if review_file.exists() else {}
 hashes=[int(r['phash'],16) for r in good];mirrors=[int(r['mirror_phash'],16) for r in good]
 for i in range(len(good)):
  for k in range(i):
   d=min((hashes[i]^hashes[k]).bit_count(),(hashes[i]^mirrors[k]).bit_count())
   if d<=NEAR_DISTANCE:
    decision=decisions.get(frozenset((good[k]['image_id'],good[i]['image_id'])),'conservative_group')
    if decision!='distinct_images':uf.join(i,k)
    pairs.append(dict(review_decision=decision,image_a=good[k]['image_id'],image_b=good[i]['image_id'],distance=d,path_a=good[k]['local_path'],path_b=good[i]['local_path'],cross_dataset=good[k]['dataset']!=good[i]['dataset'],label_conflict=good[k]['label']!=good[i]['label']))
 groups=defaultdict(list)
 for i,r in enumerate(good):groups[uf.find(i)].append(r)
 for members in groups.values():
  gid=digest('|'.join(sorted(r['image_id'] for r in members)).encode())[:20];labels={r['label'] for r in members};roles={r['role'] for r in members};pix={}
  for r in sorted(members,key=lambda x:x['local_path']):
   r['group_id']=gid
   if len(labels)>1:r['exclusion']='conflicting_labels_in_related_group'
   elif r['role']=='external' and 'benchmark' in roles:r['exclusion']='external_related_to_benchmark'
   elif r['pixel_sha256'] in pix:r['exclusion']=r['exclusion'] or 'duplicate_pixels'
   if not r['exclusion']:pix[r['pixel_sha256']]=r['image_id']
   r['split']='excluded' if r['exclusion'] else ('external_test' if r['role']=='external' else '')
 # Assign whole groups deterministically; source leaf identities remain together.
 for role in ['benchmark','ood']:
  for cls in sorted({r['original_class'] for r in good if r['role']==role}):
   candidates=defaultdict(list)
   for r in good:
    if r['role']==role and r['original_class']==cls and not r['exclusion']:candidates[r['group_id']].append(r)
   items=sorted(candidates.items());random.Random(SEED).shuffle(items)
   n=sum(len(v) for _,v in items);fractions={'train':.70,'validation':.15,'test':.15} if role=='benchmark' else {'ood_validation':.5,'ood_test':.5};counts=Counter()
   for gid,rr in items:
    split=max(fractions,key=lambda s:n*fractions[s]-counts[s]);counts[split]+=len(rr)
    for r in rr:r['split']=split
 fields=list(good[0]);writecsv(OUT/'manifest.csv',good,fields)
 writecsv(OUT/'near_duplicate_pairs.csv',pairs,['image_a','image_b','distance','path_a','path_b','cross_dataset','label_conflict','review_decision'])
 for split in sorted({r['split'] for r in good}):writecsv(OUT/(split+'.csv'),[r for r in good if r['split']==split],fields)
 # Leakage checks operate on every accepted partition, including external and OOD.
 for key in ['group_id','sha256','pixel_sha256','leaf_group']:
  buckets=defaultdict(set)
  for r in good:
   if r['split']!='excluded' and r[key]:buckets[r[key]].add(r['split'])
  assert all(len(s)==1 for s in buckets.values()),'Cross-split leakage: '+key
 for p in pairs:
  if p['review_decision']=='distinct_images':continue
  a=next(r for r in good if r['image_id']==p['image_a']);b=next(r for r in good if r['image_id']==p['image_b'])
  assert 'excluded' in (a['split'],b['split']) or a['split']==b['split']
 split_hash=digest('\n'.join(sorted(r['image_id']+','+r['sha256']+','+r['split']+','+r['group_id'] for r in good)).encode())
 summary={'dataset_version':'tomato_v1','seed':SEED,'near_distance':NEAR_DISTANCE,'downloaded':len(rows),'decoded':len(good),'decode_failures':len(excludes),'exact_byte_duplicate_excess':len(good)-len(seenbytes),'exact_pixel_duplicate_excess':len(good)-len(seenpixels),'near_pairs':len(pairs),'reviewed_distinct_pairs':sum(p['review_decision']=='distinct_images' for p in pairs),'cross_dataset_near_pairs':sum(p['cross_dataset'] for p in pairs),'conflicting_label_near_pairs':sum(p['label_conflict'] for p in pairs),'pv_with_leaf_group':sum(bool(r['leaf_group']) for r in good if r['dataset']=='plantvillage'),'pv_total':sum(r['dataset']=='plantvillage' for r in good),'exclusions':dict(Counter(r['exclusion'] for r in good if r['exclusion'])),'counts':dict(Counter(r['dataset']+'/'+r['label']+'/'+r['split'] for r in good)),'split_sha256':split_hash,'leakage_checks':'PASS: byte, pixel, leaf and detected near-duplicate groups disjoint across accepted partitions','created_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
 (OUT/'audit.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2),flush=True)
 # Contact sheets identify all external images; original filenames are in the manifest.
 contact=OUT/'contact_sheets';contact.mkdir(exist_ok=True)
 font=ImageFont.truetype('C:/Windows/Fonts/corbel.ttf',15) if Path('C:/Windows/Fonts/corbel.ttf').exists() else ImageFont.load_default()
 for tag,subset in [('external',[r for r in good if r['role']=='external']),('benchmark_sample',[r for c in ['healthy','early_blight','late_blight'] for r in sorted([x for x in good if x['role']=='benchmark' and x['label']==c],key=lambda x:x['image_id'])[:12]])]:
  for page,start in enumerate(range(0,len(subset),36),1):
   canvas=Image.new('RGB',(1200,1320),'white');draw=ImageDraw.Draw(canvas)
   for k,r in enumerate(subset[start:start+36]):
    x=(k%6)*200;y=(k//6)*220
    with Image.open(ROOT/r['local_path']) as im:im=ImageOps.exif_transpose(im).convert('RGB');im.thumbnail((190,175));canvas.paste(im,(x,y))
    draw.text((x,y+175),r['image_id'][:8]+' '+r['label'],fill='black',font=font);draw.text((x,y+195),r['split'],fill='red' if r['exclusion'] else 'green',font=font)
   canvas.save(contact/(tag+'_'+str(page)+'.jpg'))
 # Poor-quality derived cases are separately labelled, keeping their parent split.
 cases=[]
 for split in ['validation','test']:
  subset=[r for c in ['healthy','early_blight','late_blight'] for r in sorted([x for x in good if x['split']==split and x['label']==c],key=lambda x:x['image_id'])[:5]]
  for r in subset:
   with Image.open(ROOT/r['local_path']) as im:
    im=ImageOps.exif_transpose(im).convert('RGB')
    variants={'blur':im.filter(ImageFilter.GaussianBlur(7)),'dark':ImageEnhance.Brightness(im).enhance(.12),'low_resolution':im.resize((24,24)).resize(im.size)}
    for kind,v in variants.items():
     p=OUT/'quality_cases'/split/(r['image_id']+'_'+kind+'.png');p.parent.mkdir(parents=True,exist_ok=True);v.save(p);cases.append(dict(local_path=p.relative_to(ROOT).as_posix(),parent_id=r['image_id'],parent_split=split,label=r['label'],transformation=kind,source_type='synthetic_degradation'))
 writecsv(OUT/'quality_cases.csv',cases)
if __name__=='__main__':main()
