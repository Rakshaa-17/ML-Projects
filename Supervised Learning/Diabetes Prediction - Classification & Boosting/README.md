## 🩺 Diabetes Prediction using Classification Algorithms
This project aims to predict the likelihood of diabetes in patients based on medical attributes such as glucose level, BMI, insulin levels, and more. By analyzing diagnostic data, the model assists in identifying patients at risk of developing diabetes, supporting early intervention and treatment.

### 🎯 Objective
The primary objective is to build classification models that can accurately determine whether a patient has diabetes based on health parameters. The project focuses on data preprocessing, exploratory analysis, and model building to achieve reliable classification performance.

### 🧰 Technologies Used
Language:

- Python

Libraries:

- numpy, pandas – Data manipulation 
- matplotlib, seaborn – Data visualization
- scikit-learn – Machine learning and evaluation

### 📊 Exploratory Data Analysis (EDA)

- Investigated distributions, patterns, and outliers across features like Glucose, Blood Pressure, and BMI
- Replaced unrealistic zero entries (e.g., in Glucose, Insulin, SkinThickness) with median values
- Visualized feature relationships using box plots, histograms, and correlation heatmaps
- Analyzed class balance and correlations with the target variable (Outcome)

### 🧹 Data Preprocessing

Filled missing or zero values in key columns using median imputation
Encoded categorical variables (if any)
Performed feature scaling using StandardScaler for distance-based models
Split data into training and test sets using train_test_split

### 🔍 Models Used

- Logistic Regression – For baseline binary classification
- K-Nearest Neighbors (KNN) – For instance-based learning
- Support Vector Machine (SVM) – For margin-based classification
- Random Forest Classifier – For ensemble-based predictions
- XGBoost / Gradient Boosting – For boosting performance

### 🧪 Model Evaluation
Evaluation Metrics:

- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix
- ROC-AUC Score

Performed hyperparameter tuning (e.g., GridSearchCV) and applied cross-validation to ensure model robustness and generalization.

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
