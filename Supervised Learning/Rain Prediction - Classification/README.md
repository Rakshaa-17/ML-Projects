## 🌧️ Rain Prediction using Classification Algorithms
This project focuses on predicting whether it will rain the next day based on historical weather data. By using supervised machine learning classification techniques, the aim is to support weather forecasting and planning efforts, especially in agriculture and event management.

### 🎯 Objective
To develop a machine learning classification model that can:

- Predict if it will rain tomorrow (RainTomorrow)
- Analyze key weather-related factors influencing rainfall
- Provide a data-driven tool for proactive weather-based decision making

### 🧰 Technologies Used
Language:

Python

Libraries:
- pandas, numpy – Data analysis and cleaning
- matplotlib, seaborn – Exploratory Data Analysis (EDA)
- scikit-learn – Preprocessing, modeling, evaluation
- xgboost – Advanced gradient boosting classifier

### 📊 Exploratory Data Analysis (EDA)
- Investigated feature distributions and weather trends
- Handled missing values and outliers in numerical and categorical data
- Visualized correlations between weather indicators and rainfall
- Transformed categorical features using label encoding
- Checked target class distribution (RainTomorrow)

### 🔍 Classification Models Used
- Model	Description
- Logistic Regression	Baseline linear classification model
- Decision Tree Classifier	Rule-based decision making
- Random Forest Classifier	Ensemble of trees for better accuracy
- XGBoost Classifier	Boosted trees for high-performance modeling

### 🧪 Model Evaluation
Metrics Used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Techniques:

- Train-test split
- Feature importance ranking
- Model comparison to select best-performing algorithm

### 🔑 Key Insights

- Features like Humidity3pm, RainToday, and Pressure9am were highly correlated with next-day rain
- Data cleaning and encoding had a strong impact on model performance
- XGBoost and Random Forest outperformed simpler models in predicting rainfall
- Balanced evaluation metrics were essential due to class imbalance in the target variable

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)  
