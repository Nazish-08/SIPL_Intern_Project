# Evaluation Packaging and Demonstration

## Description

This project represents the final capstone evaluation and demonstration of the ANPR pipeline.

The system evaluates vehicle images captured under different conditions such as daytime, nighttime and different viewing angles.

The pipeline combines YOLO based detection with EasyOCR based number plate text recognition and evaluates the end-to-end OCR results against available ground truth values.

## Evaluation Dataset

The evaluation dataset contains 15 vehicle images.

```text
Evaluation Dataset

├── Day
│   └── 5 images
│
├── Night
│   └── 5 images
│
└── Angle
    └── 5 images
```

Total:

```text
15 images
```

## Dataset Conditions

The system is evaluated on:

* Day images
* Night images
* Different angle images

The purpose is to evaluate the pipeline under different visual conditions.

## ANPR Pipeline

```text
Input Vehicle Image
        ↓
YOLO Detection
        ↓
Bounding Box
        ↓
Safe Crop
        ↓
EasyOCR
        ↓
Text Normalization
        ↓
Ground Truth Comparison
        ↓
Exact Match Evaluation
        ↓
JSON Results
        ↓
Metrics Report
```

## Models

The project uses:

```text
YOLO
EasyOCR
```

The trained number plate detection model is stored in:

```text
models/plate_detector_best.pt
```

The YOLO model configuration used by the evaluation script is:

```text
yolo11n.pt
```

## Evaluation Configuration

```text
Confidence Threshold: 0.40
OCR Device: CPU
Image Types: JPG, JPEG, PNG, WEBP, AVIF
```

## Evaluation Process

For every image the program:

1. Loads the image.
2. Runs YOLO inference.
3. Extracts detected bounding boxes.
4. Crops detected regions.
5. Sends crops to EasyOCR.
6. Normalizes OCR text.
7. Compares the prediction with ground truth when available.
8. Records OCR confidence.
9. Measures processing time.
10. Saves structured results.

## Ground Truth

Ground truth values are available for 6 of the 15 evaluation images.

The remaining 9 images do not currently have ground truth values.

Therefore, the exact match metric is calculated only on the 6 images with available ground truth.

## Evaluation Results

The final evaluation produced:

```text
Total Images       : 15
Evaluated Images   : 6
Exact Matches      : 0
Exact Match Rate   : 0.0%
Average Time       : 2.6758 seconds
Average FPS        : 0.37
```

The results are stored in:

```text
results/capstone_results.json
results/capstone_metrics.json
```

## Result Structure

Each image result contains:

```text
image
ground_truth
prediction
ocr_confidence
detections
exact_match
detection_time_seconds
ocr_time_seconds
total_time_seconds
```

## Performance Measurement

The system records processing time for each image.

The following metrics are calculated:

* Total images
* Evaluated images
* Exact matches
* Exact match rate
* Average processing time
* Average FPS

## Testing

Pytest is used to validate the evaluation outputs and utility functions.

Test command:

```bash
pytest tests\test_evaluation.py -v
```

Test result:

```text
7 passed
```

The tests verify:

* Text normalization
* Results file existence
* Metrics file existence
* Results structure
* Metrics structure
* Total image count
* Metric value ranges

## Demonstration

The project includes a demonstration script.

Run:

```bash
python demo\run_demo.py
```

The demonstration displays:

* Total images
* Evaluated images
* Exact matches
* Exact match rate
* Average processing time
* Average FPS
* Individual image predictions
* OCR confidence
* Detection count
* Exact match status

## Project Structure

```text
Evaluation Packaging and Demonstration/
│
├── data/
│   ├── day/
│   ├── night/
│   └── angle/
│
├── models/
│   └── plate_detector_best.pt
│
├── results/
│   ├── capstone_results.json
│   └── capstone_metrics.json
│
├── tests/
│   └── test_evaluation.py
│
├── demo/
│   └── run_demo.py
│
├── evaluate_capstone.py
├── ground_truth.json
└── README.md
```

## Limitations

The current evaluation shows an exact match rate of 0.0% on the 6 images with available ground truth.

The main limitations are:

* OCR predictions do not consistently match the ground truth.
* Some images produce empty OCR results.
* Some OCR predictions contain incorrect characters.
* Low OCR confidence occurs on difficult images.
* Night images can be difficult for OCR.
* Different viewing angles can reduce recognition accuracy.
* CPU based inference results in low processing speed.
* Only 6 images currently have ground truth values.
* The evaluation does not represent a large production dataset.

## Failure Analysis

Examples from the evaluation include incorrect OCR predictions such as:

```text
Ground Truth: MP04CC2688
Prediction:    MHZODV23661
```

```text
Ground Truth: MH20DV2366
Prediction:    MH14BR6899
```

```text
Ground Truth: MH14BR6899
Prediction:    MP04CC2688
```

```text
Ground Truth: DL3CAW2927
Prediction:    IND
```

These results show that the current pipeline requires further improvement before production deployment.

## Future Improvements

Possible improvements include:

* Improve number plate detection accuracy.
* Increase the size and diversity of the training dataset.
* Add more ground truth samples.
* Improve image preprocessing.
* Apply plate specific preprocessing before OCR.
* Improve OCR configuration.
* Test alternative OCR models.
* Add vehicle and plate tracking.
* Evaluate day and night performance separately.
* Generate a failure gallery.
* Improve CPU inference performance.
* Add a CLI interface.
* Package the project with requirements and configuration files.

## Reproducibility

The evaluation can be reproduced using:

```bash
python evaluate_capstone.py
```

Tests can be executed using:

```bash
pytest tests\test_evaluation.py -v
```

The demonstration can be executed using:

```bash
python demo\run_demo.py
```

## Learning Outcome

This capstone demonstrates:

* End-to-end ANPR pipeline integration.
* YOLO based detection.
* Bounding box extraction.
* Image cropping.
* EasyOCR integration.
* OCR text normalization.
* Ground truth comparison.
* Exact match evaluation.
* Processing time measurement.
* FPS calculation.
* JSON based result storage.
* Automated testing using pytest.
* Demonstration and evaluation packaging.
* Identification of system limitations and future improvements.