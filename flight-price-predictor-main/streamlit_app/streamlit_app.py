import streamlit as st
import requests

st.set_page_config(page_title="Flight Price Predictor")

st.title("Flight Price Prediction App")

# Form inputs
with st.form("flight_form"):
    airline = st.selectbox("Airline", ["Indigo", "AirAsia", "Vistara", "SpiceJet"])
    source_city = st.selectbox("Source City", ["Delhi", "Mumbai", "Bangalore", "Kolkata"])
    departure_time = st.selectbox("Departure Time", ["Morning", "Evening", "Afternoon", "Night"])
    stops = st.selectbox("Number of Stops", ["zero", "one", "two_or_more"])
    arrival_time = st.selectbox("Arrival Time", ["Morning", "Evening", "Afternoon", "Night"])
    destination_city = st.selectbox("Destination City", ["Mumbai", "Delhi", "Bangalore", "Kolkata"])
    class_type = st.selectbox("Class", ["Economy", "Business"])
    duration = st.slider("Flight Duration (hours)", 1.0, 10.0, 2.5)
    days_left = st.slider("Days Left Until Departure", 1, 60, 15)

    submitted = st.form_submit_button("Predict Price")


if submitted:
    payload = {
        "airline": airline,
        "source_city": source_city,
        "departure_time": departure_time,
        "stops": stops,
        "arrival_time": arrival_time,
        "destination_city": destination_city,
        "class_type": class_type,  
        "duration": duration,
        "days_left": days_left
    }

    try:
        # Talk to FastAPI backend using internal container name
        response = requests.post("http://fast_api:8000/predict", json=payload)
        #response = requests.post("http://localhost:8000/predict", json=payload)


        if response.status_code == 200:
            price = response.json()["Predicted Price"]
            st.success(f"Estimated Ticket Price: ₹{price}")
        else:
            st.error(f"API Error: {response.status_code}")
            st.json(response.json())
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")
