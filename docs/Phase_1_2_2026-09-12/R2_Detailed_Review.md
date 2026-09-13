# R2 - PlantDoc and less controlled images

**Paper:** Singh, Jain, Jain, Kayal, Kumawat and Batra (2020; preprint 2019), *PlantDoc: A Dataset for Visual Plant Disease Detection*. CODS-COMAD, pp. 249-253. DOI: https://doi.org/10.1145/3371158.3371196 ; full text: https://arxiv.org/html/1911.10317
**Reading record:** Full paper, benchmark tables and limitations examined; PDF saved locally.

## Problem and data
PlantDoc addresses the lack of labelled plant photos taken outside a controlled laboratory background. The authors collected about 20,900 candidate internet images and filtered them to 2,598 images across 13 species and 27 healthy/disease categories. The annotation process involved about 300 human hours. Two people checked images using metadata and symptom guidance. The authors also annotated bounding boxes and describe 9,216 cropped leaf regions.

The distinction between original photos, annotated boxes and cropped classification files matters. The current classification repository describes itself as Cropped-PlantDoc, but its local file count must be measured rather than assumed to equal the paper's 9,216 boxes. Our download manifest records the exact repository snapshot and selected files.

## Method and evaluation
The paper compares VGG16, InceptionV3 and InceptionResNetV2 with ImageNet initialisation, PlantVillage training, and PlantVillage followed by PlantDoc fine-tuning. Classification experiments use an 80/20 division and 100 by 100 pixel inputs. SGD uses momentum 0.9 and learning rate 0.001. Detection experiments use MobileNet and Faster R-CNN; the stated detection split is 2,360/238. Classification accuracy and detection mAP are different measures.

## Reported results
In Table 1, VGG16 trained on PlantVillage achieved 15.08% on uncropped PlantDoc; PlantVillage pretraining followed by PlantDoc fine-tuning reached 29.73%. In Table 2, InceptionResNetV2 reached 39.87% when trained on PlantVillage and evaluated on cropped PlantDoc, compared with 70.53% after PlantDoc fine-tuning. Their difference is 30.66 percentage points. It should not be loosely described as a guaranteed 31% improvement for every model or dataset. Table 3 reports the best detection mAP at IoU 0.5 as 38.9, a different task from classification.

## Limitations and my assessment
The authors acknowledge possible labelling mistakes and small class sizes. Web images can contain watermarks, multiple leaves, mixed symptoms and misleading website labels. Related crops of one original photo can also make an image-level split optimistic unless grouped. A web-collected external set tests a different image source; it is not the same as a prospective GNDU greenhouse trial.

I will keep the selected PlantDoc tomato images entirely outside training and threshold selection for the first experiment. I will preserve the original train/test folder names as provenance, but combine their compatible selected files into our external-only evaluation pool. This is a custom external test, not reproduction of the published PlantDoc split or score. Obvious unsuitable images will be excluded with reasons; uncertain disease labels will not be silently corrected without expert evidence.

## Connection to PlantGuard
The repository supplies selected tomato healthy, early-blight and late-blight examples. I will audit them for decode errors, exact and likely near duplicates, overlap with PlantVillage, and obvious image-content issues. The final external count may be lower than the download count. I will present errors and uncertainty, not just a single favourable score.

**Guide answer:** PlantDoc helps me test whether a model trained on clean images also handles more varied photos. Its labels and image quality have limitations, so I have kept its audit and results separate.

**Locations to revisit:** Sections 3.1 and 4; Tables 1-3; Section 7.
