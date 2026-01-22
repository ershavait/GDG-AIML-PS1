## ✅ Task 1: Stock Forecasting Web App (Streamlit + ARIMA)
A Streamlit-based forecasting app that takes any **Yahoo Finance ticker** as input and:
- downloads historical closing prices using `yfinance`
- trains an **ARIMA(p, d, q)** model
- shows historical predictions + future forecast with confidence interval

File:
- `app.py` :contentReference[oaicite:0]{index=0}

---

## ✅ Task 2: Finance Assistant Notebook (Groq API + News + Vector Search)
A notebook-based finance assistant that combines:
- stock/market data
- finance news ingestion (RSS feeds)
- vector database storage + similarity search (ChromaDB)
- response generation using **Groq API**

File:
- `chatbotgroqapi.ipynb`

---

## ✅ Task 3: BTCUSDT Real-Time Data Pipeline (Backfill + WebSocket)
A data collection pipeline for **BTCUSDT 1-minute OHLCV** candles from Binance:
- Backfill script downloads historical candles (REST API)
- Live script streams real-time candles (WebSocket)
- Saves everything into a clean CSV file (deduplicated + sorted)

Files:
- `backfill.py`
- `live_stream_save.py`

---

## Repository Structure (overview)
- `Task 1` → Forecasting web app
- `Task 2` → Notebook-based finance assistant
- `Task 3` → Real-time crypto dataset generation
