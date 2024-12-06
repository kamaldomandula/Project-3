INTRO TO DATA SCIENCE
# Project-3
Optimized Code

Sunspots Forecasting with Facebook Prophet

Overview
This project implements a Time Series Forecasting Model using Facebook's Prophet library to predict sunspot activity. Sunspots are temporary phenomena on the Sun's photosphere, appearing as dark spots caused by intense magnetic activity. Their occurrence varies cyclically, typically following an 11-year solar cycle. Prophet, a robust time series forecasting tool, is utilized in this project to analyze and forecast sunspot data based on an additive model with support for non-linear trends, yearly, weekly, and daily seasonality, as well as external holiday effects.


Objectives
To analyze historical sunspot data and identify patterns.
To predict future sunspot activity using Facebook Prophet.
To visualize and interpret trends, seasonality, and uncertainties in the forecast.


Features
Data Preparation: Formatting the dataset for Prophet's requirements.
Forecasting: Predicting future sunspot activity with confidence intervals.
Visualizations:
Trend analysis over time.
Seasonal patterns, including the solar cycle.
Forecast component breakdown (trend, yearly seasonality).
Evaluation: Assessing model accuracy using performance metrics like Mean Absolute Error (MAE).


Tools and Libraries
Python
pandas: Data manipulation.
matplotlib: Visualization.
prophet: Time series forecasting.
