# 🏡 House Price Prediction App  

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-cloud-FF4B4B.svg)](https://streamlit.io/)  
[![Kaggle](https://img.shields.io/badge/dataset-Kaggle-20BEFF.svg)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  

This project is a **Streamlit web app** that predicts house prices using a **Linear Regression model** trained on the **Kaggle House Prices dataset**.  

It automatically downloads the dataset from Kaggle, trains a model, and provides interactive predictions based on selected features.  

---

## ✨ Features  
- 📥 Automatic Kaggle dataset download (no manual CSV upload needed)  
- ⚙️ Feature selection — choose one or more predictors (`GrLivArea`, `GarageCars`, `OverallQual`, `YearBuilt`)  
- 📊 Data exploration — view sample data, histogram of sale prices, and scatter plots  
- 🤖 Linear Regression model trained live in the app  
- 📐 R² score to show model performance  
- 💡 Interactive predictions with real-time input  

---

## 📸 Demo  

👉 [Live Demo](https://your-streamlit-link.streamlit.app)  
*(replace with your actual Streamlit Cloud link)*  

![App Screenshot](https://user-images.githubusercontent.com/your-screenshot-link.png)  
*(replace with your actual screenshot)*  

---

## 🚀 Deployment  

This app is deployed on **Streamlit Cloud**.  

To deploy your own:  
1. Fork this repository  
2. Connect it to Streamlit Cloud  
3. Add your **Kaggle API credentials** under *Secrets*  

---

## ⚡ Run Locally  

Clone this repo:  
```bash
git clone https://github.com/yourusername/House-Prices-Prediction.git
cd House-Prices-Prediction

## Install dependencies:

pip install -r requirements.txt


## Add your Kaggle API credentials to a .streamlit/secrets.toml file:

KAGGLE_USERNAME = "your-username"
KAGGLE_KEY = "your-key"


## Run the app:

streamlit run app.py

## 📦 Requirements

See requirements.txt
:

streamlit

pandas

scikit-learn

kaggle

matplotlib

seaborn

📂 Repository Structure
House-Prices-Prediction/
│── app.py              # Streamlit app
│── requirements.txt    # Dependencies
│── README.md           # Project documentation

🏆 Acknowledgements

Dataset: Kaggle - House Prices: Advanced Regression Techniques

Built with Streamlit

📜 License

This project is licensed under the MIT License



