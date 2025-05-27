## 📉 Customer Churn Prediction using Classification Algorithms
This project focuses on predicting customer churn—whether a customer is likely to stop using a service—based on their demographics, service usage, and account information. By leveraging classification algorithms, the goal is to help businesses proactively retain customers and reduce churn rates.

### 🎯 Objective
To develop a machine learning classification model that can:
- Identify customers at risk of churning
- Highlight the most influential factors contributing to churn
- Assist stakeholders in customer retention strategy

### 🧰 Technologies Used
Language:

- Python

Libraries:

- pandas, numpy – Data loading and manipulation
- matplotlib, seaborn – Exploratory Data Analysis (EDA)
- scikit-learn – Preprocessing, modeling, evaluation
- imblearn – Handling class imbalance
- xgboost – Advanced classification model

### 📊 Exploratory Data Analysis (EDA)
- Examined customer demographics, service subscriptions, and churn distribution
- Handled missing values and data inconsistencies
- Converted categorical variables using one-hot encoding and label encoding
- Balanced the dataset using SMOTE to address class imbalance

### 🔍 Models Used
- Model	Description
- Logistic Regression	Interpretable baseline model
- K-Nearest Neighbors	Instance-based learning
- Decision Tree Classifier	Rule-based classification
- Random Forest Classifier	Ensemble method for better accuracy
- XGBoost Classifier	Gradient boosting for optimal performance

### 🧪 Model Evaluation
Metrics Used:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

Techniques:
Cross-validation
SMOTE (Synthetic Minority Oversampling Technique)
Feature Importance analysis for model interpretation

### 🔑 Key Insights
- Features such as tenure, contract type, and monthly charges were strong indicators of churn
- Ensemble models like Random Forest and XGBoost outperformed simple classifiers
- SMOTE significantly improved model performance on imbalanced data

### 🧑‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
