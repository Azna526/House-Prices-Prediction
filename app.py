import os
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# Setup Kaggle credentials from Streamlit secrets
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

# Download dataset (Kaggle competition: House Prices)
if not os.path.exists("./data/train.csv"):
    os.system("mkdir -p data")
    os.system("kaggle competitions download -c house-prices-advanced-regression-techniques -p ./data --force")
    os.system("unzip -o ./data/house-prices-advanced-regression-techniques.zip -d ./data")

# Load data
df = pd.read_csv("./data/train.csv")

# Train a simple model
X = df[["OverallQual", "GrLivArea", "GarageCars"]]
y = df["SalePrice"]

model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("🏠 House Price Prediction App (Kaggle API)")
st.write("Enter house details to predict the price.")

overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Ground Living Area (sq ft)", 500, 5000, 1500, step=50)
garage_cars = st.slider("Garage Cars", 0, 5, 2)

# Prepare input
input_data = pd.DataFrame([[overall_qual, gr_liv_area, garage_cars]],
                          columns=["OverallQual", "GrLivArea", "GarageCars"])

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction:,.0f}")
