import torch
import torch.nn as nn
import torch.optim as optim


from dataset import create_dataloaders, create_datasets
from model import create_model
from sklearn.metrics import confusion_matrix, classification_report
from pathlib import Path

NUM_CLASSES = 10
BATCH_SIZE = 32
LEARNING_RATE = 0.001
NUM_EPOCHS = 5

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using device:", device)

train_dataset, test_dataset = create_datasets()

train_loader, test_loader = create_dataloaders(
    train_dataset,
    test_dataset,
)

model = create_model(NUM_CLASSES)

#Freeze all layers first.
for parameter in model.parameters():
    parameter.requires_grad = False

#Unfreeze the final ResNet block.
for parameter in model.layer4.parameters():
    parameter.requires_grad = True

#Keep the classifier trainable.
for parameter in model.fc.parameters():
    parameter.requires_grad = True

model = model.to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    filter(lambda parameter: parameter.requires_grad, model.parameters()),
    lr=0.0001,
)

for epoch in range(NUM_EPOCHS):
    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item() * images.size(0)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    epoch_loss = running_loss / total
    epoch_accuracy = correct / total

    print(
        f"Epoch {epoch + 1}/{NUM_EPOCHS} "
        f"- Loss: {epoch_loss:.4f} "
        f"- Accuracy: {epoch_accuracy:.4f}"
    )

model.eval()

correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

test_accuracy = correct / total

print(f"Test Accuracy: {test_accuracy:.4f}")

all_labels = []
all_predictions = []

model.eval()

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        all_labels.extend(labels.cpu().numpy())
        all_predictions.extend(predicted.cpu().numpy())

class_names = test_dataset.classes

print("\nClassification Report:")
print(
    classification_report(
        all_labels,
        all_predictions,
        target_names=class_names,
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        all_labels,
        all_predictions,
    )
)

MODEL_DIR = Path(__file__).resolve().parents[1] / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "food10_resnet18.pth"

torch.save(model.state_dict(), MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")

