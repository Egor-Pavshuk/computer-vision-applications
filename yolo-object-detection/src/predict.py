from ultralytics import YOLO
from tqdm import tqdm

from configs import (
    BEST_MODEL,
    CONFIDENCE,
    DEVICE,
    PREDICTIONS_DIR,
)

from .utils import (
    load_image,
    save_image,
    get_image_files,
)

def load_model():
    return YOLO(BEST_MODEL)


def predict_image(model, image):

    result = model.predict(
        image,
        conf=CONFIDENCE,
        device=DEVICE,
    )

    return result[0].plot()


def process_directory(model):

    files = get_image_files("dataset/test/images")

    for idx, image_path in enumerate(tqdm(files)):

        image = load_image(image_path)

        if image is None:
            continue

        annotated = predict_image(model, image)

        save_image(
            PREDICTIONS_DIR / f"result_{idx}.jpg",
            annotated,
        )

        if idx == 10:
            break