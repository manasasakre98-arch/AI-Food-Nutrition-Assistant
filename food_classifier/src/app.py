import torch
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from torchvision import transforms
import io

from .model import create_model
from .nutrition import get_nutrition

NUM_CLASSES = 10

CLASS_NAMES = [
    "FriedChicken",
    "GaengKeawWan",
    "KaoManGai",
    "KhaoNiewMaMuang",
    "KuayTeowReua",
    "PadThai",
    "PhatKaphrao",
    "Somtam",
    "StewedPorkLeg",
    "TomYumGoong"
]

app = FastAPI(
    title="AI Food Nutrition Assistant",
    description="Food image classification and nutrition API",
    version="1.0.0",
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = create_model(NUM_CLASSES)

MODEL_PATH = "food_classifier/models/food10_resnet18.pth"

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device,
    )
)

model = model.to(device)
model.eval()

@app.get("/")
def home():
    return{
        "message": "AI Food Nutrition Assistant API is running"
    }

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    image_tensor = transform(image)
    image_tensor = image_tensor.unsqueeze(0)
    image_tensor = image_tensor.to(device)

    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.softmax(outputs, dim=1)

    top_probabilities, top_indices = torch.topk(
        probabilities,
        3,
    )

    predictions = []

    for probability, index in zip(
        top_probabilities[0],
        top_indices[0],
    ):
        class_name = CLASS_NAMES[index.item()]
        confidence = probability.item() * 100

        predictions.append({
            "food": class_name,
            "confidence": round(confidence, 2),
        })

    predicted_class = CLASS_NAMES[
        top_indices[0][0].item()
    ]

    nutrition = get_nutrition(predicted_class)

    return{
        "predictions": predictions,
        "nutrition": nutrition,
    }