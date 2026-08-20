from pathlib import Path
import json
import tempfile

from PIL import Image
import easyocr


# ============================================================
# 1. FOLDERS
# ============================================================

plate_dir = Path("crops/plate")
signboard_dir = Path("crops/signboard")

output_file = Path("ocr_results.json")


# ============================================================
# 2. CHECK FOLDERS
# ============================================================

if not plate_dir.exists():
    raise FileNotFoundError("Plate folder not found.")

if not signboard_dir.exists():
    raise FileNotFoundError("Signboard folder not found.")


# ============================================================
# 3. FIND IMAGES
# ============================================================

image_extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.webp",
    "*.avif"
]

image_files = []

for extension in image_extensions:
    image_files.extend(plate_dir.glob(extension))
    image_files.extend(signboard_dir.glob(extension))

image_files = sorted(image_files)


if len(image_files) < 20:
    raise ValueError(
        f"At least 20 images required. Found: {len(image_files)}"
    )


print("Images found:", len(image_files))


# ============================================================
# 4. LOAD EASYOCR
# ============================================================

print("\nLoading EasyOCR...")

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

print("EasyOCR loaded successfully.")


# ============================================================
# 5. RUN OCR
# ============================================================

results = []

for image_file in image_files:

    print("\n========================================")
    print("Processing:", image_file.name)
    print("========================================")

    temp_file = None

    try:

        # ----------------------------------------------------
        # AVIF CONVERSION
        # ----------------------------------------------------

        if image_file.suffix.lower() == ".avif":

            print("AVIF detected. Converting to JPEG...")

            image = Image.open(image_file)
            image = image.convert("RGB")

            temp_file = tempfile.NamedTemporaryFile(
                suffix=".jpg",
                delete=False
            )

            image.save(
                temp_file.name,
                format="JPEG"
            )

            temp_file.close()

            ocr_source = temp_file.name

        else:

            ocr_source = str(image_file)


        # ----------------------------------------------------
        # EASY OCR
        # ----------------------------------------------------

        ocr_results = reader.readtext(
            ocr_source,
            detail=1,
            paragraph=False
        )


        # ----------------------------------------------------
        # SAVE DETECTIONS
        # ----------------------------------------------------

        if len(ocr_results) == 0:

            print("No text detected.")

        for detection in ocr_results:

            bbox, text, confidence = detection

            text = text.strip()

            print(
                f"Text: {text} | "
                f"Confidence: {confidence:.2f}"
            )

            results.append({
    "image": image_file.name,
    "category": (
        "plate"
        if image_file.parent.name == "plate"
        else "signboard"
    ),
    "text": text,
    "confidence": round(float(confidence), 4),
    "bbox": [
        [int(point[0]), int(point[1])]
        for point in bbox
    ]
})


    except Exception as error:

        print(
            f"OCR error for {image_file.name}: {error}"
        )


    finally:

        # ----------------------------------------------------
        # DELETE TEMPORARY JPEG
        # ----------------------------------------------------

        if temp_file is not None:

            Path(temp_file.name).unlink(
                missing_ok=True
            )


# ============================================================
# 6. SAVE JSON
# ============================================================

with open(
    output_file,
    "w",
    encoding="utf-8"
) as json_file:

    json.dump(
        results,
        json_file,
        indent=4,
        ensure_ascii=False
    )


# ============================================================
# 7. FINAL OUTPUT
# ============================================================

print("\n========================================")
print("EASYOCR EXTRACTION COMPLETE")
print("========================================")

print("Images processed:", len(image_files))
print("OCR detections:", len(results))
print("Results saved:", output_file)