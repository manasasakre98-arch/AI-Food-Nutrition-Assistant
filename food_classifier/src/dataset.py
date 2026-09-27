from pathlib import Path

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "food-10" / "siamtech_food10"

TRAIN_DIR = DATA_DIR / "train"
TEST_DIR = DATA_DIR / "test"

train_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])

test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def create_datasets():
    train_dataset = datasets.ImageFolder(
        root = TRAIN_DIR,
        transform = train_transform,
    )

    test_dataset = datasets.ImageFolder(
        root = TEST_DIR,
        transform = test_transform,
    )

    return train_dataset, test_dataset

def create_dataloaders(train_dataset, test_dataset):
    train_loader = DataLoader(
        train_dataset,
        batch_size = 32,
        shuffle=True,
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=32,
        shuffle=False,
    )

    return train_loader, test_loader

def main():
    train_dataset, test_dataset = create_datasets()

    train_loader, test_loader = create_dataloaders(
        train_dataset,
        test_dataset,
    )

    print("Classes:", train_dataset.classes)
    print("Class mappings:", train_dataset.class_to_idx)
    print("Training images:", len(train_dataset))
    print("Test images:", len(test_dataset))

    images, labels = next(iter(train_loader))

    print("Batch image shape:", images.shape)
    print("Batch label shape:", labels.shape)

if __name__ == "__main__":
    main()