from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import os
import pandas as pd


current_dir = os.path.dirname(os.path.abspath(__file__))

# Load model and preprocessor
model_path = os.path.join(current_dir, 'model', 'flight_price_model.pkl')
preprocessor_path = os.path.join(current_dir, 'model', 'preprocessor.pkl')

model = joblib.load(model_path)
preprocessor = joblib.load(preprocessor_path)

# Initialize FastAPI app
app = FastAPI(
    title="Flight Price Prediction API",
    description="Predict flight ticket price based on travel details.",
    version="1.0"
)

# Define input schema (Pydantic model)
class FlightDataRequest(BaseModel):
    airline: str = Field(..., description="Airline name")
    source_city: str = Field(..., description="City of departure")
    departure_time: str = Field(..., description="Time of departure (e.g., Morning, Evening)")
    stops: str = Field(..., description="Number of stops (e.g., zero, one)")
    arrival_time: str = Field(..., description="Time of arrival")
    destination_city: str = Field(..., description="Destination city")
    class_: str = Field(..., alias="class_type", description="Class (Economy/Business)")
    duration: float = Field(..., description="Duration of flight in hours")
    days_left: int = Field(..., description="Days left before departure")

# Root route for testing
@app.get("/", tags=["Welcome"])
async def welcome():
    return {"message": "Welcome to the Flight Price Prediction API!"}

# Prediction route
@app.post("/predict", tags=["Flight Price Prediction"])
async def predict_price(request: FlightDataRequest):
    try:
        
        input_dict = {
            "airline": [request.airline],
            "source_city": [request.source_city],
            "departure_time": [request.departure_time],
            "stops": [request.stops],
            "arrival_time": [request.arrival_time],
            "destination_city": [request.destination_city],
            "class": [request.class_],
            "duration": [request.duration],
            "days_left": [request.days_left]
        }

        input_df = pd.DataFrame(input_dict)

   
        transformed_data = preprocessor.transform(input_df)
        prediction = model.predict(transformed_data)

        # Return predicted price
        return {"Predicted Price": round(prediction[0], 2)}

    except Exception as e:
        return {"error": str(e)}
