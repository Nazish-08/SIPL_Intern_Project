# Day 18: EasyOCR OCR Fundamentals and First Extraction

## Description

This project introduces Optical Character Recognition (OCR) using EasyOCR. It performs text detection and recognition on license plate and signboard image crops and stores the raw OCR results in JSON format.

## Objective

The objective of this task was to understand the fundamentals of OCR using EasyOCR.

The task focused on:

- Installing and configuring EasyOCR
- Understanding text detection and text recognition
- Understanding bounding boxes
- Understanding OCR confidence scores
- Using language configuration
- Running OCR on CPU
- Processing license plate and signboard images
- Saving OCR results in JSON format

## Dataset

A total of 20 image crops were used:

- 10 license plate images
- 10 signboard images

## Features

- EasyOCR installation and configuration
- English language OCR
- CPU based OCR inference
- Text detection
- Text recognition
- Confidence score extraction
- Bounding box extraction
- License plate OCR
- Signboard OCR
- JSON result generation

## Project Structure

- crops/
- crops/plate/
- crops/signboard/
- ocr_extraction.py
- ocr_results.json
- README.md

## Concepts Used

- EasyOCR
- `easyocr.Reader`
- `readtext()`
- `lang_list`
- `gpu`
- `detail`
- `paragraph`
- Bounding boxes
- OCR confidence
- JSON
- Text detection
- Text recognition

## EasyOCR Configuration

EasyOCR was configured for English language OCR and CPU inference.

```python
reader = easyocr.Reader(
    ["en"],
    gpu=False
)