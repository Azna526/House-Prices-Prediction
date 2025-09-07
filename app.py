import os
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile

# ================================
# Kaggle Authentication
# ================================
if "KAGGLE_USERNAME" in st.secrets and "KAGGLE_KEY" in st.secrets:
    os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
    os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]
    st.success("✅ Kaggle credentials loaded successfully!")
else:
    st.error("❌ Kaggle credentials not found in secrets!")
    st.stop()

# ================================
# Download & Extract Dataset
# ================================
if not os.path.exists("./data/train.csv"):
    os.makedirs("data", exist_ok=True)
    st.write("📥 Downloading dataset from Kaggle...")
    os.system("kaggle competitions download -c house-prices-advanced-regression-techniques -p ./data --force")

    zip_path = "./data/house-prices-advanced-regression-techniques.zip"
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall("./data")
        st.success("✅ Dataset downloaded and extracted!")
    else:
        st.error("❌ Download failed. Check Kaggle API permissions.")
        st.stop()

# ================================
# Load Data
# ================================
@st.cache_data
def load_data():
    return pd.read_csv("./data/train.csv")

df = load_data()

# ================================
# Train Model
# ================================
@st.cache_resource
def train_model(features):
    X = df[features]
    y = df["SalePrice"]
    model = LinearRegression()
    model.fit(X, y)
    return model

# ================================
# Streamlit UI
# ================================
st.title("🏡 House Price Prediction App")
st.write("This app trains a Linear Regression model using the Kaggle House Prices dataset.")

# Data preview
st.subheader("🔎 Sample Data")
st.dataframe(df.head())

# Feature selector (multiple allowed)
st.subheader("⚙️ Select Features for Prediction")
available_features = ["GrLivArea", "GarageCars", "OverallQual", "YearBuilt"]
selected_features = st.multiselect("Choose one or more features:", available_features, default=["GrLivArea"])

if not selected_features:
    st.warning("⚠️ Please select at least one feature.")
    st.stop()

# Train model
model = train_model(selected_features)

# Histogram of SalePrice (Seaborn)
st.subheader("📊 SalePrice Distribution")
fig, ax = plt.subplots()
sns.histplot(df["SalePrice"], bins=40, kde=True, color="skyblue", ax=ax)
ax.set_xlabel("Sale Price")
ax.set_ylabel("Count")
st.pyplot(fig)

# Scatter plot with regression line (only if single feature)
if len(selected_features) == 1:
    feature = selected_features[0]
    st.subheader(f"📈 {feature} vs Sale Price")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[feature], y=df["SalePrice"], ax=ax, alpha=0.6, edgecolor=None)
    sns.regplot(x=df[feature], y=df["SalePrice"], ax=ax, scatter=False, color="red")
    ax.set_xlabel(feature)
    ax.set_ylabel("Sale Price")
    st.pyplot(fig)

# Prediction section
st.subheader("💡 Predict House Price")
user_inputs = []
for feature in selected_features:
    val = st.number_input(
        f"Enter {feature}:",
        min_value=int(df[feature].min()),
        max_value=int(df[feature].max()),
        value=int(df[feature].median())
    )
    user_inputs.append(val)

pred_price = model.predict([user_inputs])[0]
st.write(f"🏠 Predicted House Price: **${pred_price:,.2f}**")
