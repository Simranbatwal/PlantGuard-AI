# Phase 1 and 2 - simple revision notes

## Ab humne kya samjha?
PlantGuard ke do alag inputs hain: leaf photo aur environment readings. Photo se current visible condition classify karni hai. Sensors se plant ke paas ki conditions record hongi. Dono ek jagah dikhana useful hai, lekin isse automatically scientifically validated fusion nahi ban jata.

**Healthy** hamare dataset ki category hai. **Early blight** ek disease ka naam hai. **Late blight** doosri disease ka naam hai. Early aur late ko ek hi disease ke starting aur final stages mat bolna.

## Papers ko simple way mein samjho
- R1: clean photos par result bahut achha tha; different photos par kaafi gir gaya. Isliye sirf high accuracy dekhkar model ready mat maanna.
- R2: real-looking web photos zyada difficult hain. Background, multiple leaves aur wrong labels problem bana sakte hain.
- R3: photo aur sensor fusion pehle se research mein hai. Missing sensor estimate karna actual measurement nahi hai.
- R4: advance warning ke liye time history aur baad mein confirmed disease events chahiye. Sirf photos download karke 20 hours early warning claim nahi kar sakte.

## Dataset ke words
Dataset = labelled images ka collection. Label = image par diya category name. Manifest = har file ka register. Checksum = file ka digital fingerprint. Duplicate = same/repeated photo. Near duplicate = thodi edited ya similar photo, jise check/group karna hai. Leaf group = ek hi leaf ki related photos.

Train set model ko sikhata hai. Validation set settings aur threshold choose karne mein help karta hai. Test set final independent check hai. Test dekhkar baar-baar model badalna test ka purpose khatam karta hai. External test alag source/capture conditions ka check hai. Augmentation training image ki rotated/changed version hai, nayi independent plant observation nahi.

Data leakage ka example: ek leaf ki photo train mein aur usi photo ki slightly rotated copy test mein aa gayi. Model ko test unfairly easy mil sakta hai. Isliye split groups ke basis par hai.

## Guide ko kaise explain karun?
Sir, maine four relevant papers ka comparison aur tomato dataset preparation ki hai. Maine clean-image benchmark aur external photos separate rakhe hain. Related photos ko same partition mein rakha hai aur doubtful/unsuitable files ka exclusion record banaya hai. Ab mera next step dashboard aur controlled model experiments hai. Abhi model accuracy ka result nahi hai.

## Mere project mein alag kya evaluate hoga?
Main four models ka same data par comparison karungi. Phir dekhungi ki unclear/unsupported photo par har baar answer dene ke bajaye rejection ya retake request se accepted answers ki reliability improve hoti hai ya nahi. Saath mein two-zone sensor data ka proper missing/stale handling hoga. Improvement actual results ke baad likhungi.

## Main khud ab kya karun?
1. R1-R4 notes padhkar har paper ko do minute mein explain karne ki practice karun.
2. Train, validation, test aur leakage ka example samjhun.
3. Guide ko current progress aur proposed research question bataun; jo feedback mile exact note karun.
4. Model-training phase mein Colab login aur Drive permission apne account se connect karun. Password share karne ki zarurat nahi.
5. Abhi hardware purchase na karun. Software checkpoint ke baad final list use karungi.

Code aur notes project folder mein hain. Hum model results aur thesis chapters actual experiments ke saath update karenge.
