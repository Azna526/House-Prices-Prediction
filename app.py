import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

# Input features
overall_qual = st.number_input("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Ground Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.number_input("Garage Cars", 0, 5, 2)

# Convert to DataFrame
input_data = pd.DataFrame([[overall_qual, gr_liv_area, garage_cars]],
                          columns=["OverallQual", "GrLivArea", "GarageCars"])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction:,.0f}")
