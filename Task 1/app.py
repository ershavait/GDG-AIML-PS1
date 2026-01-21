import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Task 1 - ARIMA Forecast", layout="wide")

# Live Data Function (yfinance)
@st.cache_data(ttl=300)
def fetch_close(symbol, period="1y"):
    df = yf.download(symbol, period=period, interval="1d", progress=False)
    if df is None or df.empty:
        return None
    return df["Close"].dropna()

# UI
st.title("📈 Task 1: ARIMA Forecast (Live yfinance)")
st.caption("Type any Yahoo Finance ticker (example: RELIANCE.NS, ^NSEI, AAPL)")

st.sidebar.header("Inputs")

# INPUT
selected_symbol = st.sidebar.text_input(
    "Enter Yahoo Finance Ticker",
    value="RELIANCE.NS"
).strip()

period = st.sidebar.selectbox(
    "History Period",
    ["6mo", "1y", "2y", "5y"],
    index=1
)

st.sidebar.header("ARIMA Parameters")
forecast_days = st.sidebar.slider("Forecast Days", 3, 14, 7)
p = st.sidebar.number_input("p (AR)", 0, 5, 5)
d = st.sidebar.number_input("d (I)", 0, 2, 1)
q = st.sidebar.number_input("q (MA)", 0, 5, 5)

st.subheader(f"📌 Selected Symbol: {selected_symbol}")

if selected_symbol == "":
    st.warning("⚠️ Please enter a ticker symbol in sidebar.")
    st.stop()


# Load Data
close = fetch_close(selected_symbol, period=period)

if close is None or close.empty:
    st.error("❌ Could not fetch data. Check ticker symbol / internet connection.")
    st.stop()

close = close.dropna()

# Plot Historical Closing Prices
st.subheader("📊 Historical Closing Prices")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(close.index, close, label=f"{selected_symbol} Close")
ax1.legend()
st.pyplot(fig1)

# Train ARIMA and  Forecast
st.subheader("🔮 Historical Prediction and Forecast")

with st.spinner("Training ARIMA model..."):
    model = ARIMA(close, order=(p, d, q))
    fit = model.fit()

    historical_pred = fit.get_prediction(
        start=close.index[1],
        end=close.index[-1]
    ).predicted_mean

    forecast = fit.get_forecast(steps=forecast_days)
    forecast_mean = forecast.predicted_mean
    conf_int = forecast.conf_int()

future_dates = pd.date_range(
    start=close.index[-1],
    periods=forecast_days + 1,
    freq="B"
)[1:]

forecast_mean.index = future_dates
conf_int.index = future_dates

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(close.index, close, label="Actual", linewidth=2)
ax2.plot(historical_pred.index, historical_pred, linestyle="--", label="Predicted (Historical)")

ax2.fill_between(
    future_dates,
    conf_int.iloc[:, 0],
    conf_int.iloc[:, 1],
    alpha=0.3,
    label="Confidence Interval"
)

ax2.plot(forecast_mean.index, forecast_mean, linewidth=3, label="Forecast")
ax2.legend()
st.pyplot(fig2)

st.success("✅ Forecast generated successfully")