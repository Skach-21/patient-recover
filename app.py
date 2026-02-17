import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load trained model
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Patient Recovery Prediction",
    page_icon="🏥",
    layout="centered"
)

# -----------------------------
# Inject CSS for styling
# -----------------------------
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: grey;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Header styling */
    .header-box {
        background-color:#003366 ;
        color: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Input section box */
    .input-box {
        background-color:white ;
	color: pink;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 10px #d1d1d1;
    }

    /* Prediction box */
    .prediction-box {
        background-color: blue-dark;
        color: cyan;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        margin-top: 20px;
        transition: background-color 0.3s ease;
    }

    .prediction-box:hover {
        background-color: white;
    }

    /* Button hover */
    div.stButton > button:hover {
        background-color: pink;
        color: blue;
        border-radius: 8px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: white;
        font-size: 0.9em;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="header-box"><h1>Patient Recovery Prediction System</h1>'
            '<p>Predict recovery days based on patient features using AI</p></div>', unsafe_allow_html=True)

# -----------------------------
# Input Section
# -----------------------------
st.markdown('<div class="input-box">', unsafe_allow_html=True)
st.header("Patient Information")

# Layout columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender_input = st.selectbox("Gender", ["M", "F"])
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=75)

with col2:
    fever_input = st.selectbox("Fever", ["No", "Yes"])
    fatigue_input = st.selectbox("Fatigue", ["No", "Yes"])

st.markdown('</div>', unsafe_allow_html=True)

# Convert inputs to numeric for model
gender = 0 if gender_input == "M" else 1
fever = 1 if fever_input == "Yes" else 0
fatigue = 1 if fatigue_input == "Yes" else 0

input_data = pd.DataFrame([[age, gender, fever, fatigue, heart_rate]],
                          columns=['Age','Gender','Fever','Fatigue','HeartRate'])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Recovery Days"):
    predicted_days = model.predict(input_data)[0]
    st.markdown(f'<div class="prediction-box">Predicted Recovery Days: {predicted_days:.1f} days</div>', 
                unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown('<div class="footer">This prediction is for educational purposes and not medical advice.</div>', 
            unsafe_allow_html=True)





