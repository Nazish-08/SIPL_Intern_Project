from pathlib import Path
from ultralytics import YOLO


# ============================================================
# 1. PATHS
# ============================================================

model_path = Path(
    "../YOLO Train Custom Detector/runs/plate_detector/weights/best.pt"
).resolve()

dataset_yaml = Path(
    "../Plate Detection Dataset/data.yaml"
).resolve()


# ============================================================
# 2. CHECK FILES
# ============================================================

if not model_path.exists():
    raise FileNotFoundError(
        f"Model not found: {model_path}"
    )

if not dataset_yaml.exists():
    raise FileNotFoundError(
        f"Dataset configuration not found: {dataset_yaml}"
    )


# ============================================================
# 3. LOAD MODEL
# ============================================================

model = YOLO(str(model_path))

print("========== CONFIDENCE THRESHOLD COMPARISON ==========")
print("Model:", model_path)


# ============================================================
# 4. BASELINE: CONF = 0.25
# ============================================================

print("\n========== CONFIDENCE = 0.25 ==========")

metrics_025 = model.val(
    data=str(dataset_yaml),
    split="test",
    imgsz=640,
    batch=4,
    conf=0.25,
    device="cpu",
    plots=False,
    verbose=False
)

print(f"Precision:   {metrics_025.box.mp:.4f}")
print(f"Recall:      {metrics_025.box.mr:.4f}")
print(f"mAP50:       {metrics_025.box.map50:.4f}")
print(f"mAP50-95:    {metrics_025.box.map:.4f}")


# ============================================================
# 5. NEW THRESHOLD: CONF = 0.50
# ============================================================

print("\n========== CONFIDENCE = 0.50 ==========")

metrics_050 = model.val(
    data=str(dataset_yaml),
    split="test",
    imgsz=640,
    batch=4,
    conf=0.50,
    device="cpu",
    plots=False,
    verbose=False
)

print(f"Precision:   {metrics_050.box.mp:.4f}")
print(f"Recall:      {metrics_050.box.mr:.4f}")
print(f"mAP50:       {metrics_050.box.map50:.4f}")
print(f"mAP50-95:    {metrics_050.box.map:.4f}")


# ============================================================
# 6. COMPARISON
# ============================================================

print("\n========================================")
print("BEFORE / AFTER COMPARISON")
print("========================================")

print(
    f"Precision:  "
    f"{metrics_025.box.mp:.4f} → "
    f"{metrics_050.box.mp:.4f}"
)

print(
    f"Recall:     "
    f"{metrics_025.box.mr:.4f} → "
    f"{metrics_050.box.mr:.4f}"
)

print(
    f"mAP50:      "
    f"{metrics_025.box.map50:.4f} → "
    f"{metrics_050.box.map50:.4f}"
)

print(
    f"mAP50-95:   "
    f"{metrics_025.box.map:.4f} → "
    f"{metrics_050.box.map:.4f}"
)


# ============================================================
# 7. DECISION
# ============================================================

print("\n========================================")
print("THRESHOLD DECISION")
print("========================================")

if metrics_050.box.map50 > metrics_025.box.map50:
    print("conf=0.50 produced higher mAP50.")
else:
    print("conf=0.25 produced higher or equal mAP50.")

print("\nComparison complete.")