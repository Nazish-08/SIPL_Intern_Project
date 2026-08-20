from pathlib import Path

import cv2
import numpy as np
from PIL import Image


# ============================================================
# 1. PATHS
# ============================================================

plate_dir = Path("crops/plate")
signboard_dir = Path("crops/signboard")

output_dir = Path("preprocessing")

output_dir.mkdir(exist_ok=True)


# ============================================================
# 2. IMAGE EXTENSIONS
# ============================================================

image_extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.webp",
    "*.avif"
]


# ============================================================
# 3. FIND IMAGES
# ============================================================

image_files = []

for extension in image_extensions:
    image_files.extend(plate_dir.glob(extension))
    image_files.extend(signboard_dir.glob(extension))

image_files = sorted(image_files)

print("Images found:", len(image_files))


# ============================================================
# 4. PROCESS EACH IMAGE
# ============================================================

for image_file in image_files:

    print("\n========================================")
    print("Processing:", image_file.name)
    print("========================================")

    # --------------------------------------------------------
    # READ IMAGE
    # --------------------------------------------------------

    if image_file.suffix.lower() == ".avif":

        try:
            pil_image = Image.open(image_file)
            pil_image = pil_image.convert("RGB")

            image = np.array(pil_image)

            image = cv2.cvtColor(
                image,
                cv2.COLOR_RGB2BGR
            )

            print("AVIF image converted successfully.")

        except Exception as error:

            print(
                f"Could not read AVIF image: {error}"
            )

            continue

    else:

        image = cv2.imread(
            str(image_file)
        )

    if image is None:

        print(
            "Could not read:",
            image_file.name
        )

        continue


    # --------------------------------------------------------
    # ORIGINAL
    # --------------------------------------------------------

    original_dir = output_dir / "original"
    original_dir.mkdir(exist_ok=True)

    cv2.imwrite(
        str(
            original_dir /
            f"{image_file.stem}.jpg"
        ),
        image
    )


    # --------------------------------------------------------
    # GRAYSCALE
    # --------------------------------------------------------

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    gray_dir = output_dir / "grayscale"
    gray_dir.mkdir(exist_ok=True)

    cv2.imwrite(
        str(
            gray_dir /
            f"{image_file.stem}.jpg"
        ),
        gray
    )


    # --------------------------------------------------------
    # CLAHE / CONTRAST ENHANCEMENT
    # --------------------------------------------------------

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    clahe_image = clahe.apply(
        gray
    )

    clahe_dir = output_dir / "clahe"
    clahe_dir.mkdir(exist_ok=True)

    cv2.imwrite(
        str(
            clahe_dir /
            f"{image_file.stem}.jpg"
        ),
        clahe_image
    )


    # --------------------------------------------------------
    # THRESHOLD
    # --------------------------------------------------------

    _, threshold = cv2.threshold(
        clahe_image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    threshold_dir = output_dir / "threshold"
    threshold_dir.mkdir(exist_ok=True)

    cv2.imwrite(
        str(
            threshold_dir /
            f"{image_file.stem}.jpg"
        ),
        threshold
    )


# ============================================================
# 5. COMPLETE
# ============================================================

print("\n========================================")
print("PREPROCESSING COMPLETE")
print("========================================")

print(
    "Original images :",
    output_dir / "original"
)

print(
    "Grayscale images:",
    output_dir / "grayscale"
)

print(
    "CLAHE images    :",
    output_dir / "clahe"
)

print(
    "Threshold images:",
    output_dir / "threshold"
)