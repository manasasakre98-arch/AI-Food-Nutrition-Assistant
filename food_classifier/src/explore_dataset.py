from pathlib import Path

from torchvision.datasets import Food101


def main():
    # Store the downloaded dataset in food_classifier/data, relative to this script.
    data_dir = Path(__file__).resolve().parents[1] / "data"

    # Download Food-101 if needed, then open both official dataset splits.
    train_dataset = Food101(root=data_dir, split="train", download=True)
    test_dataset = Food101(root=data_dir, split="test", download=False)

    # Show the sizes and class names so the dataset is easy to inspect.
    print(f"Training samples: {len(train_dataset)}")
    print(f"Test samples: {len(test_dataset)}")
    print("Food classes:")
    for class_name in train_dataset.classes:
        print(f"- {class_name}")
    print(f"Total classes: {len(train_dataset.classes)}")

    # Load one training example and look up the readable name for its label.
    image, class_index = train_dataset[0]
    class_name = train_dataset.classes[class_index]
    print(f"Sample image label: {class_name}")

    # Open the sample image in the computer's default image viewer.
    image.show(title=f"Food-101 sample: {class_name}")


if __name__ == "__main__":
    main()
