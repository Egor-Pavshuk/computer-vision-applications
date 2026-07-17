from ultralytics import YOLO
from pathlib import Path
from shutil import copy2
from configs import (
    MODEL_PATH,
    DATASET_CONFIG,
    EPOCHS,
    IMAGE_SIZE,
    BATCH_SIZE,
    DEVICE,
)

def train():

    model = YOLO(MODEL_PATH)

    model.train(
        data=DATASET_CONFIG,
        epochs=EPOCHS,
        imgsz=IMAGE_SIZE,
        batch=BATCH_SIZE,
        device=DEVICE,
    )

    copy2(
        Path("runs/detect/train/weights/best.pt"),
        Path("models/best.pt")
    )