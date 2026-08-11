# Model Selection and Persistence

## Description

This project demonstrates hyperparameter tuning, model comparison and model persistence using scikit-learn.

Two model families, K-Nearest Neighbors and Logistic Regression, are tuned using GridSearchCV and compared using cross-validation accuracy.

## Workflow

```text
Iris Dataset
    ↓
Train/Test Split
    ↓
KNN GridSearchCV ─────────┐
                          ├── Model Comparison
Logistic Regression ──────┘
       GridSearchCV
             ↓
      Best Model Selection
             ↓
       Test Evaluation
             ↓
      Save Pipeline
             ↓
       Load Pipeline
             ↓
      Inference Test
```

## Models Compared

### K-Nearest Neighbors

Hyperparameters tuned:

* n_neighbors
* weights

### Logistic Regression

Hyperparameters tuned:

* C
* solver

## Model Selection Metric

The models are selected using five-fold cross-validation accuracy.

The model with the highest cross-validation accuracy is selected as the final model.

## Model Persistence

The complete fitted pipeline is saved using `joblib`.

```text
model_v1.joblib
```

The saved pipeline is then loaded and used for inference without retraining.

## Files

```text
model_selection.py
model_comparison.csv
model_v1.joblib
README.md
```

## How to Run

```bash
python model_selection.py
```

## Reproducibility

A fixed `random_state=42` is used for the train/test split.

## Inference Verification

The program compares predictions from the original fitted pipeline and the reloaded pipeline.

Expected result:

```text
Original and loaded predictions match: True
```

## Learning Outcome

* Learned hyperparameter tuning using GridSearchCV.
* Compared two different model families.
* Used cross-validation to select a model.
* Learned how to inspect best_params_.
* Saved a complete fitted pipeline using joblib.
* Reloaded the saved model and performed inference.