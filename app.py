# app.py

import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load the trained model
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Patient Recovery Prediction",
    page_icon="🏥",
    layout="centered",
)

# -----------------------------
# Header / Hero Section
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; padding:20px; border-radius:10px; background-color:#f0f4f8">
        <h1 style="color:#003366;">Patient Recovery Prediction System</h1>
        <p style="color:#555;">Predict recovery days based on patient features using AI</p>
    </div>
    """, unsafe_allow_html=True
)

st.write("---")

# -----------------------------
# Input Section
# -----------------------------
st.header("Patient Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender", ["M", "F"])
    heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=75)

with col2:
    fever = st.selectbox("Fever (1=Yes, 0=No)", [0,1])
    fatigue = st.selectbox("Fatigue (1=Yes, 0=No)", [0,1])

# Map gender to numeric
gender_num = 0 if gender == "M" else 1
input_data = pd.DataFrame([[age, gender_num, fever, fatigue, heart_rate]],
                          columns=['Age','Gender','Fever','Fatigue','HeartRate'])

# -----------------------------
# Prediction Button
# -----------------------------
st.write("---")
if st.button("Predict Recovery Days"):
    predicted_days = model.predict(input_data)[0]
    
    # Display result in a styled info box
    st.markdown(
        f"""
        <div style="padding:20px; border-radius:10px; background-color:#d1e7dd; text-align:center;">
            <h2 style="color:#0f5132;">Predicted Recovery Days: {predicted_days:.1f} days</h2>
        </div>
        """, unsafe_allow_html=True
    )

# -----------------------------
# Footer / Disclaimer
# -----------------------------
st.write("---")
st.markdown(
    "<p style='text-align:center; color:#888;'>This prediction is for educational purposes and not a substitute for medical advice.</p>",
    unsafe_allow_html=True
)
