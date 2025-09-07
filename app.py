import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict the price.")

# Input fields
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Ground Living Area (sq ft)", 500, 5000, 1500, step=50)
garage_cars = st.slider("Garage Cars", 0, 5, 2)

# Prepare input data
input_data = pd.DataFrame(
    [[overall_qual, gr_liv_area, garage_cars]],
    columns=["OverallQual", "GrLivArea", "GarageCars"]
)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction:,.0f}")
