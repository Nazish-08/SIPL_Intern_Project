from pathlib import Path
import csv
import time

import cv2
from ultralytics import YOLO


# ============================================================
# 1. PATHS
# ============================================================

video_file = Path("videos/cctv.mp4")
output_dir = Path("output")

output_dir.mkdir(exist_ok=True)

output_video = output_dir / "annotated_cctv.mp4"
count_file = Path("frame_counts.csv")


# ============================================================
# 2. CHECK VIDEO
# ============================================================

if not video_file.exists():
    raise FileNotFoundError(
        f"Video not found: {video_file}"
    )


# ============================================================
# 3. LOAD YOLO MODEL
# ============================================================

model = YOLO("yolo11n.pt")

print("========== YOLO MODEL ==========")
print("Pretrained YOLO model loaded successfully.")


# ============================================================
# 4. OPEN VIDEO
# ============================================================

cap = cv2.VideoCapture(str(video_file))

if not cap.isOpened():
    raise RuntimeError(
        "Could not open CCTV video."
    )


# ============================================================
# 5. VIDEO INFORMATION
# ============================================================

fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
)
frame_height = int(
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
)
total_frames = int(
    cap.get(cv2.CAP_PROP_FRAME_COUNT)
)

print("\n========== VIDEO INFORMATION ==========")
print("FPS:", fps)
print("Width:", frame_width)
print("Height:", frame_height)
print("Total Frames:", total_frames)


# ============================================================
# 6. VIDEO WRITER
# ============================================================

fourcc = cv2.VideoWriter_fourcc(
    *"mp4v"
)

video_writer = cv2.VideoWriter(
    str(output_video),
    fourcc,
    fps,
    (frame_width, frame_height)
)

if not video_writer.isOpened():
    cap.release()
    raise RuntimeError(
        "Could not create output video."
    )


# ============================================================
# 7. VEHICLE CLASSES
# ============================================================

vehicle_classes = {
    "car",
    "motorcycle",
    "bus",
    "truck"
}


# ============================================================
# 8. CSV FILE
# ============================================================

csv_file = open(
    count_file,
    "w",
    newline="",
    encoding="utf-8"
)

writer = csv.writer(csv_file)

writer.writerow([
    "frame_number",
    "vehicle_count",
    "processing_time_seconds"
])


# ============================================================
# 9. PROCESS VIDEO
# ============================================================

frame_number = 0
total_processing_time = 0.0

print("\n========== VIDEO PROCESSING ==========")


while True:

    success, frame = cap.read()

    if not success:
        break

    frame_number += 1

    start_time = time.perf_counter()


    # ========================================================
    # YOLO INFERENCE
    # ========================================================

    results = model.predict(
        source=frame,
        conf=0.40,
        imgsz=640,
        device="cpu",
        stream=True,
        verbose=False
    )


    vehicle_count = 0

    annotated_frame = frame.copy()


    # ========================================================
    # PROCESS YOLO RESULT
    # ========================================================

    for result in results:

        boxes = result.boxes

        if boxes is None:
            continue


        for box in boxes:

            class_id = int(
                box.cls[0]
            )

            confidence = float(
                box.conf[0]
            )

            class_name = model.names[
                class_id
            ]


            # Only count vehicles
            if class_name not in vehicle_classes:
                continue


            vehicle_count += 1


            # Bounding box
            x1, y1, x2, y2 = (
                box.xyxy[0]
                .tolist()
            )

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)


            # Draw bounding box
            cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )


            # Label
            label = (
                f"{class_name} "
                f"{confidence:.2f}"
            )


            cv2.putText(
                annotated_frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )


    # ========================================================
    # PROCESSING TIME
    # ========================================================

    processing_time = (
        time.perf_counter()
        - start_time
    )

    total_processing_time += (
        processing_time
    )


    # ========================================================
    # DISPLAY VEHICLE COUNT
    # ========================================================

    cv2.putText(
        annotated_frame,
        f"Vehicles: {vehicle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


    # ========================================================
    # WRITE FRAME TO VIDEO
    # ========================================================

    video_writer.write(
        annotated_frame
    )


    # ========================================================
    # WRITE CSV
    # ========================================================

    writer.writerow([
        frame_number,
        vehicle_count,
        round(processing_time, 6)
    ])


    # ========================================================
    # TERMINAL PROGRESS
    # ========================================================

    if frame_number % 30 == 0:

        print(
            f"Frame {frame_number}/{total_frames} | "
            f"Vehicles: {vehicle_count} | "
            f"Time: {processing_time:.4f}s"
        )


# ============================================================
# 10. RELEASE RESOURCES
# ============================================================

cap.release()
video_writer.release()
csv_file.close()


# ============================================================
# 11. PERFORMANCE
# ============================================================

if total_processing_time > 0:

    processing_fps = (
        frame_number
        / total_processing_time
    )

else:

    processing_fps = 0


# ============================================================
# 12. FINAL REPORT
# ============================================================

print("\n========================================")
print("YOLO VIDEO INFERENCE COMPLETE")
print("========================================")

print(
    "Processed Frames:",
    frame_number
)

print(
    "Total Processing Time:",
    round(
        total_processing_time,
        2
    ),
    "seconds"
)

print(
    "Average Processing FPS:",
    round(
        processing_fps,
        2
    )
)

print(
    "Annotated Video:",
    output_video
)

print(
    "Frame Count CSV:",
    count_file
)