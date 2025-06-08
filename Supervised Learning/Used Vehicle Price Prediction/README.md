## Used Vehicle Price Prediction using Regression Algorithms

This project aims to predict the prices of used vehicles based on various features such as vehicle age, mileage, brand, fuel type, and transmission. By analyzing historical vehicle listing data, we build regression models that help estimate a car's value — aiding both buyers and sellers in making informed decisions.

## 🎯 Objective

The primary objective is to develop regression models that accurately predict used vehicle prices based on their specifications and conditions. The project includes data cleaning, feature engineering, visualization, and model tuning to optimize performance.

### 🧰 Technologies Used

**Language:**
- Python

**Libraries:**
- `numpy`, `pandas` – Data manipulation
- `matplotlib`, `seaborn` – Data visualization
- `scikit-learn` – Machine learning and evaluation

### 📊 Exploratory Data Analysis (EDA)

- Investigated relationships between key features (year, mileage, brand, fuel type) and price
- Checked for missing or inconsistent values and handled them accordingly
- Encoded categorical variables such as brand, transmission, and fuel type
- Detected and treated outliers in price and mileage distributions

### 🔍 Models Used

- **Linear Regression** – For baseline performance
- **Decision Tree Regressor** – To handle non-linear patterns
- **Random Forest Regressor** – For better accuracy through ensemble learning

### 🧪 Model Evaluation

**Metrics Used:**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Additional Steps:
- Performed train-test split for validation
- Tuned hyperparameters using Grid Search
- Compared model performance to select the best approach

### 🛠 Future Enhancements

- Integrate **XGBoost** or **LightGBM** for improved performance
- Add more detailed car condition metrics (e.g., service history, accident records)
- Deploy the model using **Flask** or **Streamlit** for interactive web use
- Enable dynamic user inputs for instant price prediction

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)



