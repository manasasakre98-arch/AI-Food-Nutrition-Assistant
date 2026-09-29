# 🍜 AI Food & Nutrition Assistant

An AI-powered web application that identifies food from an uploaded image and provides nutritional information for the predicted food.

The project combines a **ResNet18 image classification model**, a **FastAPI backend**, and a **HTML/CSS/JavaScript frontend** to create an end-to-end food recognition and nutrition application.

---

## ✨ Features

- 📷 Upload a food image
- 🖼️ Preview the selected image
- 🤖 Classify food using a ResNet18 deep learning model
- 🎯 Display the Top-3 predictions
- 📊 Show prediction confidence percentages
- 📈 Visual confidence bars
- 🍽️ Display nutrition information for the predicted food
- 🔥 Calories
- 💪 Protein
- 🍚 Carbohydrates
- 🥑 Fat
- 🌐 FastAPI REST API
- 📚 Interactive Swagger API documentation
- 🔄 Analyze another image without refreshing the application
- 💻 Simple responsive frontend

---

## 🧠 How It Works

The application follows this pipeline:

```text
User uploads food image
        │
        ▼
Frontend
HTML + CSS + JavaScript
        │
        │ Image upload
        ▼
FastAPI Backend
        │
        ▼
Image Preprocessing
Resize → Tensor Conversion
        │
        ▼
ResNet18 Model
        │
        ▼
Food Classification
        │
        ▼
Top-3 Predictions
        │
        ▼
Nutrition Lookup
        │
        ▼
Food + Confidence + Nutrition
        │
        ▼
Frontend Result Display
```

---

## 🤖 Machine Learning Model

The food classification component uses **ResNet18** with PyTorch and Torchvision.

The model is trained to classify images into **10 Thai food categories**.

### Model Configuration

| Parameter | Value |
|---|---|
| Model | ResNet18 |
| Number of classes | 10 |
| Training epochs | 5 |
| Batch size | 32 |
| Learning rate | 0.001 |
| Optimizer | Adam |
| Loss function | Cross Entropy Loss |
| Training device | CPU |
| Test images | 290 |

### Image Preprocessing

Input images are processed using:

```python
transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])
```

---

## 📊 Model Performance

The final training run achieved:

**Test Accuracy: 95.52%**

### Training Performance

| Epoch | Loss | Training Accuracy |
|---:|---:|---:|
| 1 | 1.1212 | 68.08% |
| 2 | 0.2642 | 94.62% |
| 3 | 0.1126 | 98.92% |
| 4 | 0.0718 | 99.23% |
| 5 | 0.0409 | 99.62% |

### Test Classification Results

| Food Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| FriedChicken | 1.00 | 0.94 | 0.97 |
| GaengKeawWan | 1.00 | 0.95 | 0.97 |
| KaoManGai | 1.00 | 0.96 | 0.98 |
| KhaoNiewMaMuang | 1.00 | 0.98 | 0.99 |
| KuayTeowReua | 0.95 | 0.93 | 0.94 |
| PadThai | 0.88 | 0.96 | 0.92 |
| PhatKaphrao | 0.91 | 1.00 | 0.95 |
| Somtam | 0.95 | 0.86 | 0.90 |
| StewedPorkLeg | 0.88 | 0.96 | 0.92 |
| TomYumGoong | 0.91 | 1.00 | 0.95 |

**Overall test accuracy: 95.52%**

---

## 🍜 Supported Food Classes

The model currently recognizes the following 10 food categories:

1. FriedChicken
2. GaengKeawWan
3. KaoManGai
4. KhaoNiewMaMuang
5. KuayTeowReua
6. PadThai
7. PhatKaphrao
8. Somtam
9. StewedPorkLeg
10. TomYumGoong

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Frontend        │
                    │ HTML / CSS / JS     │
                    └──────────┬──────────┘
                               │
                         Image Upload
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI         │
                    │      Backend        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Image Preprocessing │
                    │   224 × 224         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     ResNet18        │
                    │ Classification Model│
                    └──────────┬──────────┘
                               │
                         Top-3 Results
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Nutrition Lookup    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Food + Nutrition    │
                    │     Response        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Frontend Results    │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Machine Learning

- Python
- PyTorch
- Torchvision
- ResNet18
- Scikit-learn

### Backend

- FastAPI
- Uvicorn
- Python Multipart

### Frontend

