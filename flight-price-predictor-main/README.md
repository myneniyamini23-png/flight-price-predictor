# Flight Price Predictor

A full-stack machine learning project that predicts flight ticket prices based on user inputs such as airline, route, travel class, duration, and days left before departure.

This project is built with:
- **FastAPI**: for serving the ML model as a REST API
- **Streamlit**: for a user-friendly frontend interface
- **Docker & Docker Compose**: for containerization and easy deployment

---

## Features

- Predict flight ticket prices using a trained RandomForest model
- REST API with validation using Pydantic and FastAPI
- Streamlit-based UI for easy user interaction
- Fully containerized using Docker Compose
- Auto-generated API documentation (Swagger UI)

---

## Project Structure

```
.
├── docker-compose.yml
├── fast_api/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── model/
│       ├── flight_price_model.pkl
│       └── preprocessor.pkl
├── streamlit_app/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── Dockerfile
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nandini-678/flight-price-predictor.git
cd flight-price-predictor
```

### 2. Run the App with Docker Compose

```bash
docker-compose up --build
```

This will build and launch both the FastAPI backend and the Streamlit frontend.

---

## Access the Application

- Streamlit Frontend: [http://localhost:8501](http://localhost:8501)
- FastAPI Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Sample API Request

Send a POST request to `/predict`:

```json
{
  "airline": "Indigo",
  "source_city": "Delhi",
  "departure_time": "Morning",
  "stops": "one",
  "arrival_time": "Evening",
  "destination_city": "Mumbai",
  "class_type": "Economy",
  "duration": 2.5,
  "days_left": 15
}
```

