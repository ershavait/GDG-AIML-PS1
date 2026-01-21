# 📈 Task 1: ARIMA Forecasting (Live Yahoo Finance Data)

This project is a **Streamlit web app** that performs **time-series forecasting** using the **ARIMA model** on **live stock/market data** fetched from **Yahoo Finance (yfinance)**.

Users can enter any valid Yahoo Finance ticker (example: `RELIANCE.NS`, `^NSEI`, `AAPL`) and get:

✅ Historical closing price chart  
✅ ARIMA model historical prediction  
✅ Future forecast for selected number of days  
✅ Confidence interval for forecast  

---

## 🚀 Features

- Live market data using **yfinance**
- Interactive UI using **Streamlit Sidebar**
- ARIMA forecasting with adjustable parameters: **p, d, q**
- Forecast range: **3 to 14 business days**
- Plotting using **Matplotlib**
- Uses caching for fast performance (`st.cache_data`)

---

## 🛠️ Tech Stack / Libraries Used

- **Python**
- **Streamlit** (Web UI)
- **Pandas** (Data handling)
- **yfinance** (Live market data)
- **Matplotlib** (Plots)
- **statsmodels** (ARIMA Model)

---

## 📂 Project Structure

