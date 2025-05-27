# 📦 E-Commerce Shipping Prediction using Classification Algorithms

This project focuses on predicting whether an order in an e-commerce system will be delivered on time based on customer and shipping details. Using classification models, the goal is to help businesses optimize their logistics and improve customer satisfaction by identifying factors that affect shipping delays.

### 🎯 Objective

To develop a machine learning classification model that can:

* Predict whether an order will be delivered on time or not
* Identify the most influential features affecting delivery performance
* Help logistics teams make informed decisions to reduce late deliveries

### 🧰 Technologies Used

**Language:**

* Python

**Libraries:**

* `pandas`, `numpy` – Data manipulation and analysis
* `matplotlib`, `seaborn` – Data visualization and EDA
* `scikit-learn` – Preprocessing, modeling, and evaluation
* `xgboost` – Advanced boosting model for classification tasks

### 📊 Exploratory Data Analysis (EDA)

* Analyzed key features such as delivery time, product importance, warehouse location, and shipping mode
* Visualized class distribution for the target variable `Reached.on.Time_Y.N`
* Checked for class imbalance and performed basic data cleaning
* Encoded categorical variables (Label Encoding/One-Hot Encoding as needed)
* Detected feature correlations and outliers


### 🔍 Classification Models Used

| Model                    | Description                              |
| ------------------------ | ---------------------------------------- |
| Logistic Regression      | Linear model for binary classification   |
| Decision Tree Classifier | Rule-based tree model for quick insights |
| Random Forest Classifier | Ensemble learning for robust performance |
| XGBoost Classifier       | Gradient boosting for optimal accuracy   |


### 🧪 Model Evaluation

**Metrics Used:**

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

**Techniques:**

* Train-test split
* Feature importance analysis
* Model comparison to determine best performance

### 🔑 Key Insights

* High importance of product type and delivery time on delivery success
* Class imbalance required attention to ensure fair evaluation
* XGBoost and Random Forest performed better than simpler models
* Feature engineering and preprocessing greatly affected outcomes


### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)

