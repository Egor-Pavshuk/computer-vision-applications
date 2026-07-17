# Computer Vision Applications

This repository contains practical computer vision projects implemented in Python using modern deep learning frameworks. The projects focus on object detection and face recognition and demonstrate complete computer vision pipelines, from data preprocessing to inference and evaluation.

## Repository Structure

```text
Computer-Vision/
│
├── face-recognition/
│   ├── FaceRecognition.ipynb
│   └── README.md
│
├── yolo/
│   ├── YOLO.ipynb
│   └── README.md
│
├── requirements.txt
└── .gitignore
```

## Projects

### YOLO Object Detection

Object detection project based on the Ultralytics YOLO framework.

**Features**

* Dataset preparation
* Model training
* Model evaluation
* Object detection on images
* Performance visualization

**Technologies**

* Python
* PyTorch
* Ultralytics YOLO
* OpenCV
* NumPy
* Matplotlib

---

### Face Recognition with ArcFace

Face recognition pipeline based on InsightFace and ArcFace embeddings.

**Pipeline**

* Face detection
* Face embedding extraction
* Cosine similarity matching
* Image retrieval

**Technologies**

* Python
* InsightFace
* ArcFace
* ONNX Runtime
* OpenCV
* NumPy

---

## Notes

Large datasets, trained weights, and generated embeddings are not included in this repository due to their size. Each project contains its own documentation with setup instructions and dataset information.

---

## License

This repository is intended for educational and research purposes.
