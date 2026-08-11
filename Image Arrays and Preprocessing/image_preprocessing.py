import cv2
import numpy as np
from pathlib import Path


# ============================================================
# 1. FILE PATHS
# ============================================================

input_file = Path("images/vehicle.jpg")
output_dir = Path("output")

output_dir.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD VEHICLE IMAGE
# ============================================================

image = cv2.imread(str(input_file))

if image is None:
    raise FileNotFoundError(f"Image not found: {input_file}")

print("========== ORIGINAL IMAGE ==========")
print("Image loaded successfully.")
print("Shape:", image.shape)
print("Dimensions:", image.ndim)
print("Data Type:", image.dtype)


# ============================================================
# 3. BGR TO RGB
# ============================================================

rgb_image = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

print("\n========== COLOR FORMAT ==========")
print("OpenCV image format: BGR")
print("Converted image format: RGB")


# ============================================================
# 4. RESIZE WHILE KEEPING ASPECT RATIO
# ============================================================

original_height, original_width = image.shape[:2]

target_width = 800

scale = target_width / original_width
target_height = int(original_height * scale)

resized_image = cv2.resize(
    image,
    (target_width, target_height)
)

cv2.imwrite(
    str(output_dir / "resized.jpg"),
    resized_image
)

print("\n========== RESIZE ==========")
print("Original:", original_width, "x", original_height)
print("Resized:", target_width, "x", target_height)


# ============================================================
# 5. GRAYSCALE
# ============================================================

gray_image = cv2.cvtColor(
    resized_image,
    cv2.COLOR_BGR2GRAY
)

cv2.imwrite(
    str(output_dir / "grayscale.jpg"),
    gray_image
)

print("\n========== GRAYSCALE ==========")
print("Grayscale shape:", gray_image.shape)


# ============================================================
# 6. THRESHOLD
# ============================================================

_, threshold_image = cv2.threshold(
    gray_image,
    120,
    255,
    cv2.THRESH_BINARY
)

cv2.imwrite(
    str(output_dir / "threshold.jpg"),
    threshold_image
)

print("\n========== THRESHOLD ==========")
print("Threshold image created.")


# ============================================================
# 7. PLATE ROI
# ============================================================

# Coordinates based on the supplied vehicle image.
# Original image size: 736 x 1063

x1 = 155
y1 = 745

x2 = 345
y2 = 835


# ============================================================
# 8. SCALE ROI COORDINATES
# ============================================================

x1 = int(x1 * scale)
x2 = int(x2 * scale)

y1 = int(y1 * scale)
y2 = int(y2 * scale)


# ============================================================
# 9. CLIP COORDINATES
# ============================================================

height, width = resized_image.shape[:2]

x1 = int(np.clip(x1, 0, width))
x2 = int(np.clip(x2, 0, width))

y1 = int(np.clip(y1, 0, height))
y2 = int(np.clip(y2, 0, height))


# ============================================================
# 10. CROP FULL NUMBER PLATE
# ============================================================

plate_roi = resized_image[
    y1:y2,
    x1:x2
]

if plate_roi.size == 0:
    raise ValueError("ROI crop is empty.")


cv2.imwrite(
    str(output_dir / "plate_roi.jpg"),
    plate_roi
)

print("\n========== PLATE ROI ==========")
print("X1:", x1)
print("Y1:", y1)
print("X2:", x2)
print("Y2:", y2)

print("Plate ROI Shape:", plate_roi.shape)


# ============================================================
# 11. GRAYSCALE PLATE ROI
# ============================================================

plate_gray = cv2.cvtColor(
    plate_roi,
    cv2.COLOR_BGR2GRAY
)

cv2.imwrite(
    str(output_dir / "plate_gray.jpg"),
    plate_gray
)


# ============================================================
# 12. THRESHOLD PLATE ROI
# ============================================================

_, plate_threshold = cv2.threshold(
    plate_gray,
    120,
    255,
    cv2.THRESH_BINARY
)

cv2.imwrite(
    str(output_dir / "plate_threshold.jpg"),
    plate_threshold
)


# ============================================================
# 13. SAVE RGB VERSION
# ============================================================

rgb_for_save = cv2.cvtColor(
    rgb_image,
    cv2.COLOR_RGB2BGR
)

cv2.imwrite(
    str(output_dir / "rgb_image.jpg"),
    rgb_for_save
)


# ============================================================
# 14. FINAL OUTPUT
# ============================================================

print("\n========== PROCESSING COMPLETE ==========")

print("Output files:")

for file in sorted(output_dir.iterdir()):
    print("-", file.name)