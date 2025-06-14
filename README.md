# 🌫️ Air Quality Predictor using Machine Learning

This project is an AI-powered model that predicts the Air Quality Index (AQI) based on environmental pollutants like **NO2**, **O3**, **SO2**, and **CO** levels using a supervised machine learning model (Random Forest Regressor).

> 📍 Built as part of an internship project to apply modern AI techniques to real-world environmental data.

---

## 📊 Dataset

The original dataset was sourced from [Kaggle: US Pollution Data (2000–2016)](https://www.kaggle.com/datasets/sogun3/uspollution). Due to size constraints, a smaller preprocessed dataset is used for training in this repository:

# 🌫️ Air Quality Predictor using Machine Learning

This project is an AI-powered model that predicts the Air Quality Index (AQI) based on environmental pollutants like **NO2**, **O3**, **SO2**, and **CO** levels using a supervised machine learning model (Random Forest Regressor).

> 📍 Built as part of an internship project to apply modern AI techniques to real-world environmental data.

---

## 📊 Dataset

The original dataset was sourced from [Kaggle: US Pollution Data (2000–2016)](https://www.kaggle.com/datasets/sogun3/uspollution). Due to size constraints, a smaller preprocessed dataset is used for training in this repository:


---

## 🚀 Features

- ✅ Data preprocessing and feature extraction
- ✅ AQI prediction using **Random Forest Regression**
- ✅ Scaled input using `StandardScaler`
- ✅ Sample prediction input
- ✅ MSE and R² metrics evaluation

---

## 🧠 Tech Stack

- **Language**: Python 3.12+
- **Libraries**:
  - `pandas`, `numpy`
  - `scikit-learn`
  - `joblib`

---

## 🏗️ Project Structure:
air-quality_predictor/
│
├── data/
│ └── air_quality_data.csv # Preprocessed dataset
│
├── Source/
│ ├── preprocesses.py # Data loading & preprocessing
│ ├── train_model.py # Model training & evaluation
│ └── prediction.py # Model loading and prediction
│
├── aqi_model.pkl # Saved trained model
├── main.py # Entry point for training & prediction
└── README.md # This file

# How to run

### 1️⃣ Clone the repository
```bash
1. git clone https://github.com/arpitbytes507/air-quality_predictor.git
cd air-quality_predictor

2. pip install -r requirements.txt

3. python3.main.py 

👨‍💻 Author
Arpit Dhumane
🔗 GitHub: arpitbytes507