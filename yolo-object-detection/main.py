import argparse
from src import load_model, process_directory, train

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--train",
        action="store_true",
        help="Train YOLO model"
    )

    parser.add_argument(
        "--predict",
        action="store_true",
        help="Run inference"
    )

    args = parser.parse_args()

    if args.train:
        train()

    elif args.predict:
        model = load_model()
        process_directory(model)

if __name__ == "__main__":
    main()