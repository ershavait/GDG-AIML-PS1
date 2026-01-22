# 📈 BTCUSDT 1-Minute Data Collector (Binance)

This project collects **BTCUSDT 1-minute OHLCV data** from Binance and saves it into a CSV file.

It works in 2 parts:
1) **Backfill (historical candles)** → creates the CSV first time  
2) **Live WebSocket stream** → keeps updating the same CSV with latest closed candles

---

## ✅ What this project does
- Fetches **historical 1m candles** from Binance REST API
- Saves the data into: `data/BTCUSDT_1m.csv`
- Connects to Binance WebSocket for **live 1m candles**
- Appends only **closed candles** into the CSV
- Removes duplicates and keeps data sorted

---

## 📂 Files in this project
- `backfill.py` → downloads historical candles and creates the CSV :contentReference[oaicite:0]{index=0}  
- `live_stream_save.py` → streams live candles and updates the same CSV :contentReference[oaicite:1]{index=1}  

---

## ⚙️ Requirements
- Python 3.9+
- Internet connection (Binance API + WebSocket)
 

## 🚀 How to Run  

```bash
# 1) Install dependencies
pip install pandas requests websockets

# 2) Run backfill (creates historical CSV)
python backfill.py
# This will create:
# data/BTCUSDT_1m.csv  :contentReference[oaicite:0]{index=0}

# 3) Run live stream (updates CSV continuously)
python live_stream_save.py
# This will connect to Binance WebSocket and keep appending closed 1-minute candles
# into the same CSV file  :contentReference[oaicite:1]{index=1}

# 4) Stop live streaming
# Press: CTRL + C


