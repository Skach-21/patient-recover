# app.py

import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# 1. Load the trained model
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Patient Recovery Prediction System")
st.write("Enter patient information to predict recovery days:")

# -----------------------------
# 2. User input
# -----------------------------
age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", ["M", "F"])
fever = st.selectbox("Fever (1=Yes, 0=No)", [0,1])
fatigue = st.selectbox("Fatigue (1=Yes, 0=No)", [0,1])
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=75)

# Map gender to numeric
gender_num = 0 if gender == "M" else 1

# Prepare input dataframe
input_data = pd.DataFrame([[age, gender_num, fever, fatigue, heart_rate]],
                          columns=['Age','Gender','Fever','Fatigue','HeartRate'])

# -----------------------------
# 3. Make prediction
# -----------------------------
if st.button("Predict Recovery Days"):
    predicted_days = model.predict(input_data)[0]
    st.success(f"Predicted Recovery Days: {predicted_days:.1f} days")
