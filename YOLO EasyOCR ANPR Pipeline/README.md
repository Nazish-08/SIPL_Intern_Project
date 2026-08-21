# Day 20: YOLO + EasyOCR ANPR Pipeline

## Description

This project integrates YOLO license plate detection with EasyOCR and OpenCV to create an end-to-end Automatic Number Plate Recognition (ANPR) pipeline.

The pipeline detects license plate regions, safely crops the detected regions, preprocesses the crops, performs OCR, normalizes the extracted text, validates Indian license plate patterns, and stores structured results in JSON and CSV format.

## Objective

The objective of this task was to combine the previously developed YOLO and OCR components into a single reusable ANPR pipeline.

The pipeline performs:

- License plate detection using YOLO
- Safe bounding box cropping
- OpenCV preprocessing
- EasyOCR text extraction
- OCR confidence calculation
- Text normalization
- Indian license plate validation
- Timestamp generation
- Structured JSON output
- Structured CSV output
- Annotated image generation
- Basic error handling

## Dataset

A total of 5 vehicle images were processed.

The input images are stored in:

```text
input/
├── vehicle01.jpg
├── vehicle02.jpg
├── vehicle03.jpg
├── vehicle04.jpg
└── vehicle05.jpg