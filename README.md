# 🛒 RetailPulse - AI-Powered Customer Analytics Platform

## 📌 Project Overview
RetailPulse is an end-to-end Data Science project that helps retail businesses make smarter decisions using Machine Learning and Predictive Analytics.

## 🎯 Key Features
- 📊 Customer Segmentation using K-Means Clustering
- 🔮 Demand Forecasting using Prophet & LSTM
- ⚠️ Churn Prediction using Random Forest & Logistic Regression
- 📈 Interactive Dashboard using Streamlit
- 🔬 Model Tracking using MLflow
- 🐳 Containerized using Docker

## 🛠️ Technologies Used
- Python, Pandas, NumPy
- Scikit-learn, Prophet, TensorFlow
- Streamlit, MLflow
- Docker

## 📂 Project Structure
RetailPulse/
├── data/
├── notebooks/
├── models/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

## 📊 Model Results
| Model | Accuracy | F1 Score |
|-------|----------|----------|
| Random Forest | 89.16% | 0.8665 |
| Gradient Boosting | 93.34% | 0.9112 |
| Logistic Regression | 93.43% | 0.9120 |

## 🚀 How to Run

### Local
streamlit run app.py

### Docker
docker build -t retailpulse .
docker run -p 8501:8501 retailpulse


## 👥 Team Members
1. Aditya Kumar Biling
2. Archit Narwaria
3. Mohd Sahdan
4. Srija
