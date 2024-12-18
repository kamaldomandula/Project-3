# -*- coding: utf-8 -*-
"""Monthlydata.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WzIhRJ2LU9sJGbcMq9eL2HRz6FUt0glo

### Installing the required libraries
"""

pip install pandas matplotlib seaborn prophet scikit-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

"""### Loading Daily Data"""

monthly_data = pd.read_csv(r"C:\Users\shrav\Downloads\SN_m_tot_V2.0.csv", delimiter=';', header=None)
monthly_data.columns = ["Year", "Month", "FractionalYear", "MonthlyMeanSunspotNumber", "StdDev", "Observations", "Indicator"]
monthly_data = monthly_data[monthly_data["MonthlyMeanSunspotNumber"] != -1]  # Remove missing values
monthly_data['Date'] = pd.to_datetime(monthly_data[['Year', 'Month']].assign(Day=1))
monthly_data = monthly_data[['Date', "MonthlyMeanSunspotNumber"]].rename(columns={'Date': 'ds', "MonthlyMeanSunspotNumber": 'y'})

monthly_data['y'] = monthly_data['y'].replace(0, 1e-6)  # Replace zeros with a small positive value

monthly_data['y'] = monthly_data['y'].apply(lambda x: np.log(x + 1e-6))  # Log transform with small constant

monthly_data = monthly_data[monthly_data['y'] > 0]  # Remove zero values

"""### Training the FBProphet Model"""

# Initialize Prophet Model
monthly_model = Prophet()

# Fit the model
monthly_model.fit(monthly_data)

# Create future dataframe (9 months)
future_monthly = monthly_model.make_future_dataframe(periods=9, freq='ME')

# Predict
forecast_monthly = monthly_model.predict(future_monthly)

# Predict for 1, 6, and 9 months
future_monthly_1 = monthly_model.make_future_dataframe(periods=1, freq='M')
future_monthly_6 = monthly_model.make_future_dataframe(periods=6, freq='M')
future_monthly_9 = monthly_model.make_future_dataframe(periods=9, freq='M')

# Predict 1 month
forecast_monthly_1 = monthly_model.predict(future_monthly_1)

# Predict 6 months
forecast_monthly_6 = monthly_model.predict(future_monthly_6)

# Predict 9 months
forecast_monthly_9 = monthly_model.predict(future_monthly_9)

# Visualize predictions for each forecast
fig_1 = monthly_model.plot(forecast_monthly_1)
plt.title("Sunspot Forecast: Next 1 Month")
plt.show()

fig_6 = monthly_model.plot(forecast_monthly_6)
plt.title("Sunspot Forecast: Next 6 Months")
plt.show()

fig_9 = monthly_model.plot(forecast_monthly_9)
plt.title("Sunspot Forecast: Next 9 Months")
plt.show()

# For 1 month prediction
print("Predicted values for the next 1 month:")
print(forecast_monthly_1[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1))

# For 6 months prediction
print("Predicted values for the next 6 months:")
print(forecast_monthly_6[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(6))

# For 9 months prediction
print("Predicted values for the next 9 months:")
print(forecast_monthly_9[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(9))

"""### Visualizing Predictions"""

fig = monthly_model.plot(forecast_monthly)
plt.title("Monthly Sunspot Forecasting")
plt.xlabel("Date")
plt.ylabel("Sunspot Number")
plt.show()

"""### Tune Hyperparameters : Adding custom seasonality"""

monthly_model = Prophet(growth='linear', changepoint_prior_scale=0.05)
monthly_model.add_seasonality(name='yearly', period=12, fourier_order=10)

# Fit and Predict again
monthly_model.fit(monthly_data)
forecast_monthly = monthly_model.predict(future_monthly)

"""### Evaluating Model Performance"""

y_true = monthly_data['y'].tail(9)
y_pred = forecast_monthly['yhat'][-9:]

mae = mean_absolute_error(y_true, y_pred)
mape = mean_absolute_percentage_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print(f"MAE: {mae}, MAPE: {mape}, R²: {r2}")