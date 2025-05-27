# 💊 Drug Classification using Supervised Learning
This project focuses on predicting the most suitable drug to prescribe to a patient based on their medical attributes. By leveraging classification algorithms, the goal is to assist healthcare providers in making informed, data-driven decisions for medication prescription.

### 🎯 Objective
To develop a machine learning classification model that can:

- Predict the type of drug suitable for a patient based on their profile
- Identify which features (age, BP, cholesterol, Na/K levels) most influence drug decisions
- Enhance decision-making in clinical settings using data science techniques

### 🧰 Technologies Used
Language:

- Python

Libraries:

- pandas, numpy – Data handling and preprocessing
- matplotlib, seaborn – Data visualization and EDA
- scikit-learn – Preprocessing, modeling, evaluation
- xgboost – Gradient Boosting for classification

### 📊 Exploratory Data Analysis (EDA)

- Explored relationships between age, BP, cholesterol, Na_to_K ratio, and target drug
- Handled categorical features using Label Encoding
- Visualized distributions and feature importance
- Checked class balance in target variable
- Performed train-test split for model validation

### 🔍 Classification Models Used
Model	Description
Logistic Regression	Interpretable linear classifier
Decision Tree Classifier	Rule-based decision-making model
Random Forest Classifier	Ensemble model for improved performance
XGBoost Classifier	Boosted trees for high accuracy

### 🧪 Model Evaluation
Metrics Used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Techniques:

- Feature scaling (as required)
-Train/Test Split for evaluation
-Feature Importance for model interpretation

### 🔑 Key Insights
- Drug Y and Drug X were most commonly prescribed, requiring accurate classification
- Na_to_K ratio had a strong impact on the type of drug prescribed
- Ensemble methods like Random Forest and XGBoost delivered better classification performance
- Simple models like Logistic Regression offered good baseline accuracy with high interpretability

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
