# Energy Generation Forecasting using LSTM and RNN Models

This project focuses on forecasting energy generation from fossil gas using time series data. The dataset includes energy generation records and weather features, which are used to train and evaluate Long Short-Term Memory (LSTM) and Recurrent Neural Network (RNN) models. The project involves data preprocessing, feature engineering, model training, and evaluation.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Installation](#installation)

## Project Overview
The goal of this project is to predict future energy generation from fossil gas using historical data and weather features. The project employs LSTM and RNN models to capture temporal dependencies in the data. The models are evaluated using various metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared (R²).

## Dataset
The dataset consists of two main files:
- **energy_dataset.csv**: Contains time-stamped energy generation data.
- **weather_features.csv**: Contains weather-related features such as temperature, humidity, and weather descriptions.

The datasets are merged based on the timestamp, and only the data for the city of Madrid is used.

## Methodology
1. **Data Preprocessing**:
   - Handling missing values.
   - Removing leading and trailing zeros/NaNs.
   - Feature engineering: Extracting datetime features (hour, day of week, etc.).
   - Scaling: Both MinMaxScaler and StandardScaler are used to normalize the data.

2. **Model Building**:
   - **LSTM Model**: A two-layer LSTM model with dropout for regularization.
   - **RNN Model**: A two-layer SimpleRNN model with dropout.

3. **Model Training**:
   - The models are trained using different loss functions: MSE, MAE, and Huber loss.
   - The training process includes validation to monitor overfitting.

4. **Evaluation**:
   - The models are evaluated on a test set using metrics such as MSE, MAE, MAPE, SMAPE, and R².

## Results
The results of the models are summarized in a CSV file (`model_results.csv`), which includes the following metrics for each model:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)
- Symmetric Mean Absolute Percentage Error (SMAPE)
- R-squared (R²)
- Training time

## Installation
To run this project, you need to have Python installed along with the following libraries:
- pandas
- numpy
- scikit-learn
- tensorflow
- matplotlib

You can install the required libraries using pip:
```bash
pip install pandas numpy scikit-learn tensorflow matplotlib