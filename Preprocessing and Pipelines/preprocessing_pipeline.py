import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# ============================================================
# 1. CREATE SAMPLE DATASET
# ============================================================

data = {
    "age": [25, 30, 28, 35, 40, 22, 31, 27, 45, 29],
    "salary": [
        40000,
        60000,
        50000,
        75000,
        90000,
        35000,
        None,
        48000,
        100000,
        55000
    ],
    "city": [
        "Mumbai",
        "Delhi",
        "Mumbai",
        "Pune",
        "Delhi",
        "Mumbai",
        "Pune",
        None,
        "Delhi",
        "Mumbai"
    ],
    "experience": [1, 4, 3, 7, 10, 0, 5, 2, 12, 4],
    "purchased": [
        "Yes",
        "No",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes"
    ]
}

df = pd.DataFrame(data)

print("========== DATASET ==========")
print(df)


# ============================================================
# 2. FEATURES AND TARGET
# ============================================================

X = df.drop("purchased", axis=1)
y = df["purchased"]

print("\n========== FEATURES ==========")
print(X)

print("\n========== TARGET ==========")
print(y)


# ============================================================
# 3. TRAIN / TEST SPLIT
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
# 4. DEFINE COLUMN TYPES
# ============================================================

numeric_features = [
    "age",
    "salary",
    "experience"
]

categorical_features = [
    "city"
]


# ============================================================
# 5. NUMERICAL PREPROCESSING
# ============================================================

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ]
)


# ============================================================
# 6. CATEGORICAL PREPROCESSING
# ============================================================

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)


# ============================================================
# 7. COLUMN TRANSFORMER
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_pipeline,
            numeric_features
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_features
        )
    ]
)


# ============================================================
# 8. COMPLETE ML PIPELINE
# ============================================================

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(max_iter=1000)
        )
    ]
)


# ============================================================
# 9. TRAIN MODEL
# ============================================================

model.fit(X_train, y_train)

print("\n========== MODEL TRAINING ==========")
print("Pipeline training completed.")


# ============================================================
# 10. PREDICTIONS
# ============================================================

predictions = model.predict(X_test)

print("\n========== PREDICTIONS ==========")

print("Actual:")
print(y_test.to_numpy())

print("\nPredicted:")
print(predictions)


# ============================================================
# 11. MODEL ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

score = model.score(
    X_test,
    y_test
)

print("\n========== PIPELINE PERFORMANCE ==========")
print("Accuracy:", accuracy)
print("Score:", score)
print("Accuracy Percentage:", accuracy * 100, "%")


# ============================================================
# 12. NEW DATA PREDICTION
# ============================================================

new_customer = pd.DataFrame({
    "age": [32],
    "salary": [65000],
    "city": ["Mumbai"],
    "experience": [5]
})

new_prediction = model.predict(new_customer)

print("\n========== NEW PREDICTION ==========")
print(new_customer)
print("Predicted Purchase:", new_prediction[0])