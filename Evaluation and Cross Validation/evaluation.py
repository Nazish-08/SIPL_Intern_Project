import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target   

print("========== DATASET ==========")
print("Features:", X.shape)
print("Labels:", y.shape)
print("Classes:", iris.target_names)


# ============================================================
# 2. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================================
# 3. CREATE AND TRAIN MODEL
# ============================================================

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

print("\n========== MODEL ==========")
print("KNN model trained successfully.")


# ============================================================
# 4. PREDICTIONS
# ============================================================

predictions = model.predict(X_test)

print("\n========== PREDICTIONS ==========")
print("Actual:")
print(y_test)

print("\nPredicted:")
print(predictions)


# ============================================================
# 5. ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n========== ACCURACY ==========")
print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")


# ============================================================
# 6. CLASSIFICATION REPORT
# ============================================================

print("\n========== CLASSIFICATION REPORT ==========")

report = classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
)

print(report)


# ============================================================
# 7. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    predictions
)

print("========== CONFUSION MATRIX ==========")
print(cm)


# ============================================================
# 8. PLOT CONFUSION MATRIX
# ============================================================

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot()

plt.title("Iris Classification Confusion Matrix")

plt.savefig(
    "confusion_matrix.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("\nConfusion matrix saved as confusion_matrix.png")


# ============================================================
# 9. CROSS VALIDATION
# ============================================================

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\n========== CROSS VALIDATION ==========")

print("CV Scores:")
print(cv_scores)

print("Mean CV Accuracy:", np.mean(cv_scores))
print("CV Standard Deviation:", np.std(cv_scores))


# ============================================================
# 10. ANPR METRIC INTERPRETATION
# ============================================================

print("\n========== ANPR INTERPRETATION ==========")

print("""
False Positive:
The system predicts a valid plate or positive case,
but the actual case is negative.

False Negative:
A valid plate or positive case exists,
but the system fails to detect it.

Precision:
Higher precision means fewer false positive predictions.

Recall:
Higher recall means fewer false negative predictions.

F1 Score:
F1 combines precision and recall into a single metric.
""")