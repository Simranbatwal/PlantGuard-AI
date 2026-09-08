# AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN

System: PlantGuard

Simran Batwal | Roll number: 28452500003

M.Tech | Computer Science | 3rd Semester

Guru Nanak Dev University, Amritsar

Guide: Dr. Anil Kumar

8 September 2026 | Initial-stage proposal


# PlantGuard: guide review summary


**AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**

Simran Batwal | M.Tech, Computer Science | 3rd Semester

Guru Nanak Dev University, Amritsar | Roll no.: 28452500003

## Current stage
Topic discussion, initial planning and some preliminary reading. Dataset download / audit and coding are planned after scope review. No trained-model or experimental results are claimed.

## Proposed college prototype
Two tomato pots; two ESP32 Wi-Fi nodes; capacitive soil probes, SHT31 sensors and genuine leaf-wetness plates. Phone / USB camera provides close-up leaf images. Existing laptop runs the AI, database and dashboard.

**Flow:** two sensing nodes -> local Wi-Fi -> laptop AI, database and dashboard.

## Research focus for guide review
Compare image-only, simple contextual and quality-aware decision policies. Evaluate whether bounded fresh observations improve reliability under uncertain images or faulty / missing sensor data. Learned fusion needs paired labels; forecasting needs independent time-labelled disease events.

## Scope and evidence
Tomato-first integration; four image-model comparisons. Report macro-F1, class recall, accepted-case error / coverage, unknown handling, telemetry gaps and latency. Other crops, severity and continual learning are data-dependent extensions.

## Resources and next 30 days
Indicative physical budget: **INR 18,150 + INR 3,630 reserve = INR 21,780**. Reuse laptop / network / tools. Next: agree scope, read core papers, audit data, calibrate first node and demonstrate two-node wireless logging.

## Guide decisions requested
Research question, dataset / labelling support, hardware configuration, deferred features and next review date. Market continuation, if later pursued, will run main AI on VPS/cloud.

Guide: Dr. Anil Kumar | Review date: __________    Next meeting: ____________________

