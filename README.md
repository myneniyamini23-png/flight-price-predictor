# ✈️ Flight Price Predictor  

A **full-stack machine learning project** that predicts flight ticket prices based on various factors such as airline, route, travel class, duration, and days left before departure.  

This project integrates **FastAPI**, **Streamlit**, and **Docker** to deliver a scalable, interactive, and production-ready price prediction system.  

---

## 🧠 Tech Stack  

- **FastAPI** — Backend REST API for model inference  
- **Streamlit** — Frontend web app for user interaction  
- **Random Forest Regressor** — Machine Learning model for price prediction  
- **Docker & Docker Compose** — For containerization and easy multi-service deployment  

---

## 🚀 Features  

- 🎯 Predict flight ticket prices using a trained **Random Forest** model  
- ⚙️ REST API with **FastAPI** and **Pydantic** for data validation  
- 🖥️ User-friendly **Streamlit** UI for real-time predictions  
- 🧩 Fully **containerized** using Docker Compose  
- 📘 Auto-generated API docs with **Swagger UI**  

---

## 📁 Project Structure  

flight-price-predictor/
├── docker-compose.yml
├── fast_api/
│ ├── main.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── model/
│ ├── flight_price_model.pkl
│ └── preprocessor.pkl
├── streamlit_app/
│ ├── streamlit_app.py
│ ├── requirements.txt
│ └── Dockerfile
└── README.md

---


