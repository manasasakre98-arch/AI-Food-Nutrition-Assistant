from pathlib import Path

import torch
from PIL import Image
from torchvision import models, transforms

CLASS_NAMES = [
    "FriedChicked",
    "GaengKeawWan",
    "KaoManGai",
    "KhaoNiewMaMuang",
    "KuayTeowReua",
    "PadThai",
    "PhatKaphrao",
    "Somtam",
    "StewedPorkLeg",
    "TomYumGoong",
]

model = models.resnet18(weights=None)

model.fc = torch.nn.Linear(
    model.fc.in_features,
    len(CLASS_NAMES),
)

MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "food10_resnet18.pth"
)

model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

IMAGE_PATH = (
    Path(__file__).resolve().parents[1]
    / "test_images"
    / "test_food.jpg"
)

image = Image.open(IMAGE_PATH).convert("RGB")

image_tensor = transform(image).unsqueeze(0)

with torch.no_grad():
    outputs = model(image_tensor)

    probabilities = torch.softmax(outputs, dim=1)

    confidence, predicted_class = torch.max(probabilities, dim=1)

predicted_name = CLASS_NAMES[predicted_class.item()]

print(f"Prediction: {predicted_name}")
print(f"Confidence: {confidence.item() * 100:.2f}%")