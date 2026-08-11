# Image Arrays and Preprocessing

## Description
This project demonstrates image preprocessing using NumPy and OpenCV. A vehicle image is loaded as a NumPy array, inspected, resized, converted to grayscale, thresholded, and cropped to extract a plate region.

## Features
* Load vehicle images using OpenCV
* Inspect image shape, dimensions and data type
* Understand BGR and RGB formats
* Resize images while preserving aspect ratio
* Convert images to grayscale
* Apply binary thresholding
* Crop a Region of Interest (ROI)
* Use NumPy slicing for image cropping
* Use np.clip() to keep ROI coordinates within image boundaries
* Save processed images using OpenCV

## Project Structure

```text
Image Arrays and Preprocessing/
│
├── image_preprocessing.py
├── images/
│   └── vehicle.jpg
├── output/
│   ├── resized.jpg
│   ├── grayscale.jpg
│   ├── threshold.jpg
│   ├── plate_roi.jpg
│   ├── plate_gray.jpg
│   ├── plate_threshold.jpg
│   └── rgb_image.jpg
└── README.md
```

## Concepts Used

* cv2.imread()
* cv2.cvtColor()
* cv2.resize()
* cv2.threshold()
* cv2.imwrite()
* NumPy ndarray
* ndarray slicing
* np.clip()
* BGR and RGB
* ROI extraction

## How to Run

```bash
python image_preprocessing.py
```

## Output

The program generates resized, grayscale, thresholded and plate ROI images inside the `output` directory.

## Learning Outcome

* Learned how OpenCV represents images as NumPy arrays.
* Understood the difference between BGR and RGB.
* Practiced basic image preprocessing.
* Learned how to extract a Region of Interest using NumPy slicing.
* Prepared consistent plate-region samples for future detection and OCR tasks.