# YOLO Inference on Video

## Description

This project demonstrates YOLO inference on a CCTV style traffic video. The video is processed frame by frame to detect vehicles, draw bounding boxes, count vehicles per frame and measure inference performance.

## Workflow

```text
CCTV Video
    ↓
Video Frames
    ↓
YOLO Inference
    ↓
Vehicle Detection
    ↓
Bounding Boxes + Confidence
    ↓
Vehicle Count Per Frame
    ↓
Annotated Video
    ↓
Frame Count CSV + Timing
```

## Vehicle Classes

The following vehicle classes are counted:

* Car
* Motorcycle
* Bus
* Truck

Other detected classes are ignored for the vehicle count.

## Inference Configuration

```text
Confidence Threshold: 0.40
Image Size: 640
Device: CPU
Streaming: Enabled
```

## Frame Processing

The program reads the CCTV video frame by frame.

For every frame it:

1. Runs YOLO inference.
2. Identifies detected vehicle classes.
3. Filters detections using the confidence threshold.
4. Draws bounding boxes.
5. Displays the vehicle count.
6. Records frame processing time.
7. Writes the annotated frame to the output video.

## Vehicle Counting

Vehicle counting is performed independently for every frame.

Example:

```text
Frame 1 → 3 vehicles
Frame 2 → 3 vehicles
Frame 3 → 4 vehicles
```

This is frame based detection counting. It does not perform object tracking or unique vehicle counting across frames.

## Performance Measurement

The program records processing time for each frame and calculates average processing FPS.

Example:

```text
Total Processing Time: XX seconds
Average Processing FPS: XX
```

## Output Files

```text
YOLO Inference on Video/
│
├── videos/
│   └── cctv.mp4
│
├── output/
│   └── annotated_cctv.mp4
│
├── video_inference.py
├── frame_counts.csv
└── README.md
```

## CSV Output

The `frame_counts.csv` file contains:

```text
frame_number
vehicle_count
processing_time_seconds
```

## How to Run

```bash
python video_inference.py
```

## ANPR Relevance

Video based YOLO inference is an important component of an ANPR system.

A future ANPR pipeline can process CCTV footage as:

```text
CCTV Video
    ↓
Frame Extraction
    ↓
Vehicle Detection
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

The current implementation performs vehicle detection and frame based counting. It does not perform vehicle tracking or OCR.

## Learning Outcome

* Learned YOLO inference on video.
* Processed video frame by frame.
* Controlled confidence threshold.
* Used image size and device parameters.
* Used streaming inference.
* Counted vehicles per frame.
* Generated annotated video.
* Recorded frame processing time.
* Calculated processing FPS.
* Exported frame level detection statistics.