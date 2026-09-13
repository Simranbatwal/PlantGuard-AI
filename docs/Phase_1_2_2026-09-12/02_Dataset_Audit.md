# Phase 2 - Tomato dataset preparation and audit

I have downloaded and checked the selected original images. The first release is tomato_v1. The data lists are ready for controlled experiments; model training is the next stage.

## Actual class counts

| Class | Downloaded | Retained | Train | Validation | Internal test |
| --- | --- | --- | --- | --- | --- |
| healthy | 1591 | 1585 | 1111 | 237 | 237 |
| early blight | 1000 | 1000 | 700 | 152 | 148 |
| late blight | 1909 | 1901 | 1331 | 284 | 286 |
| Total | 4500 | 4486 | 3142 | 673 | 671 |

The split targets 70/15/15. Whole related-image groups are kept together, which explains small differences from exact percentages. Per-class metrics will account for the unequal class sizes.

| External PlantDoc class | Downloaded | Retained external test | Excluded |
| --- | --- | --- | --- |
| healthy | 63 | 46 | 17 |
| early blight | 88 | 81 | 7 |
| late blight | 111 | 108 | 3 |
| Total | 262 | 235 | 27 |

PlantDoc is a custom external-only pool. Original train/test folder names are preserved, but none of these selected images is used for our training or threshold selection. This is not a reproduction of the paper's benchmark split.

## Additional cases
- 180 unsupported leaves: 60 apple healthy, 60 potato healthy and 60 tomato Septoria images. Grouped division gives 89 OOD-validation and 91 OOD-test images. This small controlled-background set is a limited unfamiliar-input challenge.
- 90 synthetic degraded images: blur, darkening and low resolution, derived from 15 validation and 15 test parents. Their parent partitions and transformations are saved. They are not new biological observations.
- 24 synthetic non-leaf geometry images, divided 12/12, are software rejection fixtures. They are not a natural non-leaf benchmark. Natural non-leaf photographs remain a later evaluation addition.

## Checks performed
All 4,942 selected original files downloaded successfully, matched the source Git blob hashes and decoded without errors. Their source size is approximately 181.7 MiB.

The audit found 14 excess byte-identical files and 15 excess decoded-pixel-identical files. These overlap and must not be added together. Fifteen repeated pixel copies were excluded, with originals preserved on disk.

Perceptual-hash screening found 84 candidate pairs at Hamming distance up to 6, including horizontal-mirror comparisons. Eleven cross-label or cross-source candidates were visually inspected. Ten were different photos with similar overall shape and were retained. One pair showed the same scene labelled both early and late blight; both files were quarantined. The remaining candidate relations are conservatively kept within the same partition. The full candidate and decision records are saved.

All 262 external thumbnails and a 36-image benchmark sample were visually screened. Twenty-four external images were quarantined for clear format/content issues or uncertain crop/healthy labels. Examples include charts, composites, insufficient leaf detail and suspicious healthy-labelled leaves. No disease labels were silently changed. Visual screening is not expert pathology confirmation.

Final exclusions are 41 originals: 15 duplicate copies, 2 conflicting-label files and 24 visual exclusions. The retained original-image total is 4,901: 4,486 main benchmark, 235 external and 180 unsupported leaves.

## Leaf identities and split checks
Known source leaf metadata matched 2,918 of the 4,500 supported PlantVillage images. The remaining 1,582 have no matched leaf ID in this audit. Known leaf identities and accepted duplicate relations stay together. The retained benchmark contains 2,248 computational groups; these are not 2,248 independently verified plants.

Assertions passed for separation of file hashes, decoded-pixel hashes, known leaf identities and accepted near-duplicate groups across partitions. Saved decisions remove visually rejected false matches from these relations. Missing plant/session identities and imperfect similarity screening limit biological independence claims. Complete field generalisation has not been established.

No augmentation was used to increase the benchmark before splitting. Derived quality cases preserve the parent partition. Model loaders must use the CSV lists and must not scan all files in a directory, because excluded originals remain on disk.

## Sources and version records
**PlantVillage:** https://github.com/spMohanty/PlantVillage-Dataset

Pinned commit: 7f7ecc7e1eaca78107e3affe7cb5abd9427e139a

The author repository's saved README_HF.md declares CC BY-SA 3.0. Source metadata and attribution are retained.

**PlantDoc:** https://github.com/pratikkayal/PlantDoc-Dataset

Pinned commit: 5467f6012d78d1c446145d5f582da6096f852ae8

The repository contains a CC BY 4.0 licence. Its web-collected images include some stock marks; the repository declaration does not individually verify every original owner's permission. Keep this as an attributed academic benchmark and review rights separately before commercial redistribution.

Both snapshots were retrieved on 12 September 2026. The manifest records original names, source URLs, blob hashes, SHA-256, dimensions, labels and original split names. Six source filenames contained Windows-reserved characters. Their safe local names changed, while their source names, contents and URLs remained recorded.

## Frozen split fingerprint
69377f2755d001fe734c4b60d8ebba22d80b82840f0ad1882a069f87c8ce19c4

This identifies image IDs, file hashes, partitions and groups. Every later run must record it. Data changes require a new release/version with a reason.

## Files to use
- manifest.csv: complete decoded-file audit.
- train.csv, validation.csv, test.csv: main image-model lists.
- external_test.csv, ood_validation.csv, ood_test.csv: separate evaluation lists.
- excluded.csv: originals present on disk but not used.
- quality_cases.csv and nonleaf_fixtures.csv: explicitly synthetic fixtures.
- data/sources/visual_review.csv and pair_review.csv: visual decisions.
- tools/data/download.py, audit.py and verify.py: preparation and checks.

Data preparation is complete for the first benchmark. Expert relabelling, new local photos, paired sensor data and prospective field testing remain future work.
