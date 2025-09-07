import os
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ========================
# Kaggle Authentication (from Streamlit secrets)
# ========================
try:
    os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
    os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]
    st.success("✅ Kaggle credentials loaded successfully!")
except Exception as e:
    st.error("❌ Kaggle credentials not found. Please set them in Streamlit Secrets.")
    st.stop()

# ========================
# Cached function to download & load dataset
# ========================
@st.cache_data
def load_data():
    if not os.path.exists("./data/train.csv"):
        os.system("mkdir -p data")
        os.system("kaggle competitions download -c house-prices-advanced-regression-techniques -p ./data --force")
        os.system("unzip -o ./data/house-prices-advanced-regression-techniques.zip -d ./data")
    return pd.read_csv("./data/train.csv")

# ========================
# Cached function to train model
# ========================
@st.cache_resource
def train_model(df):
    X = df[["OverallQual", "GrLivArea", "GarageCars"]]
    y = df["SalePrice"]
    model = LinearRegression()
    model.fit(X, y)
    return model

# ========================
# Main App
# ========================
st.title("🏠 House Price Prediction App")
st.write("This app trains a Linear Regression model using the Kaggle House Prices dataset.")

# Load data
df = load_data()

# 👀 Preview dataset
st.subheader("📊 Sample of Training Data")
st.dataframe(df.head())

# 📈 Histogram of Sale Price
st.subheader("📈 Sale Price Distribution (Histogram)")
fig, ax = plt.subplots()
ax.hist(df["SalePrice"], bins=50, color="skyblue", edgecolor="black")
ax.set_xlabel("Sale Price")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Train model
model = train_model(df)

# Streamlit UI
st.subheader("🔮 Make a Prediction")
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Ground Living Area (sq ft)", 500, 5000, 1500, step=50)
garage_cars = st.slider("Garage Cars", 0, 5, 2)

# Prepare input
input_data = pd.DataFrame([[overall_qual, gr_liv_area, garage_cars]],
                          columns=["OverallQual", "GrLivArea", "GarageCars"])

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction:,.0f}")
