# R4 - Time-aligned tomato late-blight risk research

**Paper:** Gao et al. (2026), *Environmental-Visual Fusion for Proactive Tomato Late Blight Management in Protected Horticulture*. Horticulturae 12(3):299. DOI: https://doi.org/10.3390/horticulturae12030299
**Reading record:** The 28-page primary PDF was examined, including collection, temporal separation, architecture, main results, ablation and limitations.

## Problem and data
The study asks whether environmental history and visual symptoms can support earlier tomato late-blight warning in a greenhouse. Data were collected in Bayannur, Inner Mongolia, during November 2023 to March 2024. Table 1 reports 18,600 images and 172,800 records for each of four minute-sampled environmental variables: air temperature, relative humidity, leaf wetness and light. Labels cover healthy, potential-risk and symptomatic stages. These are not the same labels as healthy, early blight and late blight: early blight is a separate disease name, not an early stage of late blight.

## Method and split
The environmental branch processes a 24-hour history. A hierarchical visual Transformer extracts image features. Temporal and visual representations are aligned and fused with attention to produce risk scores, followed by greenhouse-control mapping. Section 4.1 describes a chronological 70/15/15 split with a 24-hour buffer between partitions and time-series cross-validation. Training uses 224-pixel images, AdamW, batch size 32, up to 200 epochs and early-stopping patience 20. This is a substantially larger collection and compute setup than two college pots.

## Reported results
Table 2 reports 0.952 accuracy, 0.944 F1, 0.975 AUC and 21.6 hours of risk lead time for the full system. Its vision-only ResNet50 baseline reports 0.914 accuracy and 5.6 hours. Table 5 reports that removing temporal modelling reduces lead time to 8.0 hours. Removing control mapping leaves prediction metrics unchanged, so control benefit and predictive accuracy must be analysed separately. These are the authors' greenhouse results; PlantGuard has not reproduced them.

## Limitations and my assessment
The paper acknowledges one greenhouse and one production cycle, dependence on sensor continuity, and the need for wider validation. Potential-risk labels partly use environmental risk analysis. For an independent early-warning claim, I would check that the labels are confirmed by later disease events rather than simply reproducing rules derived from the same input readings.

The stated 172,800 minute records correspond to 120 days of uninterrupted sampling; the calendar collection window spans about five months. Missing periods, selected intervals and effective sample counts would need clarification before reproduction. I would also record the number of independent outbreaks, class counts, alert threshold, false-alert definition and exactly how future outcomes were confirmed. A temporal gap is helpful, but preprocessing must remain causal: future readings must not be used to interpolate a real-time input. The paper's descriptive collection and data-availability statement do not give us a directly usable paired download in this phase.

## Connection to PlantGuard
This paper supports keeping sensor timestamps, missingness and history in the design. It does not allow us to claim advance warning from a folder of still leaf photos. I will use the public images for current-condition classification. Later, if enough independent time-labelled disease events are available, I can define a forecasting horizon and use chronological splits with a suitable gap. Until then, environmental readings provide monitoring context and any rule-based alert will be named accordingly.

Our college and market compute decisions stay unchanged: laptop first, VPS/cloud later. The paper's greenhouse-control system is not a reason to add a field AI box or automatic sprayer to the current scope.

**Guide answer:** Diagnosis asks what the image shows now. Forecasting asks what will happen later and needs outcome-labelled history. I will finish the diagnosis benchmark first and keep forecasting conditional on suitable data.

**Locations to revisit:** collection/Table 1 pages 5-6; architecture pages 7-11; split page 12; Table 2 page 14; Table 5 page 20; limitations pages 21-23.
