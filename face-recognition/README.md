# Face Recognition with ArcFace

This project implements a face recognition pipeline using **InsightFace** and **ArcFace** embeddings. It detects faces, extracts feature embeddings, and identifies matching faces in a dataset using cosine similarity.

## Features

* Face detection with InsightFace
* ArcFace embedding extraction
* Cosine similarity matching
* Batch processing of image datasets
* Automatic saving of matched images

## Pipeline

1. Load the dataset.
2. Detect faces in each image.
3. Generate ArcFace embeddings.
4. Generate embeddings for reference images.
5. Compare embeddings using cosine similarity.
6. Save matched images.

## Technologies

* Python
* InsightFace
* ArcFace
* ONNX Runtime
* OpenCV
* NumPy
* Matplotlib
* Google Colab

## Dataset

The face dataset is **not included** in this repository due to its size.

Update the dataset paths inside the notebook before running the project.

## Results

The pipeline successfully:

* detects faces in images;
* extracts ArcFace embeddings;
* compares embeddings using cosine similarity;
* retrieves matching images from the dataset.

## Future Improvements

* Face clustering
* Multiple-face tracking
* Real-time webcam recognition
* Threshold optimization