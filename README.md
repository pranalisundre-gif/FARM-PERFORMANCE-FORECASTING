<p align="center">
  <img src="assets/project-banner.png" width="100%">
</p>

<h1 align="center">🐔 Farm Performance & Forecasting</h1>

<p align="center">
  A machine learning powered Flask application for analyzing farm performance, forecasting future demand, and predicting product prices.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-4CAF50?style=for-the-badge)
![Data Science](https://img.shields.io/badge/Data%20Science-6C63FF?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📖 Project Overview

**Farm Performance & Forecasting** is an end-to-end data science and machine learning application designed to support data-driven poultry farm management.

The application combines historical farm data with machine learning models to provide three major analytical capabilities:

- 🐔 **Farm Performance Scoring**
- 📈 **Demand Forecasting**
- 💰 **Price Prediction**

A Flask web application provides an interactive interface through which users can access the analytics and prediction modules.

The project follows a complete machine learning workflow from data preprocessing and exploratory analysis to feature engineering, model development, prediction, and web application integration.

---

## 🎯 Project Objectives

- Analyze overall farm performance using relevant farm metrics.
- Generate a farm performance score.
- Forecast future demand for poultry products.
- Predict future product prices.
- Convert machine learning outputs into an easy-to-use web application.
- Support better planning and data-driven farm decisions.

---

# 🧠 Main Modules

## 1️⃣ Farm Performance Scoring

The Farm Performance module evaluates farm-level information and generates an overall performance score.

The analysis considers operational parameters such as:

- Flock Size
- Mortality Rate
- Age of Flock
- Feed Conversion Ratio (FCR)
- Average Body Weight
- Vaccination Status

The application presents an overall performance score along with category-level performance information.

### Purpose

The module helps identify areas where farm performance can be improved and provides a summarized view of operational performance.

---

## 2️⃣ Demand Forecasting

The Demand Forecasting module estimates future demand based on historical demand patterns.

Users can provide forecasting parameters and generate future demand estimates for a selected forecast period.

### Output

The application provides:

- Forecast Date
- Forecasted Demand
- Lower Bound
- Upper Bound

This allows users to understand expected future demand as well as the forecast range.

### Purpose

Demand forecasting can support:

- Production planning
- Inventory planning
- Resource allocation
- Future operational decisions

---

## 3️⃣ Price Prediction

The Price Prediction module estimates future poultry product prices using historical information and the trained prediction model.

Users can select the required product and forecasting period to generate predicted prices.

### Output

The application provides:

- Prediction Date
- Predicted Price
- Lower Bound
- Upper Bound

### Purpose

Price prediction can support:

- Pricing decisions
- Revenue planning
- Market planning
- Future business decisions

---

# 🔄 Machine Learning Workflow

The project follows the following workflow:

```text
Raw Farm Data
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Model Development
      ↓
Farm Performance Scoring
      ↓
Demand Forecasting
      ↓
Price Prediction
      ↓
Flask Web Application
      ↓
Interactive Results
```

---

# 📓 Notebook Workflow

The project contains separate notebooks for different stages of development:

```text
01_data_preprocessing.ipynb
        ↓
02_EDA.ipynb
        ↓
03_feature_engineering.ipynb
        ↓
04_farm_performance_scoring.ipynb
        ↓
05_demand_forecasting.ipynb
        ↓
06_price_prediction.ipynb
```

### Notebook 01 — Data Preprocessing

Prepares the source data for analysis and machine learning.

### Notebook 02 — EDA

Explores the available data and identifies relevant patterns and relationships.

### Notebook 03 — Feature Engineering

Creates and prepares features required by the machine learning models.

### Notebook 04 — Farm Performance Scoring

Develops the farm performance scoring component.

### Notebook 05 — Demand Forecasting

Develops the demand forecasting component.

### Notebook 06 — Price Prediction

Develops the price prediction component.

---

# 🌐 Web Application

The machine learning components are integrated into a Flask web application.

### Application Pages

The application includes:

- 🏠 Home
- 📊 Dashboard
- 🐔 Farm Performance
- 📈 Demand Forecasting
- 💰 Price Prediction
- ℹ️ About

---

# 📊 Dashboard

The dashboard provides a centralized overview of farm analytics.

The application dashboard presents information such as:

- Overall Performance Score
- Flock Size
- Mortality Rate
- Feed Conversion Ratio
- Profitability
- Performance Trends
- Performance Categories
- Mortality Trends
- Demand Forecast
- Price Prediction

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Machine Learning | Python ML Libraries |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Frontend | HTML, CSS, JavaScript |
| Model Storage | Pickle (`.pkl`) |
| Development | Jupyter Notebook / VS Code |

---

# 📂 Project Structure

```text
Farm-Performance-and-Forecasting
│
├── app.py
├── predictor.py
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── demand_feature_columns.pkl
│   ├── demand_forecast.pkl
│   ├── farm_feature_columns.pkl
│   ├── farm_performance.pkl
│   ├── forecast_seed.pkl
│   ├── label_encoder.pkl
│   ├── price_feature_columns.pkl
│   └── price_prediction.pkl
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_farm_performance_scoring.ipynb
│   ├── 05_demand_forecasting.ipynb
│   └── 06_price_prediction.ipynb
│
├── static/
│   ├── images/
│   │   └── hero-farm.png
│   ├── dashboard.css
│   ├── script.js
│   └── style.css
│
└── templates/
    ├── dashboard.html
    └── home.html
```

---

# 📸 Application Preview

## 🏠 Home Page

<p align="center">
  <img src="static/images/hero-farm.png" width="90%">
</p>

---

## 📊 Dashboard

The dashboard provides a centralized view of farm performance and forecasting information.

---

## 🐔 Farm Performance

The Farm Performance module accepts farm information and generates an overall performance score with category-level results.

---

## 📈 Demand Forecasting

The Demand Forecasting module generates future demand estimates along with forecast ranges.

---

## 💰 Price Prediction

The Price Prediction module generates future price estimates along with prediction ranges.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/pranaliundre-gif/Farm-Performance-and-Forecasting.git
```

## 2. Navigate to the Project

```bash
cd Farm-Performance-and-Forecasting
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

If a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies required by the project environment.

## 5. Run the Flask Application

```bash
python app.py
```

## 6. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 💡 Business Applications

The system demonstrates how machine learning can support poultry farm decision-making through:

### Better Planning

Use demand forecasts to support future production and resource planning.

### Performance Monitoring

Use farm performance scores to identify areas requiring attention.

### Price Planning

Use predicted prices to support future pricing and revenue decisions.

### Data-Driven Decisions

Combine historical data, machine learning predictions, and interactive analytics to support operational decisions.

---

# 🔮 Future Enhancements

Potential future improvements include:

- Real-time farm data integration.
- Automated model retraining.
- Live market price integration.
- Additional farm performance metrics.
- Advanced forecasting models.
- Model explainability.
- Automated data refresh.
- Cloud deployment.
- Mobile-friendly application enhancements.
- Role-based access for farm managers and administrators.

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience in:

- Python
- Machine Learning
- Data Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Forecasting
- Predictive Analytics
- Flask Web Development
- Model Integration
- Data Visualization
- Business Analytics
- End-to-End ML Application Development

---

# 👩‍💻 Author

**Pranali Undre**

Information Technology Student

### Areas of Interest

- Data Science
- Machine Learning
- Data Analytics
- Artificial Intelligence
- Business Intelligence

### GitHub

https://github.com/pranaliundre-gif

### LinkedIn

_Add your LinkedIn profile URL here._

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the **MIT License**.