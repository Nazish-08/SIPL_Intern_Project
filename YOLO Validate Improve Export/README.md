# YOLO Validate, Improve and Export

## Description

Validated the custom YOLO11n number plate detector using the test dataset, analyzed weak detections, compared confidence thresholds, and exported the trained model to ONNX format.

## Baseline Validation

Test dataset:

- 35 images
- 112 annotated instances

Results:

- Precision: 86.25%
- Recall: 85.87%
- mAP50: 81.69%
- mAP50-95: 65.14%

## Class Performance

### License Plate

- Precision: 97.5%
- Recall: 86.7%
- mAP50: 84.7%
- mAP50-95: 66.6%

### Vehicle

- Precision: 75.0%
- Recall: 85.1%
- mAP50: 78.7%
- mAP50-95: 63.7%

## Weak Detection Analysis

Low confidence detections below 0.50 were identified as candidate weak cases.

More than 20 weak detection cases were reviewed using the generated prediction images and CSV report.

## Confidence Threshold Comparison

| Metric | conf=0.25 | conf=0.50 |
|---|---:|---:|
| Precision | 86.25% | 90.20% |
| Recall | 85.87% | 73.98% |
| mAP50 | 81.69% | 70.73% |
| mAP50-95 | 65.14% | 57.38% |

## Final Decision

The confidence threshold of 0.25 was retained.

Although 0.50 increased precision, it significantly reduced recall and mAP. Therefore, 0.25 provided the better overall result for the detector.

## ONNX Export

The trained `best.pt` model was exported to ONNX format.

```text
exported/best.onnx