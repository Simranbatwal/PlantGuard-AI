from pathlib import Path
import csv,json,shutil
p=Path('frontend/src/main.jsx')
s=p.read_text(encoding='utf-8-sig').replace('rows=matching?history:[]','rows=matching?history.filter(r=>r.zone_id===zone&&r.source_type===source):[]')
s=s.replace('<button key={id} className={page===id?', '<button key={id} aria-label={label} title={label} className={page===id?')
p.write_text(s,encoding='utf-8')
p=Path('backend/app.py');s=p.read_text(encoding='utf-8-sig')
s=s.replace('VALUES(?,?,?,?,?,?,?,?)\',(', 'VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(source,node,boot,seq) DO NOTHING\',(')
s=s.replace("            return {'id':cur.lastrowid,'duplicate':False}","""            if cur.rowcount==0:
                previous=c.execute('SELECT id,payload FROM telemetry WHERE source=? AND node=? AND boot=? AND seq=?',(value.source_type,value.node_id,value.boot_id,value.sequence)).fetchone()
                if previous['payload']!=payload:raise HTTPException(409,'This message identity already contains different data.')
                return {'id':previous['id'],'duplicate':True}
            return {'id':cur.lastrowid,'duplicate':False}""")
p.write_text(s,encoding='utf-8')
rows=list(csv.DictReader(open('data/processed/tomato_v1/manifest.csv',encoding='utf-8-sig')))
r=next(x for x in rows if x['split']=='train' and not x['exclusion'] and x['label']=='healthy')
dest=Path('docs/Phase_3_2026-09-13');shutil.copyfile(r['local_path'],dest/'UI_TEST_training_leaf.jpg')
(dest/'ui_sample_provenance.json').write_text(json.dumps({'purpose':'Upload-flow test only; not disease-model evaluation.','original_manifest_row':r},indent=2),encoding='utf-8')
print('Selected training-only upload fixture:',r['image_id'])
