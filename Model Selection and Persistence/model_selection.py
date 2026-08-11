import pandas as pd
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


# ============================================================
# 1. LOAD DATASET
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target

print("========== DATASET ==========")
print("Features:", X.shape)
print("Labels:", y.shape)


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

print("\n========== TRAIN / TEST SPLIT ==========")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# 3. MODEL 1: KNN PIPELINE
# ============================================================

knn_pipeline = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("model", KNeighborsClassifier())
    ]
)

knn_parameters = {
    "model__n_neighbors": [3, 5, 7, 9],
    "model__weights": ["uniform", "distance"]
}


# ============================================================
# 4. GRID SEARCH FOR KNN
# ============================================================

knn_grid = GridSearchCV(
    estimator=knn_pipeline,
    param_grid=knn_parameters,
    cv=5,
    scoring="accuracy"
)

knn_grid.fit(X_train, y_train)

print("\n========== KNN GRID SEARCH ==========")
print("Best KNN Parameters:")
print(knn_grid.best_params_)

print("Best KNN CV Accuracy:")
print(knn_grid.best_score_)


# ============================================================
# 5. MODEL 2: LOGISTIC REGRESSION PIPELINE
# ============================================================

logistic_pipeline = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        (
            "model",
            LogisticRegression(max_iter=1000)
        )
    ]
)

logistic_parameters = {
    "model__C": [0.1, 1, 10],
    "model__solver": ["lbfgs", "liblinear"]
}


# ============================================================
# 6. GRID SEARCH FOR LOGISTIC REGRESSION
# ============================================================

logistic_grid = GridSearchCV(
    estimator=logistic_pipeline,
    param_grid=logistic_parameters,
    cv=5,
    scoring="accuracy"
)

logistic_grid.fit(X_train, y_train)

print("\n========== LOGISTIC REGRESSION GRID SEARCH ==========")
print("Best Logistic Regression Parameters:")
print(logistic_grid.best_params_)

print("Best Logistic Regression CV Accuracy:")
print(logistic_grid.best_score_)


# ============================================================
# 7. COMPARE MODELS
# ============================================================

comparison = pd.DataFrame({
    "Model": [
        "KNN",
        "Logistic Regression"
    ],
    "CV Accuracy": [
        knn_grid.best_score_,
        logistic_grid.best_score_
    ]
})

print("\n========== MODEL COMPARISON ==========")
print(comparison)


# ============================================================
# 8. SAVE COMPARISON TABLE
# ============================================================

comparison.to_csv(
    "model_comparison.csv",
    index=False
)

print("\nModel comparison saved to model_comparison.csv")


# ============================================================
# 9. SELECT BEST MODEL
# ============================================================

if knn_grid.best_score_ >= logistic_grid.best_score_:
    best_model = knn_grid.best_estimator_
    best_model_name = "KNN"
    best_score = knn_grid.best_score_

else:
    best_model = logistic_grid.best_estimator_
    best_model_name = "Logistic Regression"
    best_score = logistic_grid.best_score_


print("\n========== BEST MODEL ==========")
print("Selected Model:", best_model_name)
print("Best CV Accuracy:", best_score)


# ============================================================
# 10. TEST BEST MODEL
# ============================================================

test_accuracy = best_model.score(
    X_test,
    y_test
)

print("\n========== TEST PERFORMANCE ==========")
print("Test Accuracy:", test_accuracy)
print("Test Accuracy Percentage:", test_accuracy * 100, "%")


# ============================================================
# 11. SAVE COMPLETE FITTED PIPELINE
# ============================================================

model_version = "model_v1.joblib"

joblib.dump(
    best_model,
    model_version
)

print("\n========== MODEL SAVED ==========")
print("Saved model:", model_version)


# ============================================================
# 12. LOAD SAVED MODEL
# ============================================================

loaded_model = joblib.load(
    model_version
)

print("\n========== MODEL LOADED ==========")
print("Saved pipeline loaded successfully.")


# ============================================================
# 13. INFERENCE TEST
# ============================================================

new_flower = [[
    5.1,
    3.5,
    1.4,
    0.2
]]

prediction = loaded_model.predict(
    new_flower
)

predicted_species = iris.target_names[
    prediction[0]
]

print("\n========== INFERENCE TEST ==========")
print("Input:", new_flower)
print("Predicted Class:", prediction[0])
print("Predicted Species:", predicted_species)


# ============================================================
# 14. VERIFY LOADED MODEL
# ============================================================

original_prediction = best_model.predict(
    new_flower
)

loaded_prediction = loaded_model.predict(
    new_flower
)

print("\n========== MODEL VERIFICATION ==========")

print(
    "Original and loaded predictions match:",
    original_prediction[0] == loaded_prediction[0]
)