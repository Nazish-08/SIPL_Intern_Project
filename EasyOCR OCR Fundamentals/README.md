# Day 18: EasyOCR OCR Fundamentals and First Extraction

## 1. Objective

The objective of this task was to understand the fundamentals of Optical Character Recognition (OCR) using EasyOCR and perform the first text extraction experiments.

The task focused on:

- Installing and configuring EasyOCR
- Understanding text detection and text recognition
- Understanding bounding boxes
- Understanding OCR confidence scores
- Using language configuration
- Running OCR on CPU
- Processing license plate and signboard images
- Saving raw OCR results in JSON format

---

## 2. Environment

### Software

- Python 3
- EasyOCR
- Pillow
- JSON
- PyTorch

### Hardware

- CPU inference
- GPU disabled

EasyOCR was configured with:

```python
reader = easyocr.Reader(
    ["en"],
    gpu=False
)