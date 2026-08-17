# YOLO Computer Vision and Detection

## Description

This project demonstrates object detection using a pretrained YOLO model from Ultralytics. Ten different vehicle and traffic images are processed to inspect detected objects, bounding boxes, class labels and confidence scores.

## Workflow

```text
Input Images
     ↓
Image Format Handling
     ↓
Pretrained YOLO Model
     ↓
Object Detection
     ↓
Bounding Boxes
     ↓
Class Labels
     ↓
Confidence Scores
     ↓
Annotated Images + CSV Summary
```

## Features

* Load a pretrained YOLO model
* Process 10 images
* Support multiple image formats
* Detect multiple objects in a single image
* Extract object classes
* Extract confidence scores
* Extract bounding box coordinates
* Generate annotated images
* Export detection results to CSV

## Detected Object Examples

The pretrained model can detect common COCO classes such as:

* Car
* Person
* Motorcycle
* Bus
* Truck
* Bench

## Detection Information

For every detected object, the program records:

```text
Image
Original Format
Class ID
Class Name
Confidence
X1
Y1
X2
Y2
```

## Bounding Boxes

YOLO represents each detected object's bounding box using:

```text
x1, y1, x2, y2
```

These coordinates define the position of the detected object inside the image.

## Confidence

The confidence score represents how confident the model is about a detection.

Example:

```text
car → 0.93
```

This represents a confidence score of approximately 93%.

## IoU

Intersection over Union (IoU) measures the overlap between a predicted bounding box and a ground-truth bounding box.

Higher IoU indicates better overlap between the prediction and the actual object location.

## Precision and Recall

### Precision

Precision measures how many detected positive objects are actually correct.

High precision means fewer false positive detections.

### Recall

Recall measures how many actual objects were successfully detected.

High recall means fewer missed detections.

## Files

```text
YOLO Computer Vision and Detection/
│
├── images/
├── output/
├── yolo_detection.py
├── detections.csv
├── yolo11n.pt
└── README.md
```

## How to Run

```bash
python yolo_detection.py
```

## Output

The program generates annotated images inside the `output` directory and a detection summary in `detections.csv`.

Example:

```text
output/
├── image01_detected.jpg
├── image02_detected.jpg
├── ...
└── image10_detected.jpg
```

## ANPR Relevance

YOLO provides the detection foundation required for an ANPR pipeline.

A future ANPR workflow can use:

```text
Vehicle Image
     ↓
Object Detection
     ↓
Number Plate Detection
     ↓
Plate Crop
     ↓
Image Preprocessing
     ↓
OCR
     ↓
Vehicle Number
```

The pretrained general-purpose YOLO model used in this task is for learning object detection concepts. It is not a dedicated number-plate detection model.

## Learning Outcome

* Learned the YOLO object detection workflow.
* Understood bounding boxes, classes and confidence scores.
* Processed multiple images using a pretrained model.
* Handled different image formats.
* Generated annotated detection images.
* Exported detection results to CSV.
* Understood IoU, precision and recall concepts.
* Connected object detection with the future ANPR pipeline.