from pathlib import Path

import torch
from PIL import Image
from torchvision import models, transforms
from nutrition import get_nutrition

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

top_probabilities, top_indices = torch.topk(probabilities, 3)

top_confidence =top_probabilities[0][0].item()

if top_confidence < 0.50:
    print("The model is not confident enough to identify this image.")
else:
    print("Top 3 predictions:")

    for probability, index in zip(top_probabilities[0], top_indices[0]):
        class_name = CLASS_NAMES[index.item()]
        confidence = probability.item() * 100

        print(f"{class_name}: {confidence:.2f}%")

    predicted_class = CLASS_NAMES[top_indices[0][0].item()]
    nutrition = get_nutrition(predicted_class)

    print("\nNutrition Information:")
    print(f"Food: {predicted_class}")
    print(f"Serving: {nutrition['serving']}")
    print(f"Calories: {nutrition['calories']}")
    print(f"Protein: {nutrition['protein']} g")
    print(f"Carbs: {nutrition['carbs']} g")
    print(f"Fat: {nutrition['fat']} g")

 