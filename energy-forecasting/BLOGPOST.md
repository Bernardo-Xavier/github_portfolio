# Energy Generation Forecasting with LSTM and RNN Models

In this blog post, I will walk you through my recent project on forecasting energy generation from fossil gas using Long Short-Term Memory (LSTM) and Recurrent Neural Network (RNN) models. The goal of this project was to predict future energy generation based on historical data and weather features.

## Introduction
Energy generation forecasting is crucial for grid management and energy trading. Accurate predictions can help in optimizing energy production and reducing costs. In this project, I used time series data from an energy dataset and weather features to train and evaluate LSTM and RNN models.

## Data Preprocessing
The dataset consisted of two main files: `energy_dataset.csv` and `weather_features.csv`. The energy dataset contained time-stamped energy generation data, while the weather dataset included various weather-related features. I merged these datasets based on the timestamp and focused on the data for Madrid.

### Handling Missing Values
I started by handling missing values in the dataset. I removed leading and trailing rows where the target column (energy generation) had zeros or NaNs. Then, I filled the remaining missing values with the mean of the respective columns.

### Feature Engineering
I extracted several datetime features such as hour, day of the week, month, and day of the year. These features help the model capture temporal patterns in the data.

### Scaling
I used both MinMaxScaler and StandardScaler to normalize the data. Scaling is essential for neural networks as it helps in faster convergence during training.

## Model Building
I built two types of models: LSTM and RNN. Both models had two layers with dropout for regularization. The models were trained using different loss functions: Mean Squared Error (MSE), Mean Absolute Error (MAE), and Huber loss.

## Model Training
The models were trained for 100 epochs with a batch size of 32. I used the Adam optimizer and monitored the validation loss to prevent overfitting.

## Evaluation
The models were evaluated on a test set using various metrics:
- **Mean Squared Error (MSE)**: Measures the average squared difference between the predicted and actual values.
- **Mean Absolute Error (MAE)**: Measures the average absolute difference between the predicted and actual values.
- **Mean Absolute Percentage Error (MAPE)**: Measures the percentage difference between the predicted and actual values.
- **Symmetric Mean Absolute Percentage Error (SMAPE)**: Similar to MAPE but symmetric.
- **R-squared (R²)**: Measures the proportion of variance in the dependent variable that is predictable from the independent variables.

## Results
The results showed that the LSTM model performed slightly better than the RNN model. The best results were obtained using the MinMaxScaler and the Huber loss function. The detailed results are available in the `model_results.csv` file.

## Conclusion
This project demonstrated the effectiveness of LSTM and RNN models in forecasting energy generation. The models were able to capture temporal dependencies in the data and provide accurate predictions. Future work could involve experimenting with more complex models and incorporating additional features.