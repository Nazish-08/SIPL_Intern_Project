from pathlib import Path
import shutil

from ultralytics import YOLO


# ============================================================
# 1. MODEL PATH
# ============================================================

model_path = Path(
    "../YOLO Train Custom Detector/runs/plate_detector/weights/best.pt"
).resolve()


# ============================================================
# 2. OUTPUT PATH
# ============================================================

output_dir = Path("exported").resolve()

output_dir.mkdir(exist_ok=True)


# ============================================================
# 3. CHECK MODEL
# ============================================================

if not model_path.exists():
    raise FileNotFoundError(
        f"Model not found: {model_path}"
    )


# ============================================================
# 4. LOAD BEST MODEL
# ============================================================

model = YOLO(str(model_path))

print("========== ONNX EXPORT ==========")
print("Model:", model_path)


# ============================================================
# 5. EXPORT MODEL
# ============================================================

onnx_path = model.export(
    format="onnx",
    imgsz=640,
    dynamic=True,
    simplify=True
)


# ============================================================
# 6. COPY ONNX TO DAY 17 FOLDER
# ============================================================

onnx_path = Path(onnx_path)

final_path = output_dir / "best.onnx"

shutil.copy2(
    onnx_path,
    final_path
)


# ============================================================
# 7. FINAL OUTPUT
# ============================================================

print("\n========================================")
print("ONNX EXPORT COMPLETE")
print("========================================")

print("Original ONNX:")
print(onnx_path)

print("\nDay 17 ONNX:")
print(final_path)