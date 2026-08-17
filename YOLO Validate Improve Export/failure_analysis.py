from pathlib import Path
import csv

from ultralytics import YOLO


# ============================================================
# 1. PATHS
# ============================================================

model_path = Path(
    "../YOLO Train Custom Detector/runs/plate_detector/weights/best.pt"
).resolve()

dataset_dir = Path(
    "../Plate Detection Dataset/test/images"
).resolve()

output_dir = Path("failure_analysis").resolve()
output_dir.mkdir(exist_ok=True)


# ============================================================
# 2. CHECK PATHS
# ============================================================

if not model_path.exists():
    raise FileNotFoundError(
        f"Model not found: {model_path}"
    )

if not dataset_dir.exists():
    raise FileNotFoundError(
        f"Test image folder not found: {dataset_dir}"
    )


# ============================================================
# 3. LOAD MODEL
# ============================================================

model = YOLO(str(model_path))

print("========== FAILURE ANALYSIS ==========")
print("Model:", model_path)
print("Test images:", dataset_dir)


# ============================================================
# 4. FIND TEST IMAGES
# ============================================================

image_files = sorted(
    list(dataset_dir.glob("*.jpg"))
    + list(dataset_dir.glob("*.jpeg"))
    + list(dataset_dir.glob("*.png"))
)

if len(image_files) == 0:
    raise FileNotFoundError(
        "No test images found."
    )

print("Test images found:", len(image_files))


# ============================================================
# 5. CSV REPORT
# ============================================================

csv_path = output_dir / "failure_cases.csv"

with open(
    csv_path,
    "w",
    newline="",
    encoding="utf-8"
) as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow([
        "image",
        "status",
        "class",
        "confidence",
        "reason"
    ])


    # ========================================================
    # 6. RUN PREDICTIONS
    # ========================================================

    for image_file in image_files:

        print("\nProcessing:", image_file.name)

        results = model.predict(
            source=str(image_file),
            conf=0.25,
            imgsz=640,
            device="cpu",
            save=True,
            project=str(output_dir),
            name="predictions",
            exist_ok=True,
            verbose=False
        )

        result = results[0]

        boxes = result.boxes


        # ====================================================
        # 7. NO DETECTION
        # ====================================================

        if boxes is None or len(boxes) == 0:

            print("  → No detection")

            writer.writerow([
                image_file.name,
                "weak",
                "none",
                0.0,
                "No object detected"
            ])

            continue


        # ====================================================
        # 8. INSPECT DETECTIONS
        # ====================================================

        for box in boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            class_name = model.names[class_id]

            # -----------------------------------------------
            # Weak detection
            # -----------------------------------------------

            if confidence < 0.50:

                status = "weak"
                reason = "Low confidence"

            else:

                status = "detected"
                reason = "Normal confidence"


            print(
                f"  Class: {class_name} | "
                f"Confidence: {confidence:.2f} | "
                f"Status: {status}"
            )


            writer.writerow([
                image_file.name,
                status,
                class_name,
                round(confidence, 4),
                reason
            ])


# ============================================================
# 9. FINAL MESSAGE
# ============================================================

print("\n========================================")
print("FAILURE ANALYSIS COMPLETE")
print("========================================")

print("CSV report:", csv_path)

print(
    "Prediction images:",
    output_dir / "predictions"
)

print("\nReview the prediction images manually.")
print("Focus on weak detections and missed license plates.")