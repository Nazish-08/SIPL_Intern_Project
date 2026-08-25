from pathlib import Path
import json
import re
import time

from ultralytics import YOLO
import easyocr


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"
GROUND_TRUTH_FILE = BASE_DIR / "ground_truth.json"

RESULTS_DIR.mkdir(exist_ok=True)


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "models/plate_detector_best.pt"

CONFIDENCE_THRESHOLD = 0.40

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".avif"
}


# ============================================================
# MODELS
# ============================================================

print("Loading YOLO model...")

model = YOLO(MODEL_PATH)

print("Loading EasyOCR...")

reader = easyocr.Reader(
    ["en"],
    gpu=False
)


# ============================================================
# LOAD GROUND TRUTH
# ============================================================

with open(
    GROUND_TRUTH_FILE,
    "r",
    encoding="utf-8"
) as file:

    ground_truth = json.load(file)


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text: str) -> str:

    text = text.upper()

    text = re.sub(
        r"[^A-Z0-9]",
        "",
        text
    )

    return text


# ============================================================
# PROCESS IMAGE
# ============================================================

def process_image(
    image_path: Path,
    relative_path: str
):

    start_time = time.perf_counter()

    results = model.predict(
        source=str(image_path),
        conf=CONFIDENCE_THRESHOLD,
        verbose=False
    )

    detection_time = time.perf_counter()

    detections = []

    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            coordinates = box.xyxy[0].tolist()

            x1, y1, x2, y2 = map(
                int,
                coordinates
            )

            confidence = float(
                box.conf[0]
            )

            detections.append(
                {
                    "box": {
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2
                    },
                    "detection_confidence": round(
                        confidence,
                        4
                    )
                }
            )

    ocr_time_start = time.perf_counter()

    ocr_results = []

    for detection in detections:

        box = detection["box"]

        x1 = max(0, box["x1"])
        y1 = max(0, box["y1"])
        x2 = max(x1, box["x2"])
        y2 = max(y1, box["y2"])

        crop = results[0].orig_img[
            y1:y2,
            x1:x2
        ]

        if crop.size == 0:
            continue

        ocr_output = reader.readtext(
            crop
        )

        for item in ocr_output:

            text = item[1]

            confidence = float(
                item[2]
            )

            normalized = normalize_text(
                text
            )

            if normalized:

                ocr_results.append(
                    {
                        "text": normalized,
                        "ocr_confidence": round(
                            confidence,
                            4
                        )
                    }
                )

    ocr_time = (
        time.perf_counter()
        - ocr_time_start
    )

    total_time = (
        time.perf_counter()
        - start_time
    )

    prediction = ""

    prediction_confidence = 0.0

    if ocr_results:

        best_result = max(
            ocr_results,
            key=lambda item: item[
                "ocr_confidence"
            ]
        )

        prediction = best_result["text"]

        prediction_confidence = best_result[
            "ocr_confidence"
        ]

    expected = ground_truth.get(
        relative_path
    )

    exact_match = False

    if expected is not None:

        exact_match = (
            normalize_text(expected)
            == prediction
        )

    return {
        "image": relative_path,
        "ground_truth": expected,
        "prediction": prediction,
        "ocr_confidence": prediction_confidence,
        "detections": len(detections),
        "exact_match": exact_match,
        "detection_time_seconds": round(
            detection_time - start_time,
            4
        ),
        "ocr_time_seconds": round(
            ocr_time,
            4
        ),
        "total_time_seconds": round(
            total_time,
            4
        )
    }


# ============================================================
# RUN EVALUATION
# ============================================================

results = []

print("\nStarting capstone evaluation...\n")


for category in [
    "day",
    "night",
    "angle"
]:

    category_dir = DATA_DIR / category

    image_files = sorted(
        [
            file
            for file in category_dir.iterdir()
            if file.is_file()
            and file.suffix.lower()
            in SUPPORTED_EXTENSIONS
        ]
    )

    for image_path in image_files:

        relative_path = (
            f"{category}/{image_path.name}"
        )

        print(
            "Processing:",
            relative_path
        )

        result = process_image(
            image_path,
            relative_path
        )

        results.append(result)


# ============================================================
# METRICS
# ============================================================

evaluated_results = [
    result
    for result in results
    if result["ground_truth"] is not None
]

exact_matches = sum(
    result["exact_match"]
    for result in evaluated_results
)

total_evaluated = len(
    evaluated_results
)

exact_match_rate = 0.0

if total_evaluated > 0:

    exact_match_rate = (
        exact_matches
        / total_evaluated
    ) * 100


total_time = sum(
    result["total_time_seconds"]
    for result in results
)

average_time = 0.0

if results:

    average_time = (
        total_time
        / len(results)
    )

fps = 0.0

if average_time > 0:

    fps = 1 / average_time


metrics = {
    "total_images": len(results),
    "evaluated_images": total_evaluated,
    "exact_matches": exact_matches,
    "exact_match_rate_percent": round(
        exact_match_rate,
        2
    ),
    "average_processing_time_seconds": round(
        average_time,
        4
    ),
    "average_fps": round(
        fps,
        2
    )
}


# ============================================================
# SAVE RESULTS
# ============================================================

with open(
    RESULTS_DIR / "capstone_results.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4
    )


with open(
    RESULTS_DIR / "capstone_metrics.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        metrics,
        file,
        indent=4
    )


# ============================================================
# FINAL REPORT
# ============================================================

print("\n========================================")
print("CAPSTONE EVALUATION COMPLETE")
print("========================================")

print(
    "Total Images       :",
    metrics["total_images"]
)

print(
    "Evaluated Images   :",
    metrics["evaluated_images"]
)

print(
    "Exact Matches      :",
    metrics["exact_matches"]
)

print(
    "Exact Match Rate   :",
    f'{metrics["exact_match_rate_percent"]}%'
)

print(
    "Average Time       :",
    f'{metrics["average_processing_time_seconds"]} seconds'
)

print(
    "Average FPS        :",
    metrics["average_fps"]
)

print(
    "\nResults saved to:",
    RESULTS_DIR
)