# Ipl_First_Inning_score_predictor
# 🏏 IPL First Innings Score Predictor

A Machine Learning-based web application that predicts the expected final score of an IPL team's first innings based on the current match situation.

The project uses **XGBoost Regression** to predict the first-innings score using match features such as current score, wickets remaining, balls left, current run rate, and runs scored in the last five overs.

The application is built using **Python and Streamlit**, providing a simple and interactive interface for users.

## 📌 Project Overview

In cricket, predicting the final innings score depends on several factors, including the current score, remaining deliveries, wickets in hand, and recent scoring performance.

This project uses historical IPL ball-by-ball data to train a machine learning model that estimates the final first-innings score from the current match situation.

### 🎯 Objectives

- Analyze historical IPL ball-by-ball data.
- Perform data preprocessing and feature engineering.
- Train a regression model using XGBoost.
- Evaluate model performance using R² Score and Mean Absolute Error.
- Build an interactive web application using Streamlit.
- Predict the expected final score based on user inputs.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Data preprocessing and model pipeline |
| XGBoost | Machine learning regression model |
| Matplotlib / Seaborn | Data visualization |
| Streamlit | Web application |
| Pickle | Saving and loading the trained model |
| Jupyter Notebook | Model development and experimentation |

## 📊 Features Used for Prediction

The model uses the following eight features:

| Feature | Description |
|---|---|
| batting_team | Team currently batting |
| bowling_team | Team currently bowling |
| curr_score | Current innings score |
| ball_left | Number of balls remaining |
| wickets_left | Number of wickets remaining |
| curr | Current run rate |
| last_five | Runs scored in the last 30 deliveries |
| city | Match venue city |

Categorical features such as batting team, bowling team, and city are converted into numerical representations using One-Hot Encoding.

## 🤖 Machine Learning Model

The project uses **XGBoost Regressor**, a gradient-boosting algorithm based on decision trees.

The model is trained using a preprocessing pipeline consisting of:

1. **ColumnTransformer:** Applies One-Hot Encoding to categorical features.
2. **StandardScaler:** Scales the transformed features.
3. **XGBRegressor:** Predicts the expected final innings score.

### Model Evaluation

The model was evaluated using a test dataset.

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.9197 |
| Mean Absolute Error (MAE) | 4.44 |

These results indicate that the model explains approximately 91.97% of the variation in the test-set target scores, with an average absolute prediction error of approximately 4.44 runs.

## 🖥️ Application Features

- Select batting and bowling teams.
- Select the match city.
- Enter the current score.
- Enter completed overs and balls in the current over.
- Enter wickets lost.
- Enter runs scored in the last five overs.
- Get the predicted final first-innings score.

## 📁 Project Structure

```text
IPL-First-Innings-Score-Predictor/
│
├── app.py
├── pipe.pkl
├── Feature_extraction.ipynb
├── requirements.txt
└── README.md
```

**File descriptions:**

- `app.py` – Streamlit application.
- `pipe.pkl` – Exported trained machine learning pipeline.
- `Feature_extraction.ipynb` – Data preprocessing, feature engineering, model training, and evaluation.
- `requirements.txt` – Required Python libraries.
- `README.md` – Project documentation.

## 📦 Requirements

The main dependencies are:

```text
streamlit
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
```

## 🔮 Future Improvements

- Integrate live IPL match data.
- Improve predictions using additional match-related features.
- Compare different regression algorithms.
- Improve the user interface and visualization.
- Deploy the application online for public access.

## 👨‍💻 Author

**Suraj Kumar**

Computer Science and Engineering (Data Science)

## ⭐ Acknowledgement

This project was developed as a practical application of machine learning, data preprocessing, feature engineering, and regression techniques using Python.

---

*If you find this project interesting, consider giving the repository a star! ⭐*
