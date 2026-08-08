# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import os
import joblib
import numpy as np
import pandas as pd
from datetime import datetime


# ==========================================================
# MODEL DIRECTORY
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# ==========================================================
# LOAD ALL MODELS
# ==========================================================

def load_models():
    """Load all trained models and required files."""

    models = {

        # Farm Performance
        "farm_model": joblib.load(
            os.path.join(MODEL_DIR, "farm_performance.pkl")
        ),

        "farm_features": joblib.load(
            os.path.join(MODEL_DIR, "farm_feature_columns.pkl")
        ),

        "label_encoder": joblib.load(
            os.path.join(MODEL_DIR, "label_encoder.pkl")
        ),

        # Revenue Prediction
        "price_model": joblib.load(
            os.path.join(MODEL_DIR, "price_prediction.pkl")
        ),

        "price_features": joblib.load(
            os.path.join(MODEL_DIR, "price_feature_columns.pkl")
        ),

        # Demand Forecast
        "demand_model": joblib.load(
            os.path.join(MODEL_DIR, "demand_forecast.pkl")
        ),

        "demand_features": joblib.load(
            os.path.join(MODEL_DIR, "demand_feature_columns.pkl")
        ),

        # Forecast Seed
        "forecast_seed": joblib.load(
            os.path.join(MODEL_DIR, "forecast_seed.pkl")
        )

    }

    print("\n===== FARM FEATURES =====")
    print(models["farm_model"].feature_names_in_)

    print("\n===== PRICE FEATURES =====")
    print(models["price_model"].feature_names_in_)

    print("\n===== DEMAND FEATURES =====")
    print(models["demand_model"].feature_names_in_)

    return models


# ==========================================================
# LOAD ONCE WHEN FLASK STARTS
# ==========================================================

MODELS = load_models()

# ==========================================================
# NORMALIZE USER INPUT
# ==========================================================

def normalize_input(form_data):
    """
    Convert Flask form values into the correct data types.
    """

    data = {

        "farm_size": float(form_data.get("farm_size", 0)),

        "experience": float(form_data["experience"]),

        "total_chicks": float(form_data["total_chicks"]),

        "mortality": float(form_data["mortality"]),

        "feed": float(form_data["feed"]),

        "sales_qty": float(form_data["sales_qty"]),

        "expected_roi": float(form_data["expected_roi"]),

        "forecast_days": int(form_data["forecast_days"])

    }

    data["mortality_rate"] = calculate_mortality_rate(data)

    return data


# ==========================================================
# MORTALITY RATE
# ==========================================================

def calculate_mortality_rate(data):
    """
    Calculate mortality percentage.
    """

    if data["total_chicks"] == 0:
        return 0.0

    return round(

        (data["mortality"] / data["total_chicks"]) * 100,

        2

    )


# ==========================================================
# CREATE FARM INPUT
# ==========================================================

def create_farm_input(data):
    """
    Create DataFrame for Farm Performance model.
    """

    values = {

        "Farm_Size_Birds": data["farm_size"],

        "Experience_Years": data["experience"],

        "Total_Chicks": data["total_chicks"],

        "Total_Mortality": data["mortality"],

        "Total_Feed_Consumed": data["feed"],

        "Total_Sales_Qty": data["sales_qty"],

        "Expected_ROI_%": data["expected_roi"],

        "Mortality_Rate": data["mortality_rate"]

    }

    farm_df = pd.DataFrame([values])

    return farm_df.reindex(

        columns=MODELS["farm_features"],

        fill_value=0

    )


# ==========================================================
# CREATE PRICE INPUT
# ==========================================================

def create_price_input(data):
    """
    Create DataFrame for Revenue Prediction model.
    """

    values = {

        "Farm_Size_Birds": data["farm_size"],

        "Experience_Years": data["experience"],

        "Total_Feed_Consumed": data["feed"],

        "Total_Sales_Qty": data["sales_qty"],

        "Total_Mortality": data["mortality"],

        "Expected_ROI_%": data["expected_roi"]

    }

    price_df = pd.DataFrame([values])

    return price_df.reindex(

        columns=MODELS["price_features"],

        fill_value=0

    )

