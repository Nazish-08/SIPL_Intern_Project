# Preprocessing and Pipelines

## Description

This project demonstrates a safe machine learning preprocessing workflow using scikit-learn Pipeline and ColumnTransformer. The dataset contains numerical and categorical features with missing values.

## Workflow

```text
Raw Dataset
    ↓
Train/Test Split
    ↓
Numerical Preprocessing
    ↓
Imputation
    ↓
Standard Scaling
    ↓
Categorical Preprocessing
    ↓
Imputation
    ↓
One-Hot Encoding
    ↓
Logistic Regression
    ↓
Prediction
    ↓
Accuracy Evaluation
```

## Features

* Handle missing numerical values
* Handle missing categorical values
* Scale numerical features
* Encode categorical features
* Apply different preprocessing to different columns
* Combine preprocessing and model using Pipeline
* Prevent preprocessing data leakage
* Train and evaluate a Logistic Regression classifier
* Make predictions on new data

## Concepts Used

* SimpleImputer
* StandardScaler
* OneHotEncoder
* ColumnTransformer
* Pipeline
* LogisticRegression
* train_test_split
* fit()
* predict()
* score()
* accuracy_score()
* random_state

## File

```text
preprocessing_pipeline.py
```

## How to Run

```bash
python preprocessing_pipeline.py
```

## Preprocessing

### Numerical Features

The numerical columns are processed using:

```text
SimpleImputer
    ↓
StandardScaler
```

Missing numerical values are replaced with the mean and the resulting values are standardized.

### Categorical Features

The categorical columns are processed using:

```text
SimpleImputer
    ↓
OneHotEncoder
```

Missing categorical values are replaced with the most frequent value and categorical values are converted into numerical features.

## Pipeline

The preprocessing steps and Logistic Regression model are combined into a single Pipeline. This ensures that preprocessing is learned only from the training data and helps prevent data leakage.

## Reproducibility

A fixed `random_state=42` is used for the train/test split.

## Learning Outcome

* Learned how to handle missing values.
* Learned numerical scaling and categorical encoding.
* Learned how ColumnTransformer applies different preprocessing to different columns.
* Learned how Pipeline combines preprocessing and machine learning models.
* Understood how Pipeline helps prevent data leakage.