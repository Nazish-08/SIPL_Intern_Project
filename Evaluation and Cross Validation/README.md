# Evaluation and Cross Validation

## Description

This project evaluates a classification model using accuracy, precision, recall, F1 score, confusion matrix and cross validation.

## Workflow

```text
Iris Dataset
    ↓
Train/Test Split
    ↓
KNN Classifier
    ↓
Predictions
    ↓
Model Evaluation
    ↓
Cross Validation
```

## Metrics Used

### Accuracy
Measures the percentage of correctly classified samples.

### Precision
Measures how many predicted positive cases were actually positive.

High precision means fewer false positives.

### Recall
Measures how many actual positive cases were correctly detected.

High recall means fewer false negatives.

### F1 Score
Combines precision and recall into a single metric.

### Confusion Matrix
Shows the relationship between actual and predicted classes.

## Cross Validation

Five-fold cross validation is used to evaluate model performance across multiple train/test splits.

The program reports:

* Individual CV scores
* Mean CV accuracy
* CV standard deviation

## ANPR Interpretation

### False Positive

The system predicts a valid plate or positive case when the actual case is negative.

Example:

```text
Actual: No valid plate
Prediction: Plate detected
```

### False Negative

A valid plate or positive case exists, but the system fails to detect it.

Example:

```text
Actual: Valid plate
Prediction: Plate not detected
```

For ANPR, recall is important when missing a valid vehicle or plate is costly. Precision is important when false detections create incorrect vehicle records.

## Files

* `evaluation.py`
* `confusion_matrix.png`
* `README.md`

## How to Run

```bash
python evaluation.py
```

## Learning Outcome

* Learned classification evaluation metrics.
* Interpreted precision, recall and F1 score.
* Created and interpreted a confusion matrix.
* Applied five-fold cross validation.
* Understood false positives and false negatives in the context of ANPR.