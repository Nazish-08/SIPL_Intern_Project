# Plate Detection Dataset

## Description

This dataset was prepared for number plate and vehicle object detection using the YOLO format.

The dataset contains images with corresponding YOLO annotation files. Two object classes are used:

```text
0: license-plate
1: vehicle
```

## Dataset Structure

```text
Plate Detection Dataset/
│
├── train/
│   ├── images/
│   └── labels/
│
├── val/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
├── data.yaml
├── dataset_quality_checklist.md
└── README.md
```

## Dataset Size

```text
Training images:   245
Validation images: 70
Test images:       35
Total images:      350
```

Each split contains matching image and label files.

## Classes

The dataset contains two classes:

| Class ID | Class |
|---|---|
| 0 | license-plate |
| 1 | vehicle |

## YOLO Annotation Format

Each image has a corresponding `.txt` annotation file.

The annotation format is:

```text
class_id center_x center_y width height
```

The bounding box coordinates are normalized between 0 and 1.

Example:

```text
0 0.6803 0.7945 0.1178 0.0757
```

Here:

```text
0       → license-plate
0.6803  → center X
0.7945  → center Y
0.1178  → box width
0.0757  → box height
```

## Image and Label Matching

Every image should have a corresponding label file with the same filename.

Example:

```text
train/images/example.jpg
train/labels/example.txt
```

This ensures that YOLO can associate the annotation with the correct image.

## Dataset Splitting

The dataset is divided into:

```text
Train → 245 images
Validation → 70 images
Test → 35 images
```

The training set is used for model learning, the validation set is used for evaluation during development, and the test set is reserved for final evaluation.

## Data Leakage

Data leakage can occur when highly similar or duplicate images from the same source appear across training, validation and test sets.

The dataset should therefore be checked for:

* Duplicate images
* Near-duplicate images
* Frames from the same source appearing across different splits
* Test images accidentally included in training data

## Annotation Quality

Annotations should be visually inspected to ensure:

* License plate boxes tightly cover the license plate.
* Vehicle boxes cover the intended vehicle.
* Correct class IDs are used.
* Bounding boxes are not unnecessarily large.
* Bounding boxes are not missing important parts of the target.
* Image and label filenames match.

## Data Configuration

The `data.yaml` file defines the dataset paths and class names.

```yaml
path: .

train: train/images
val: val/images
test: test/images

names:
  0: license-plate
  1: vehicle
```

## ANPR Relevance

This dataset provides the detection foundation for an ANPR pipeline.

The planned workflow is:

```text
Vehicle Image
      ↓
Vehicle Detection
      ↓
License Plate Detection
      ↓
Plate Crop
      ↓
Image Preprocessing
      ↓
OCR
      ↓
Vehicle Registration Number
```

The current dataset is used for object detection. OCR is handled in a later stage of the ANPR workflow.

## Learning Outcome

* Prepared a custom object detection dataset.
* Understood YOLO image and label structure.
* Worked with normalized YOLO bounding box coordinates.
* Defined training, validation and test splits.
* Created a YOLO `data.yaml` configuration.
* Identified potential data leakage.
* Reviewed annotation quality requirements.
* Connected custom object detection datasets with the ANPR pipeline.