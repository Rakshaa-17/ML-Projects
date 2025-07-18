## Customer Churn Prediction using Artificial Neural Networks (ANN)
This project focuses on predicting customer churn—whether a customer is likely to stop using a service—based on their demographics, account activity, and service-related features. By leveraging a deep learning-based artificial neural network (ANN), the aim is to help businesses proactively retain customers and reduce churn rates by identifying at-risk individuals.

### 🎯 Objective
- To develop an Artificial Neural Network (ANN) model that can:
- Accurately predict customers who are likely to churn
- Learn complex, non-linear relationships from the data
- Support business decision-making in customer retention strategies

### 🧰 Technologies Used
Language:
Python

Libraries:
- pandas, numpy – Data loading and preprocessing
- matplotlib, seaborn – Data visualization and EDA
- scikit-learn – Preprocessing, model evaluation
- TensorFlow, Keras – Building and training the ANN model

### 📊 Exploratory Data Analysis (EDA)
- Analyzed features such as geography, gender, tenure, balance, number of products, and active membership
- Checked for data imbalance and skewed distributions
- Applied Label Encoding and One-Hot Encoding for categorical variables
- Scaled numerical features using StandardScaler for optimal neural network performance

### 🧠 Model Architecture: Artificial Neural Network (ANN)
 Layer Type	           Details
- Input Layer	      Accepts 11 numerical/categorical features
- Hidden Layer 1	   Dense layer with ReLU activation
- Hidden Layer 2	   Dense layer with ReLU activation
 Output Layer	     Dense layer with sigmoid activation

-Optimizer: Adam
-Loss Function: Binary Crossentropy
-Epochs: 100
-Batch Size: 10

### 🧪 Model Evaluation
Metrics Used:
     - Accuracy
     - Precision
     - Recall
     - F1-Score
     - Confusion Matrix

### Techniques:
- Train-Test Split (80-20)
- Feature scaling to optimize training
- Threshold tuning for binary classification

### 🔑 Key Insights
- Customers with lower tenure, higher balance, and specific geographical locations showed a higher tendency to churn
- The ANN model was able to capture complex feature interactions better than traditional models
- Feature scaling significantly improved ANN convergence and performance
- Model achieved high accuracy and generalization on test data

  ### 🧑‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
