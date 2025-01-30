# Predictive Analytics for Customer Churn

## Introduction
Customer churn, also known as customer attrition, is a critical metric for businesses. It refers to the percentage of customers who stop using a company's products or services over a specific period. Predicting churn is essential for businesses to retain customers and improve profitability. In this project, I built a machine learning model to predict customer churn using a telecom dataset.

## Dataset
The dataset used in this project is `customer_churn_dataset-testing-master.csv`. It contains information about telecom customers, including features like `MonthlyCharges`, `TotalCharges`, `tenure`, and `Churn` (the target variable).

## Approach
### 1. Data Exploration
I started by exploring the dataset to understand its structure and identify missing values. Visualizations were created using libraries like `seaborn` and `matplotlib` to analyze the distribution of the target variable (`Churn`) and other features.

### 2. Data Preprocessing
- **Handling Missing Values**: The dataset had no missing values, so no imputation was required.
- **Encoding Categorical Variables**: Categorical features were encoded using `LabelEncoder`.
- **Feature Scaling**: Numerical features were standardized using `StandardScaler`.

### 3. Model Training
I trained three machine learning models:
- **Logistic Regression**
- **Random Forest**
- **XGBoost**

### 4. Model Evaluation
The models were evaluated using metrics like accuracy, precision, recall, F1-score, and ROC AUC score. The XGBoost model performed the best with an ROC AUC score of 0.92.

### 5. Feature Importance
Using the XGBoost model, I identified the most important features influencing churn. The top features were:
- `Payment Delay`
- `Support Calls`
- `Tenure`

## Challenges
- **Imbalanced Data**: The dataset was imbalanced, with fewer churned customers compared to non-churned customers. Techniques like oversampling or class weighting could be applied in the future to address this issue.
- **Model Selection**: Choosing the best model required careful evaluation of multiple algorithms.

## Results
The XGBoost model achieved the highest ROC AUC score of 0.92. The key insights from the project are:
- Customers with higher `MonthlyCharges` are more likely to churn.
- Longer `tenure` reduces the likelihood of churn.
- `TotalCharges` is a strong predictor of churn.

## Conclusion
This project demonstrates the power of machine learning in predicting customer churn. By identifying key factors influencing churn, businesses can take proactive measures to retain customers and improve profitability. The code and documentation for this project are available on [GitHub](https://github.com/Bernardo-Xavier/customer-churn-prediction).