- HTML
- CSS
- JavaScript

### Development Tools

- Git
- GitHub
- VS Code

---

## 📁 Project Structure

```text
AI-Food-Nutrition-Assistant/
│
├── food_classifier/
│   │
│   ├── frontend/
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   │
│   ├── models/
│   │   └── food10_resnet18.pth
│   │
│   └── src/
│       ├── app.py
│       ├── dataset.py
│       ├── explore_dataset.py
│       ├── model.py
│       ├── nutrition.py
│       ├── predict.py
│       └── train.py
│
├── .gitignore
└── README.md
```

---

## 🌐 FastAPI Backend

The application uses FastAPI to expose the food prediction functionality as an API.

### Start the API

From the project root:

```bash
uvicorn food_classifier.src.app:app --reload
```

The server runs locally at:

```text
http://127.0.0.1:8000
```

### Swagger Documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

The `/predict` endpoint accepts a food image and returns the predicted food classes with confidence scores and nutrition information.

---

## 📦 API Response Example

Example response from the prediction API:

```json
{
  "predictions": [
    {
      "food": "PadThai",
      "confidence": 90.47
    },
    {
      "food": "KuayTeowReua",
      "confidence": 3.14
    },
    {
      "food": "Somtam",
      "confidence": 2.03
    }
  ],
  "nutrition": {
    "serving": "1 cup (~200 g)",
    "calories": 308,
    "protein": 16.3,
    "carbs": 29,
    "fat": 15,
    "source": "USDA FoodData Central reference"
  }
}
```

---

## 🍽️ Nutrition Information

After identifying the food, the application retrieves nutrition information associated with the predicted food.

The frontend displays:

- Serving size
- Calories
- Protein
- Carbohydrates
- Fat
- Nutrition source

For example:

```text
Food: PadThai

Serving: 1 cup (~200 g)
Calories: 308 kcal
Protein: 16.3 g
Carbs: 29 g
Fat: 15 g
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/manasasakre98-arch/AI-Food-Nutrition-Assistant
cd AI-Food-Nutrition-Assistant
```


### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 4. Install required packages

```powershell
pip install torch torchvision
pip install fastapi uvicorn python-multipart
pip install scikit-learn pillow
```

---

## ▶️ Running the Application

### Step 1 — Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### Step 2 — Start FastAPI

```powershell
uvicorn food_classifier.src.app:app --reload
```

### Step 3 — Open Swagger

Visit:

```text
http://127.0.0.1:8000/docs
```

### Step 4 — Open the frontend

Open the following file in a browser:

```text
food_classifier/frontend/index.html
```

### Step 5 — Predict food

1. Select a food image.
2. Preview the selected image.
3. Click **Predict Food**.
4. View the Top-3 predictions.
5. View confidence scores.
6. View nutrition information.
7. Click **Analyze Another Image** to test another image.

---

## 🧪 Example

For a Pad Thai image, an example prediction is:

```text
Top Predictions:

PadThai          90.47%
KuayTeowReua      3.14%
Somtam            2.03%
```

Nutrition:

```text
Serving: 1 cup (~200 g)
Calories: 308 kcal
Protein: 16.3 g
Carbs: 29 g
Fat: 15 g
```

---

## ⚠️ Limitations

- The current model supports only 10 food categories.
- Prediction quality depends on the input image and similarity to the training data.
- Nutrition information is based on the available food references and may vary depending on ingredients, preparation method, and serving size.
- The current application runs locally and has not been deployed as a public web service.
- The model currently runs on CPU in the demonstrated setup.

---

## 🔮 Future Improvements

The following are potential future improvements and are **not currently implemented**:

- Expand the food classification dataset
- Add more food categories
- Improve image augmentation and generalization
- Expand nutrition data coverage
- Add meal history
- Add daily calorie tracking
- Add personalized nutrition recommendations
- Deploy the FastAPI backend
- Deploy the frontend
- Improve mobile responsiveness
- Add user authentication

---

## 📌 Project Status

**MVP Completed ✅**

The current version provides an end-to-end workflow:

```text
Food Image
    ↓
AI Food Classification
    ↓
Top-3 Predictions
    ↓
Nutrition Lookup
    ↓
Nutrition Display
```

The application has been tested locally with a working FastAPI backend and frontend.

---

## 👩‍💻 Author

**Manasa**

B.E. Computer Science Engineering