# SIPL Internship Project

This repository contains the complete work completed during my internship training at SIPL.

The project covers Python programming, data processing, NumPy, computer vision, OCR, machine learning workflows, YOLO object detection, ANPR, custom model training, evaluation, testing, and final project demonstration.

The work was completed through practical tasks, experiments, implementations, testing, and project-based learning.

---

## Internship Objectives

The main objectives of this internship were:

- Learn and strengthen Python programming fundamentals
- Understand control flow and collections
- Work with functions, modules, and packages
- Work with CSV and JSON files
- Implement exception handling and logging
- Understand Object-Oriented Programming
- Write automated tests using pytest
- Learn NumPy and numerical operations
- Understand image arrays and preprocessing
- Understand machine learning workflows
- Learn model selection and persistence
- Work with OpenCV
- Implement OCR using EasyOCR
- Perform OCR preprocessing
- Understand YOLO object detection
- Prepare a number plate detection dataset
- Train a custom YOLO detector
- Perform YOLO inference
- Build a YOLO + EasyOCR ANPR pipeline
- Evaluate model performance
- Test the final implementation
- Package and demonstrate the final ANPR project

---

## Project Structure

The repository is organized into different learning, implementation, and project modules.

### Python Fundamentals

Basic Python programming concepts including:

- Variables
- Data types
- Operators
- Input and output
- Conditional statements
- Loops
- Basic programming exercises

---

### Control Flow and Collections

Covered:

- Conditional logic
- Loops
- Lists
- Tuples
- Sets
- Dictionaries
- Data filtering
- Vehicle event processing

---

### Functions, Modules and Packages

Covered:

- Function creation
- Parameters and return values
- Code modularization
- Importing modules
- Package organization
- Type hints
- Docstrings

---

### File Processing and Exception Handling

Worked with:

- CSV files
- JSON files
- File reading and writing
- pathlib
- Data validation
- Exception handling
- Logging rejected records

---

### Object Oriented Programming and Testing

Implemented:

- Classes and objects
- Dataclasses
- VehicleEvent
- DetectionResult
- Unit testing
- pytest
- Test validation

---

## NumPy

### NumPy Arrays, Shapes & Data Types

Learned:

- NumPy arrays
- Array dimensions
- Shapes
- Data types
- Indexing
- Slicing
- Numerical operations

---

### Vectorization and Broadcasting

Worked with:

- Vectorized operations
- Broadcasting
- Array calculations
- Efficient numerical processing

---

### Image Arrays and Preprocessing

Worked with image data as numerical arrays.

Topics included:

- Image loading
- Image dimensions
- Pixel values
- Image array manipulation
- Image preprocessing

---

### Preprocessing and Pipelines

Worked on structured preprocessing workflows for computer vision and machine learning tasks.

---

## Machine Learning

### Machine Learning Workflow

Covered the general machine learning workflow:

1. Data preparation
2. Data preprocessing
3. Training
4. Validation
5. Evaluation
6. Model improvement
7. Model persistence

---

### Model Selection and Persistence

Worked with:

- Model selection
- Loading trained models
- Saving models
- Reusing trained models for inference

---

### Evaluation and Cross Validation

Worked with:

- Model evaluation
- Performance metrics
- Validation
- Cross validation
- Result analysis

---

## Computer Vision

### YOLO Computer Vision and Detection

Worked with YOLO for object detection.

Tasks included:

- Loading YOLO models
- Image inference
- Object detection
- Bounding boxes
- Confidence scores
- Detection results

---

### Plate Detection Dataset

Prepared and worked with a dataset for vehicle number plate detection.

The dataset was used as the foundation for training a custom plate detection model.

---

### YOLO Train Custom Detector

Trained a custom YOLO detector for number plate detection.

The training workflow included:

- Dataset preparation
- Dataset configuration
- YOLO model setup
- Custom detector training
- Training output
- Model weights
- Best model selection

The trained model was used in the later ANPR pipeline.

---

### YOLO Validate Improve Export

Worked on:

- Model validation
- Detection performance analysis
- Improving detection results
- Model output inspection
- Export and deployment considerations

---

### YOLO Inference on Video

Implemented YOLO inference on video input.

The workflow includes:

- Loading video
- Processing video frames
- Running object detection
- Detecting vehicles and plates
- Generating detection results

---

## OCR

### EasyOCR OCR Fundamentals

Learned and implemented OCR using EasyOCR.

Covered:

- EasyOCR setup
- OCR model loading
- Text detection
- Text recognition
- OCR confidence scores
- Text normalization

---

### EasyOCR OpenCV OCR Preprocessing

Worked with OpenCV-based preprocessing to improve OCR results.

Processing techniques were applied before OCR recognition.

---

## ANPR Pipeline

### YOLO EasyOCR ANPR Pipeline

Built an Automatic Number Plate Recognition pipeline using:

- Python
- YOLO
- EasyOCR
- OpenCV

### Pipeline

Vehicle Image
      |
      v
YOLO Detection
      |
      v
Number Plate Detection
      |
      v
Plate Crop
      |
      v
Image Preprocessing
      |
      v
EasyOCR
      |
      v
Text Extraction
      |
      v
Text Normalization
      |
      v
Number Plate Result

## Evaluation and Demonstration

### Evaluation Packaging and Demonstration

The final evaluation stage contains:

- Evaluation scripts
- Ground truth data
- Test images
- Model files
- Evaluation results
- Performance metrics
- pytest tests
- Demonstration script

The evaluation checks:

- Total images
- Evaluated images
- Exact matches
- Exact match rate
- Processing time
- Average FPS
- OCR confidence
- Detection count

### Evaluation Result


Total Images       : 15
Evaluated Images   : 6
Exact Matches      : 0
Exact Match Rate   : 0.0%
Average FPS        : 0.37

## Testing

The project includes automated tests using pytest.

Example test result:

7 passed

The tests verify:

- Text normalization
- Results file existence
- Metrics file existence
- Results structure
- Metrics structure
- Total image count
- Metric value ranges

---

## Technologies Used

- Python
- NumPy
- OpenCV
- EasyOCR
- Ultralytics YOLO
- PyTorch
- pytest
- JSON
- CSV
- Git
- GitHub

---

## Repository Organization

SIPL_Intern_Project/
│
├── Python Fundamentals/
├── Control Flow and Collections/
├── Functions Modules and Packages/
├── File Processing and Exception Handling/
├── Object Oriented Programming and Testing/
│
├── NumPy Arrays, Shapes & Data Types/
├── Vectorization and Broadcasting/
├── Image Arrays and Preprocessing/
├── Preprocessing and Pipelines/
│
├── Machine Learning Workflow/
├── Model Selection and Persistence/
├── Evaluation and Cross Validation/
│
├── EasyOCR OCR Fundamentals/
├── EasyOCR OpenCV OCR Preprocessing/
│
├── Plate Detection Dataset/
├── YOLO Computer Vision and Detection/
├── YOLO Train Custom Detector/
├── YOLO Validate Improve Export/
├── YOLO Inference on Video/
├── YOLO EasyOCR ANPR Pipeline/
│
├── Evaluation Packaging and Demonstration/
│
├── requirements.txt
└── .gitignore

---

## Learning Outcome

Through this internship project, I gained practical experience in:

- Python development
- Data processing
- Computer vision
- Image preprocessing
- OCR
- Machine learning workflows
- Object detection
- YOLO model training
- Custom dataset preparation
- Model evaluation
- Automated testing
- Git and GitHub
- Building an end-to-end ANPR pipeline

---

## Author

**Nazish**
