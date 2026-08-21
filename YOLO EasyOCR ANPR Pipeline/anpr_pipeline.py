from pathlib import Path
from datetime import datetime
import csv
import json
import re

import cv2
import easyocr
from ultralytics import YOLO


# ============================================================
# 1. PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

model_path = (
    BASE_DIR
    / "../YOLO Train Custom Detector/runs/plate_detector/weights/best.pt"
).resolve()

input_dir = BASE_DIR / "input"
output_dir = BASE_DIR / "output"
crop_dir = BASE_DIR / "crops"
results_dir = BASE_DIR / "results"

json_file = results_dir / "anpr_results.json"
csv_file = results_dir / "anpr_results.csv"


# ============================================================
# 2. CREATE FOLDERS
# ============================================================

output_dir.mkdir(exist_ok=True)
crop_dir.mkdir(exist_ok=True)
results_dir.mkdir(exist_ok=True)


# ============================================================
# 3. CHECK PATHS
# ============================================================

if not model_path.exists():
    raise FileNotFoundError(
        f"YOLO model not found: {model_path}"
    )

if not input_dir.exists():
    raise FileNotFoundError(
        f"Input folder not found: {input_dir}"
    )


# ============================================================
# 4. LOAD YOLO
# ============================================================

print("========================================")
print("LOADING YOLO MODEL")
print("========================================")

model = YOLO(str(model_path))

print("Model loaded:")
print(model_path)


# ============================================================
# 5. LOAD EASYOCR
# ============================================================

print("\n========================================")
print("LOADING EASYOCR")
print("========================================")

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

print("EasyOCR loaded successfully.")


# ============================================================
# 6. HELPER FUNCTIONS
# ============================================================

def safe_crop(image, x1, y1, x2, y2):
    """
    Crop an image using safe image boundaries.
    """

    height, width = image.shape[:2]

    x1 = max(0, min(int(x1), width - 1))
    y1 = max(0, min(int(y1), height - 1))
    x2 = max(0, min(int(x2), width))
    y2 = max(0, min(int(y2), height))

    if x2 <= x1 or y2 <= y1:
        return None

    return image[y1:y2, x1:x2]


def preprocess_plate(image):
    """
    Apply grayscale and CLAHE preprocessing.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    return enhanced


def clean_text(text):
    """
    Normalize OCR text.
    """

    text = text.upper()

    text = re.sub(
        r"[^A-Z0-9]",
        "",
        text
    )

    return text


def is_valid_indian_plate(text):
    """
    Validate a common Indian license plate pattern.
    """

    pattern = r"^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$"

    return bool(
        re.fullmatch(pattern, text)
    )


# ============================================================
# 7. FIND INPUT IMAGES
# ============================================================

image_extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.webp"
]

image_files = []

for extension in image_extensions:
    image_files.extend(
        input_dir.glob(extension)
    )

image_files = sorted(image_files)

if not image_files:
    raise FileNotFoundError(
        "No input images found."
    )

print("\nImages found:", len(image_files))


# ============================================================
# 8. PROCESS IMAGES
# ============================================================

all_results = []

for image_file in image_files:

    print("\n========================================")
    print("PROCESSING:", image_file.name)
    print("========================================")

    image = cv2.imread(
        str(image_file)
    )

    if image is None:
        print("Could not read image.")
        continue

    # --------------------------------------------------------
    # YOLO DETECTION
    # --------------------------------------------------------

    results = model.predict(
        source=image,
        conf=0.25,
        verbose=False
    )

    detection_count = 0

    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            detection_count += 1

            # ------------------------------------------------
            # GET BOUNDING BOX
            # ------------------------------------------------

            x1, y1, x2, y2 = (
                box.xyxy[0]
                .cpu()
                .numpy()
            )

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            detection_confidence = float(
                box.conf[0]
                .cpu()
                .item()
            )

            # ------------------------------------------------
            # SAFE CROP
            # ------------------------------------------------

            plate_crop = safe_crop(
                image,
                x1,
                y1,
                x2,
                y2
            )

            if plate_crop is None:
                print("Invalid crop. Skipping.")
                continue

            crop_name = (
                f"{image_file.stem}"
                f"_plate_{detection_count}.jpg"
            )

            crop_path = crop_dir / crop_name

            cv2.imwrite(
                str(crop_path),
                plate_crop
            )

            # ------------------------------------------------
            # PREPROCESS
            # ------------------------------------------------

            processed_crop = preprocess_plate(
                plate_crop
            )

            # ------------------------------------------------
            # OCR
            # ------------------------------------------------

            ocr_results = reader.readtext(
                processed_crop,
                detail=1,
                paragraph=False
            )

            best_text = ""
            best_ocr_confidence = 0.0

            for detection in ocr_results:

                bbox, text, ocr_confidence = detection

                ocr_confidence = float(
                    ocr_confidence
                )

                cleaned = clean_text(text)

                if (
                    cleaned
                    and ocr_confidence
                    > best_ocr_confidence
                ):
                    best_text = cleaned
                    best_ocr_confidence = (
                        ocr_confidence
                    )

            # ------------------------------------------------
            # PLATE VALIDATION
            # ------------------------------------------------

            valid_plate = is_valid_indian_plate(
                best_text
            )

            # ------------------------------------------------
            # TIMESTAMP
            # ------------------------------------------------

            timestamp = datetime.now().isoformat(
                timespec="seconds"
            )

            # ------------------------------------------------
            # STRUCTURED RESULT
            # ------------------------------------------------

            record = {
                "image": image_file.name,
                "timestamp": timestamp,
                "text": best_text,
                "ocr_confidence": round(
                    best_ocr_confidence,
                    4
                ),
                "detection_confidence": round(
                    detection_confidence,
                    4
                ),
                "box": {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                },
                "crop": crop_name,
                "valid_plate": valid_plate
            }

            all_results.append(record)

            # ------------------------------------------------
            # ANNOTATED IMAGE
            # ------------------------------------------------

            label = (
                f"{best_text} "
                f"{best_ocr_confidence:.2f}"
            )

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                label,
                (x1, max(25, y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            print(
                f"Plate: {best_text} | "
                f"OCR Confidence: "
                f"{best_ocr_confidence:.2f} | "
                f"Valid: {valid_plate}"
            )

    # --------------------------------------------------------
    # SAVE ANNOTATED IMAGE
    # --------------------------------------------------------

    output_path = (
        output_dir
        / f"{image_file.stem}_annotated.jpg"
    )

    cv2.imwrite(
        str(output_path),
        image
    )


# ============================================================
# 9. SAVE JSON
# ============================================================

with open(
    json_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_results,
        file,
        indent=4,
        ensure_ascii=False
    )


# ============================================================
# 10. SAVE CSV
# ============================================================

fieldnames = [
    "image",
    "timestamp",
    "text",
    "ocr_confidence",
    "detection_confidence",
    "box",
    "crop",
    "valid_plate"
]

with open(
    csv_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for record in all_results:

        csv_record = record.copy()

        csv_record["box"] = json.dumps(
            record["box"]
        )

        writer.writerow(
            csv_record
        )


# ============================================================
# 11. FINAL OUTPUT
# ============================================================

print("\n========================================")
print("ANPR PIPELINE COMPLETE")
print("========================================")

print("Images processed:", len(image_files))
print("Plate detections:", len(all_results))

print("\nAnnotated images:")
print(output_dir)

print("\nCropped plates:")
print(crop_dir)

print("\nJSON results:")
print(json_file)

print("\nCSV results:")
print(csv_file)