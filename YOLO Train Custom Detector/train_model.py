from pathlib import Path
from ultralytics import YOLO


# ============================================================
# 1. PATHS
# ============================================================

dataset_yaml = Path(
    "../Plate Detection Dataset/data.yaml"
).resolve()

project_dir = Path("runs").resolve()

project_dir.mkdir(exist_ok=True)


# ============================================================
# 2. CHECK DATASET
# ============================================================

if not dataset_yaml.exists():
    raise FileNotFoundError(
        f"Dataset configuration not found: {dataset_yaml}"
    )


# ============================================================
# 3. LOAD PRETRAINED YOLO MODEL
# ============================================================

model = YOLO("yolo11n.pt")

print("========== YOLO CUSTOM TRAINING ==========")
print("Pretrained YOLO11n model loaded.")
print("Dataset:", dataset_yaml)
print("Output:", project_dir / "plate_detector")


# ============================================================
# 4. TRAIN MODEL
# ============================================================

results = model.train(
    data=str(dataset_yaml),

    epochs=20,

    batch=4,

    imgsz=640,

    patience=5,

    device="cpu",

    project=str(project_dir),

    name="plate_detector",

    exist_ok=True,

    verbose=True
)


# ============================================================
# 5. TRAINING COMPLETE
# ============================================================

best_model = (
    project_dir
    / "plate_detector"
    / "weights"
    / "best.pt"
)

last_model = (
    project_dir
    / "plate_detector"
    / "weights"
    / "last.pt"
)

results_dir = (
    project_dir
    / "plate_detector"
)


print("\n========================================")
print("CUSTOM YOLO TRAINING COMPLETE")
print("========================================")

print("Best model:")
print(best_model)

print("\nLast model:")
print(last_model)

print("\nTraining results:")
print(results_dir)