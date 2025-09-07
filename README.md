# 🏠 House Price Prediction App

This project predicts house prices using a machine learning model trained on the **Ames Housing dataset**.  
The model has been trained locally and saved as `model.pkl`. A Streamlit app (`app.py`) loads this model and allows users to input house features to predict the price.

---

## 📂 Project Structure

```
House-Prices-Prediction/
│── app.py            # Streamlit app
│── model.pkl         # Pre-trained ML model
│── requirements.txt  # Dependencies
│── (optional) train.csv, test.csv  # Raw datasets (not required for deployment)
│── (optional) notebook.ipynb       # Jupyter notebook for training
```

---

## 🚀 Running Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/House-Prices-Prediction.git
   cd House-Prices-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment (Streamlit Cloud)

- Main file path: `app.py`
- Requirements file: `requirements.txt`
- `model.pkl` must be in the same folder as `app.py`

---

## 📝 Notes

- `train.csv` and `test.csv` are only needed if you want to retrain the model.  
- For deployment, only `app.py`, `model.pkl`, and `requirements.txt` are required.

---

## ✨ Example Features Used

- **OverallQual** (Overall Quality: 1–10)  
- **GrLivArea** (Ground Living Area in sq. ft.)  
- **GarageCars** (Number of cars garage can hold)  

---

## 📊 Example Prediction

Input:
- Overall Quality: 7  
- Ground Living Area: 2000 sq. ft.  
- Garage Cars: 2  

Output:
- Predicted Price: `$250,000`
