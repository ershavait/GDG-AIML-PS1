import os
import requests
import pandas as pd
from datetime import datetime

SYMBOL = "BTCUSDT"
INTERVAL = "1m"
LIMIT = 500  # number of candles (max 1000)

CSV_PATH = "data/BTCUSDT_1m.csv"


def backfill_to_csv():
    os.makedirs("data", exist_ok=True)

    # If CSV already exists, don’t overwrite
    if os.path.exists(CSV_PATH):
        print("✅ CSV already exists:", CSV_PATH)
        return

    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": SYMBOL, "interval": INTERVAL, "limit": LIMIT}

    print("📥 Fetching historical candles from Binance...")
    res = requests.get(url, params=params, timeout=10)
    res.raise_for_status()
    data = res.json()

    rows = []
    for candle in data:
        open_time = candle[0]   # ms
        open_p = float(candle[1])
        high_p = float(candle[2])
        low_p = float(candle[3])
        close_p = float(candle[4])
        volume = float(candle[5])

        rows.append({
            "time": datetime.fromtimestamp(open_time / 1000),
            "open": open_p,
            "high": high_p,
            "low": low_p,
            "close": close_p,
            "volume": volume
        })

    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)

    print("✅ Backfill done. Saved to:", CSV_PATH)
    print(df.tail(5))


if __name__ == "__main__":
    backfill_to_csv()
