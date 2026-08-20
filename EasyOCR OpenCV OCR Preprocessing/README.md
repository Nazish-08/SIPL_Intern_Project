
## Day 19 README

```markdown
# Day 19: EasyOCR + OpenCV OCR Preprocessing and Post-Processing

## Description

This project improves OCR performance by preprocessing image inputs using OpenCV and cleaning noisy OCR outputs using text normalization and domain-specific validation rules.

The task compares multiple preprocessing techniques and evaluates their effect on OCR results.

## Objective

The objective of this task was to improve OCR input quality and normalize noisy OCR output.

The task focused on:

- Comparing original and preprocessed images
- Converting images to grayscale
- Improving contrast using CLAHE
- Applying Otsu thresholding
- Running EasyOCR on different preprocessing outputs
- Normalizing OCR text
- Filtering low confidence detections
- Validating Indian license plate patterns
- Comparing OCR predictions with ground truth
- Calculating exact match rate

## Dataset

A total of 20 image crops were used:

- 10 license plate images
- 10 signboard images

## Features

- Original image processing
- Grayscale conversion
- CLAHE contrast enhancement
- Otsu thresholding
- EasyOCR comparison
- OCR confidence filtering
- Text normalization
- Indian license plate validation
- Ground truth comparison
- Exact match evaluation
- JSON report generation

## Project Structure

- crops/
- preprocessing/
- ocr_preprocessing.py
- ocr_comparison.py
- text_cleaning.py
- evaluate_ocr.py
- comparison_report.json
- comparison_evaluation.json
- ground_truth.json
- final_ocr_evaluation.json
- README.md

## Preprocessing Techniques

### Original

The original image is used directly as the OCR input without preprocessing.

### Grayscale

The image is converted into grayscale using OpenCV.

```python
cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)