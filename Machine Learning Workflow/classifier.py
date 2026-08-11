from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# 1. LOAD IRIS DATASET
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target

print("========== DATASET ==========")
print("Features shape:", X.shape)
print("Labels shape:", y.shape)
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)


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
# 3. CREATE CLASSIFIER
# ============================================================

model = KNeighborsClassifier(n_neighbors=3)


# ============================================================
# 4. TRAIN MODEL
# ============================================================

model.fit(X_train, y_train)

print("\n========== MODEL TRAINING ==========")
print("Model training completed.")


# ============================================================
# 5. MAKE PREDICTIONS
# ============================================================

predictions = model.predict(X_test)

print("\n========== PREDICTIONS ==========")

print("Actual labels:")
print(y_test)

print("\nPredicted labels:")
print(predictions)


# ============================================================
# 6. CALCULATE ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

score = model.score(
    X_test,
    y_test
)

print("\n========== BASELINE PERFORMANCE ==========")
print("Accuracy:", accuracy)
print("Score:", score)
print("Accuracy Percentage:", accuracy * 100, "%")


# ============================================================
# 7. PREDICT A NEW FLOWER
# ============================================================

new_flower = [[
    5.1,
    3.5,
    1.4,
    0.2
]]

prediction = model.predict(new_flower)

predicted_species = iris.target_names[prediction[0]]

print("\n========== NEW PREDICTION ==========")
print("Input:", new_flower)
print("Predicted class:", prediction[0])
print("Predicted species:", predicted_species)