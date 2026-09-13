# R1 - Controlled images and the external-image gap

**Paper:** Mohanty, Hughes and Salathe (2016), *Using Deep Learning for Image-Based Plant Disease Detection*. Frontiers in Plant Science 7:1419. DOI: https://doi.org/10.3389/fpls.2016.01419
**Reading record:** Full paper downloaded and examined, including methods, results, Table 1 and discussion. The findings below are published results, not my model results.

## Problem and previous work
The paper asks whether a deep image model can identify crop species and disease from leaf photographs. Earlier systems often needed hand-designed colour, shape or texture features. This study tests learning the visual features directly from images.

## Data and method
The authors used 54,306 PlantVillage images covering 38 crop-condition categories from 14 crops. They compared AlexNet and GoogLeNet, training from scratch and transfer learning, and colour, grayscale and segmented images. Images were resized to 256 by 256 pixels. Five training/test proportions, from 20/80 to 80/20, were investigated. The methods keep different views of the same leaf in the same partition. Training lasted 30 epochs; the paper describes SGD and reports precision, recall, F1 and overall accuracy.

Transfer learning means starting with a network that has already learnt general visual features. Segmentation here removes the background; it does not automatically provide a lesion-severity measurement. The many experiment combinations help distinguish the influence of the architecture, image representation and training-set size.

## Reported results and their context
The best colour/transfer-learning GoogLeNet configuration at 80/20 achieved 99.35% accuracy and about 0.9934 mean F1 (Table 1). On two separately collected external sets of 121 and 119 images, the best configurations reached only 31.40% and 31.69% accuracy respectively (results, page 7). These are different-condition, 38-class tests. They must not be compared directly with a future three-class tomato experiment as if the tasks were identical.

## Limitations and my assessment
The authors discuss controlled backgrounds, single leaves and reduced performance outside the source conditions. The external sets are small. A visual classification is also different from laboratory confirmation and cannot establish when infection began. The results show feasibility, but do not justify a promise of 99% field accuracy.

My main lesson is to examine what the test set actually represents. A random image split can be too easy if related views cross partitions. I will therefore use source leaf identities, duplicate groups and separate external images. I will report macro-F1 and per-class recall alongside accuracy because class sizes differ.

## Connection to PlantGuard
I will use only the original colour tomato images for the first benchmark. Healthy, early blight and late blight form the three supported labels. The four selected modern architectures will share the same frozen split. I will not add grayscale or segmented copies of the same photograph as independent samples. The proposed contribution is an evaluated reliability workflow around classification, not the invention of leaf-image classification.

**Guide answer:** This paper showed that CNN classification works well on controlled images, but performance dropped on different photos. My evaluation will therefore include both an internal test and a separate external test.

**Locations to revisit:** Methods pages 2-4; Table 1 and external results page 7; limitations pages 8-9.
