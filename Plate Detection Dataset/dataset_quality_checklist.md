# Dataset Quality Checklist

## Dataset Structure

- [x] Train, validation and test folders created
- [x] Images and labels are stored separately
- [x] Train images have matching label files
- [x] Validation images have matching label files
- [x] Test images have matching label files

## Annotation Format

- [x] YOLO TXT annotation format used
- [x] Class IDs are defined in data.yaml
- [x] Bounding box coordinates use normalized values
- [x] Class 0 represents license-plate
- [x] Class 1 represents vehicle

## Dataset Split

- [x] Training set contains 245 images
- [x] Validation set contains 70 images
- [x] Test set contains 35 images
- [x] Total dataset contains 350 images

## Data Leakage Checks

- [ ] No duplicate images across train, validation and test
- [ ] Images from the same source are not unnecessarily distributed across different splits
- [ ] Test images are kept separate from training data

## Annotation Quality

- [ ] License plate bounding boxes tightly cover the plate
- [ ] Vehicle bounding boxes cover the complete vehicle
- [ ] No incorrect class labels
- [ ] No missing annotations
- [ ] No corrupted images
- [ ] Labels visually inspected

## Final Validation

- [ ] data.yaml paths verified
- [ ] Class names verified
- [ ] Image and label filenames match
- [ ] Dataset structure reviewed