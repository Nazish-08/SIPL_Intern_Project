from pathlib import Path
import csv

import numpy as np
from PIL import Image, UnidentifiedImageError
from ultralytics import YOLO


# ============================================================
# 1. FOLDERS
# ============================================================

input_dir = Path("images")
output_dir = Path("output")

output_dir.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD PRETRAINED YOLO MODEL
# ============================================================

model = YOLO("yolo11n.pt")

print("========== YOLO MODEL ==========")
print("Pretrained YOLO model loaded successfully.")


# ============================================================
# 3. FIND ALL IMAGE FILES
# ============================================================

supported_extensions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".avif",
    ".bmp",
    ".tif",
    ".tiff"
}

all_files = sorted(input_dir.iterdir())

image_files = [
    file
    for file in all_files
    if file.is_file()
    and file.suffix.lower() in supported_extensions
]


if len(image_files) == 0:
    raise FileNotFoundError(
        "No supported image files found inside the images folder."
    )


print("\nImages found:", len(image_files))


# ============================================================
# 4. CHECK AT LEAST 10 IMAGES
# ============================================================

if len(image_files) < 10:
    raise ValueError(
        f"Day 13 requires at least 10 images. "
        f"Only {len(image_files)} images were found."
    )

image_files = image_files[:10]

print("Images selected for detection:")

for image_file in image_files:
    print("-", image_file.name)


# ============================================================
# 5. CSV FILE
# ============================================================

csv_file = open(
    "detections.csv",
    "w",
    newline="",
    encoding="utf-8"
)

writer = csv.writer(csv_file)

writer.writerow([
    "image",
    "original_format",
    "class_id",
    "class_name",
    "confidence",
    "x1",
    "y1",
    "x2",
    "y2"
])


# ============================================================
# 6. PROCESS 10 IMAGES
# ============================================================

processed_count = 0


for image_file in image_files:

    print("\n========================================")
    print("Processing:", image_file.name)
    print("========================================")

    try:

        # ====================================================
        # LOAD IMAGE USING PIL
        # ====================================================

        with Image.open(image_file) as pil_image:

            original_format = pil_image.format
            image_size = pil_image.size

            print("Actual format:", original_format)
            print("Image size:", image_size)

            # Convert every image to RGB
            # This allows JPG, PNG, WEBP, AVIF etc.
            rgb_image = pil_image.convert("RGB")

            # Convert PIL image to NumPy array
            image_array = np.array(rgb_image)


    except (UnidentifiedImageError, OSError) as error:

        print(
            f"Could not read image: {image_file.name}"
        )

        print("Reason:", error)

        continue


    # ========================================================
    # 7. RUN YOLO
    # ========================================================

    results = model.predict(
        source=image_array,
        conf=0.25,
        verbose=False
    )


    if not results:

        print("No YOLO result returned.")

        continue


    result = results[0]

    boxes = result.boxes


    # ========================================================
    # 8. SAVE ANNOTATED IMAGE
    # ========================================================

    annotated_image = result.plot()

    output_file = (
        output_dir
        / f"{image_file.stem}_detected.jpg"
    )

    Image.fromarray(
        annotated_image[:, :, ::-1]
    ).save(
        output_file,
        "JPEG",
        quality=95
    )

    print(
        "Annotated image saved:",
        output_file
    )


    # ========================================================
    # 9. CHECK DETECTIONS
    # ========================================================

    if boxes is None or len(boxes) == 0:

        print("No objects detected.")

        processed_count += 1

        continue


    # ========================================================
    # 10. READ DETECTION INFORMATION
    # ========================================================

    for box in boxes:

        class_id = int(
            box.cls[0]
        )

        confidence = float(
            box.conf[0]
        )

        coordinates = (
            box.xyxy[0]
            .tolist()
        )

        x1, y1, x2, y2 = coordinates

        class_name = model.names[
            class_id
        ]


        print(
            f"Class: {class_name} | "
            f"Confidence: {confidence:.2f} | "
            f"Box: "
            f"({x1:.1f}, {y1:.1f}, "
            f"{x2:.1f}, {y2:.1f})"
        )


        # ====================================================
        # SAVE DETECTION TO CSV
        # ====================================================

        writer.writerow([
            image_file.name,
            original_format,
            class_id,
            class_name,
            round(confidence, 4),
            round(x1, 2),
            round(y1, 2),
            round(x2, 2),
            round(y2, 2)
        ])


    processed_count += 1


# ============================================================
# 11. CLOSE CSV
# ============================================================

csv_file.close()


# ============================================================
# 12. FINAL OUTPUT
# ============================================================

print("\n========================================")
print("YOLO DETECTION COMPLETE")
print("========================================")

print(
    "Successfully processed:",
    processed_count,
    "of",
    len(image_files),
    "images"
)

print(
    "Detection summary:",
    "detections.csv"
)

print(
    "Annotated images saved inside:",
    output_dir
)