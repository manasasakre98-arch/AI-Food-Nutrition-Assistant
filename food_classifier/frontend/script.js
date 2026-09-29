const imageInput = document.getElementById("imageInput");
const predictButton = document.getElementById("predictButton");

const preview = document.getElementById("preview");
const result = document.getElementById("result");
const predictions = document.getElementById("predictions");
const nutrition = document.getElementById("nutrition");
const resetButton = document.getElementById("resetButton");

resetButton.addEventListener("click", () => {
    imageInput.value = "";

    preview.innerHTML = "";

    result.style.display = "none";

    predictions.innerHTML = "";
    nutrition.innerHTML = "";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

//Show image preview
imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];

    if(!file){
        return;
    }

    const imageURL = URL.createObjectURL(file);

    preview.innerHTML = `
        <img src="${imageURL}" alt="Selected food">
    `;
});

//Send image to FastAPI
predictButton.addEventListener("click", async () =>{
    const file = imageInput.files[0];

    if(!file){
        alert("Please select a food image first.");
        return;
    }

    predictButton.disabled = true;
    predictButton.textContent = "Predicting...";

    const formData = new FormData();

    formData.append("file", file);

    try{
        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                body: formData
            }
        );

        if(!response.ok){
            throw new Error("Prediction request failed.");
        }

        const data = await response.json();

        displayResults(data);
    } catch (error){
        console.error(error);

        alert(
            "Could not connect to the prediction API. " +
            "Make sure FastAPI is running."
        );
    } finally{
        predictButton.disabled = false;
        predictButton.textContent = "Predict Food";
    }
});

//Display API response
function displayResults(data){
    result.style.display = "block";

    predictions.innerHTML = `
        <h3>Top Predictions<h3>
    `;

    data.predictions.forEach((prediction) => {
        predictions.innerHTML += `
            <div class="prediction-item">
                 <div class="prediction-header">
                    <span>${prediction.food}</span>
                    <strong>${prediction.confidence}%</strong>
                 </div>

                 <div class="confidence-bar">
                     <div
                         class="confidence-fill"
                         style="width: ${prediction.confidence}%"
                    ></div>
                </div>

            </div>
        `;
    });

    const food = data.predictions[0].food;
    const nutritionData = data.nutrition;

    nutrition.innerHTML = `
        <div class="nutrition-card">

            <h3>${food} Nutrition</h3>

            <p class="serving">
                Serving:
                <strong>${nutritionData.serving}</strong>
            </p>

            <div class="nutrition-grid">

                <div class="nutrition-item">
                    <span>Calories</span>
                    <strong>${nutritionData.calories} kcal</strong>
                </div>

                <div class="nutrition-item">
                    <span>Protein</span>
                    <strong>${nutritionData.protein} g</strong>
                </div>

                <div class="nutrition-item">
                    <span>Carbs</span>
                    <strong>${nutritionData.carbs} g</strong>
                </div>

                <div class="nutrition-item">
                    <span>Fat</span>
                    <strong>${nutritionData.fat} g</strong>
                </div>

            </div>

            <p class="source">
                Source: ${nutritionData.source}
            </p>

        </div>
    `;
}