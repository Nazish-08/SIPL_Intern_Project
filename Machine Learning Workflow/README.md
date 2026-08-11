# Machine Learning Workflow

## Description
This project demonstrates a complete supervised machine learning workflow using the Iris dataset and a K-Nearest Neighbors classifier.

## Workflow

1. Load the Iris dataset.
2. Separate features (X) and labels (y).
3. Split the dataset into training and testing sets.
4. Create a KNN classifier.
5. Train the model using fit().
6. Generate predictions using predict().
7. Evaluate the model using accuracy and score().
8. Make a prediction on a new flower sample.

## Features

- Iris dataset
- Feature and label separation
- Train/test split
- K-Nearest Neighbors classification
- Reproducible train/test split
- Model training
- Prediction
- Baseline accuracy evaluation

## Concepts Used

- X and y
- train_test_split()
- fit()
- predict()
- score()
- accuracy_score()
- random_state
- supervised learning
- classification

## File

- classifier.py

## How to Run

```bash
python classifier.py
```

## Model

The project uses `KNeighborsClassifier` with 3 nearest neighbors as the baseline classifier.

## Reproducibility

A fixed `random_state=42` is used during the train/test split so that the same data split is produced on repeated runs.

## Learning Outcome

- Learned the basic supervised machine learning workflow.
- Understood the difference between features and labels.
- Practiced splitting data into training and testing sets.
- Trained a classification model using fit().
- Generated predictions using predict().
- Evaluated baseline model performance using accuracy.