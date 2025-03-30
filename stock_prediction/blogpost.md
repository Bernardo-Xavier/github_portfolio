# How I Built a Stock Price Predictor with LSTM and SHAP Analysis

## 🔍 The Problem
Stock market prediction remains notoriously difficult due to:
- Non-linear price movements
- High noise-to-signal ratio
- Sensitivity to external events

Traditional models like ARIMA struggle with these complexities. Could deep learning do better?

## 🧠 My Approach
I developed an **LSTM neural network** with:
- **Temporal feature engineering**: Created 20+ technical indicators (SMA, EMA, MACD)
- **Optuna hyperparameter tuning**: Automated search for optimal architecture
- **SHAP interpretability**: Explained model decisions quantitatively