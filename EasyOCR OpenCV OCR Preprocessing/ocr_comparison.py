from pathlib import Path
import json

import easyocr


# ============================================================
# 1. PATHS
# ============================================================

preprocessing_dir = Path("preprocessing")

output_file = Path("comparison_report.json")


# ============================================================
# 2. PREPROCESSING TYPES
# ============================================================

preprocessing_types = [
    "original",
    "grayscale",
    "clahe",
    "threshold"
]


# ============================================================
# 3. CHECK PREPROCESSING FOLDERS
# ============================================================

for preprocessing_type in preprocessing_types:

    folder = preprocessing_dir / preprocessing_type

    if not folder.exists():
        raise FileNotFoundError(
            f"Folder not found: {folder}"
        )


# ============================================================
# 4. LOAD EASYOCR
# ============================================================

print("========================================")
print("LOADING EASYOCR")
print("========================================")

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

print("EasyOCR loaded successfully.")


# ============================================================
# 5. FIND ORIGINAL IMAGES
# ============================================================

original_dir = preprocessing_dir / "original"

image_files = sorted(
    original_dir.glob("*.jpg")
)

print("\nOriginal images:", len(image_files))


# ============================================================
# 6. OCR COMPARISON
# ============================================================

comparison_results = []


for image_file in image_files:

    print("\n========================================")
    print("IMAGE:", image_file.name)
    print("========================================")

    image_result = {
        "image": image_file.name,
        "methods": {}
    }


    for preprocessing_type in preprocessing_types:

        processed_file = (
            preprocessing_dir /
            preprocessing_type /
            image_file.name
        )

        if not processed_file.exists():

            print(
                f"{preprocessing_type}: file not found"
            )

            continue


        print(
            f"\nProcessing: {preprocessing_type}"
        )


        ocr_results = reader.readtext(
            str(processed_file),
            detail=1,
            paragraph=False
        )


        detections = []


        for detection in ocr_results:

            bbox, text, confidence = detection

            text = text.strip()

            if not text:
                continue


            detections.append({
                "text": text,
                "confidence": round(
                    float(confidence),
                    4
                ),
                "bbox": [
                    [
                        int(point[0]),
                        int(point[1])
                    ]
                    for point in bbox
                ]
            })


            print(
                f"Text: {text} | "
                f"Confidence: {confidence:.2f}"
            )


        image_result["methods"][
            preprocessing_type
        ] = detections


    comparison_results.append(
        image_result
    )


# ============================================================
# 7. SAVE RESULTS
# ============================================================

with open(
    output_file,
    "w",
    encoding="utf-8"
) as json_file:

    json.dump(
        comparison_results,
        json_file,
        indent=4,
        ensure_ascii=False
    )


# ============================================================
# 8. COMPLETE
# ============================================================

print("\n========================================")
print("OCR COMPARISON COMPLETE")
print("========================================")

print(
    "Images compared:",
    len(comparison_results)
)

print(
    "Methods:",
    ", ".join(preprocessing_types)
)

print(
    "Results saved:",
    output_file
)