from pathlib import Path

MODEL_PATH = "models/yolov8n.pt"
BEST_MODEL = "models/best.pt"

DATASET_CONFIG = "dataset/data.yaml"

IMAGE_SIZE = 640
BATCH_SIZE = 16
EPOCHS = 50
CONFIDENCE = 0.4

DEVICE = 0

TEST_IMAGES = Path("dataset/test/images")
PREDICTIONS_DIR = Path("results")