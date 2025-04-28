from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model (ensure model.pkl is present)
model = joblib.load('model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define input data schema (request body)
class InputData(BaseModel):
    carbon_footprint: float
    water_usage: float
    material_category: int  # 0 for Synthetic, 1 for Natural
    recycling_program: int  # 0 for False, 1 for True
    waste_production: float
    sustainability_rating: int  # Numeric 0-3 scale
    has_certifications: int  # 0 for No, 1 for Yes

# Prediction endpoint
@app.post("/predict")
def predict(input_data: InputData):
    # Prepare data for prediction
    input_features = np.array([
        input_data.carbon_footprint,
        input_data.water_usage,
        input_data.material_category,  # Already numeric (0 or 1)
        input_data.recycling_program,  # Already numeric (0 or 1)
        input_data.waste_production,
        input_data.sustainability_rating,  # Numeric scale (0-3)
        input_data.has_certifications  # Already numeric (0 or 1)
    ]).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_features)

    return {"eco_friendly": "Yes" if prediction == 1 else "No"}