# ==========================================================
# FARM PERFORMANCE PREDICTION
# ==========================================================

def predict_performance(data):
    """
    Predict farm performance.
    """

    farm_input = create_farm_input(data)

    prediction = MODELS["farm_model"].predict(farm_input)[0]

    label = MODELS["label_encoder"].inverse_transform(
        [prediction]
    )[0]

    return {

        "farm_performance": label

    }


# ==========================================================
# REVENUE PREDICTION
# ==========================================================

def predict_revenue(data):
    """
    Predict expected revenue.
    """

    price_input = create_price_input(data)

    revenue = MODELS["price_model"].predict(
        price_input
    )[0]

    return {

        "estimated_revenue": round(float(revenue), 2)

    }


# ==========================================================
# DEMAND FORECAST
# ==========================================================

def forecast_demand(data):
    """
    Predict future demand.
    """
    try:
        seed = MODELS["forecast_seed"].copy()
        
    except Exception:
        raise Exception(
            "Unable to load forecast_seed.pkl"
            )

    forecast = []

    lag_1 = data["sales_qty"]
    lag_7 = data["sales_qty"]
    lag_14 = data["sales_qty"]

    today = datetime.today()

    for day in range(data["forecast_days"]):

        seed.loc[:, "lag_1"] = lag_1
        seed.loc[:, "lag_7"] = lag_7
        seed.loc[:, "lag_14"] = lag_14

        seed.loc[:, "rolling_mean_7"] = np.mean(
            [lag_1, lag_7]
        )

        seed.loc[:, "rolling_mean_14"] = np.mean(
            [lag_1, lag_7, lag_14]
        )

        seed.loc[:, "day"] = day + 1
        seed.loc[:, "month"] = today.month
        seed.loc[:, "weekday"] = today.weekday()

        demand_input = seed.reindex(

            columns=MODELS["demand_features"],

            fill_value=0

        )

        prediction = MODELS["demand_model"].predict(
            demand_input
        )[0]

        prediction = max(0, int(prediction))

        forecast.append(prediction)

        lag_14 = lag_7
        lag_7 = lag_1
        lag_1 = prediction

    if forecast:
        average = int(np.mean(forecast))
        peak = int(np.max(forecast))
        lowest = int(np.min(forecast))
        
    else:
        average = peak = lowest = 0

    if len(forecast) > 1:
        
        if forecast[-1] > forecast[0]:
            trend = "Increasing"
            
        elif forecast[-1] < forecast[0]:
            trend = "Decreasing"
            
        else:
            trend = "Stable"

    else:
        trend = "Stable"

    return {

        "average_demand": average,

        "peak_demand": peak,

        "lowest_demand": lowest,

        "trend": trend,

        "forecast_days": list(
            range(1, data["forecast_days"] + 1)
        ),

        "forecast_values": forecast

    }

# ==========================================================
# MAIN ANALYSIS FUNCTION
# ==========================================================

def analyze_farm(form_data):
    """
    Main function called by Flask.
    """

    try:

        # ----------------------------------------------
        # Normalize Input
        # ----------------------------------------------

        data = normalize_input(form_data)

        # ----------------------------------------------
        # Individual Predictions
        # ----------------------------------------------

        performance = predict_performance(data)
        
        revenue = predict_revenue(data)

        demand = forecast_demand(data)

        # ----------------------------------------------
        # Final Result
        # ----------------------------------------------

        result = {

            **performance,

            **revenue,

            **demand,

            "mortality_rate": data["mortality_rate"]

        }

        return result

    except Exception as e:

        raise Exception(

            f"Prediction Error : {str(e)}"

        )