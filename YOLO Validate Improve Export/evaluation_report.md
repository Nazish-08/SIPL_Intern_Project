# Day 17 Evaluation Report

## Baseline Validation

The trained `best.pt` model was evaluated on the test dataset containing 35 images.

### Baseline Results

| Metric | Result |
|---|---:|
| Precision | 86.25% |
| Recall | 85.87% |
| mAP50 | 81.69% |
| mAP50-95 | 65.14% |

### Class Results

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| License Plate | 97.5% | 86.7% | 84.7% | 66.6% |
| Vehicle | 75.0% | 85.1% | 78.7% | 63.7% |

## Weak Detection Analysis

Low confidence detections below 0.50 were identified as candidate weak cases.

At least 20 weak detection cases were reviewed for further analysis.

Common issues included low confidence detections and difficult detection cases.

## Confidence Threshold Comparison

| Metric | conf=0.25 | conf=0.50 |
|---|---:|---:|
| Precision | 86.25% | 90.20% |
| Recall | 85.87% | 73.98% |
| mAP50 | 81.69% | 70.73% |
| mAP50-95 | 65.14% | 57.38% |

## Threshold Decision

The `0.25` confidence threshold was retained.

Although `conf=0.50` increased precision from 86.25% to 90.20%, it reduced recall from 85.87% to 73.98% and mAP50 from 81.69% to 70.73%.

Therefore, `conf=0.25` provided the better overall validation result.

## ONNX Export

The best trained model was exported to ONNX format.

```text
exported/best.onnx