# 📊 Customer Churn Prediction

An end-to-end Machine Learning web application that predicts whether a telecom customer is likely to churn based on customer demographics, subscription details, and billing information.

The project includes data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, a Flask web application, and deployment.

---

## 🚀 Demo

🔗 Live Demo: *https://customer-churn-prediction-849g.onrender.com*

---

## 📌 Problem Statement

Customer churn is one of the biggest challenges for subscription-based businesses. Acquiring new customers is significantly more expensive than retaining existing ones.

This project predicts whether a customer is likely to leave the telecom service, enabling businesses to identify high-risk customers and take proactive retention measures.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

Features include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

Target Variable:

- Churn (Yes / No)

---

# 📈 Exploratory Data Analysis

Performed:

- Missing Value Analysis
- Data Cleaning
- Feature Engineering
- Correlation Analysis
- Univariate Analysis
- Bivariate Analysis
- Outlier Detection
- Feature Distribution Visualization

Libraries Used:

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 🤖 Machine Learning Models

The following classification algorithms were trained and compared:

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost
- Extra Trees
- XGBoost
- CatBoost

Hyperparameter tuning was performed using GridSearchCV.

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

# 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- XGBoost
- CatBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Backend

- Flask

### Deployment

- Render

---

# 📁 Project Structure

```
Customer-Churn-Prediction
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── notebook/
│   └── Customer_Churn_EDA.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── setup.py
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/abishekak18/Customer-Churn-Prediction.git
```

Move to the project folder

```bash
cd Customer-Churn-Prediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 💻 Web Application

The Flask application allows users to:

- Enter customer details
- Predict customer churn
- Display prediction results with confidence score

---

# 📊 Results

The trained model successfully predicts customer churn using customer subscription and billing information.

The application can help businesses:

- Identify customers at risk of leaving
- Improve customer retention
- Support business decision-making

---

# 📦 Future Improvements

- SHAP Explainability
- LIME Explanation
- Batch CSV Prediction
- Interactive Dashboard
- Docker Support
- CI/CD using GitHub Actions
- AWS Deployment
- User Authentication

---

# 👨‍💻 Author

**Abishek E**

GitHub:
https://github.com/abishekak18

LinkedIn:
https://www.linkedin.com/in/eabishek18/

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
