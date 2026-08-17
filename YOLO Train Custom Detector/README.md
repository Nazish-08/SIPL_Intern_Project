# YOLO Custom Number Plate Detector

## Description

This project fine tunes a pretrained YOLO11n model on a custom vehicle and license plate detection dataset.

The trained model learns to detect:

```text
0: license-plate
1: vehicle
```

## Dataset

```text
Training images:   245
Validation images: 70
Test images:       35
Total images:      350
```

The dataset contains YOLO formatted bounding box annotations.

## Model

```text
Base Model: YOLO11n
Task: Object Detection
Device: CPU
Image Size: 640
Batch Size: 4
Epochs: 20
Patience: 5
```

## Training Process

```text
Pretrained YOLO11n
        ↓
Custom Dataset
        ↓
Training
        ↓
Validation
        ↓
Best Checkpoint
        ↓
best.pt
```

## Training Configuration

The training was performed using:

```python
model.train(
    data="Plate Detection Dataset/data.yaml",
    epochs=20,
    batch=4,
    imgsz=640,
    patience=5,
    device="cpu"
)
```

## Output Files

After training, Ultralytics generated the following artifacts:

```text
runs/
└── plate_detector/
    ├── weights/
    │   ├── best.pt
    │   └── last.pt
    │
    ├── args.yaml
    ├── results.csv
    ├── results.png
    ├── confusion_matrix.png
    ├── labels.jpg
    └── train_batch images
```

## Model Checkpoints

### best.pt

`best.pt` is the best performing checkpoint produced during training.

This model will be used for future inference on new vehicle images and videos.

### last.pt

`last.pt` represents the checkpoint from the final training epoch.

## Training Results

Training metrics are recorded in:

```text
results.csv
```

Training curves are available in:

```text
results.png
```

The confusion matrix is available in:

```text
confusion_matrix.png
```

## Training Batch Visualization

The generated training batch images are used to visually inspect the dataset annotations supplied to the model.

## ANPR Relevance

The trained detector is a component of the ANPR pipeline:

```text
Vehicle Image / CCTV Video
          ↓
YOLO Vehicle Detection
          ↓
License Plate Detection
          ↓
Plate Crop
          ↓
Image Preprocessing
          ↓
OCR
          ↓
Registration Number
```

The current model performs object detection. OCR is a separate stage.

## Learning Outcomes

* Fine tuned a pretrained YOLO model.
* Used a custom annotated dataset.
* Understood epochs and batch size.
* Configured image size and patience.
* Trained using CPU.
* Generated model checkpoints.
* Saved the best model as `best.pt`.
* Recorded training metrics.
* Generated training result plots.
* Generated a confusion matrix.
* Understood the role of checkpoints in YOLO training.