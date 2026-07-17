import cv2
from pathlib import Path

def load_image(path):
    return cv2.imread(str(path))


def save_image(path, image):
    cv2.imwrite(str(path), image)


def get_image_files(folder):

    return [
        p
        for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp")
        for p in Path(folder).glob(ext)
    ]