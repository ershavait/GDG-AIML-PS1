import os
import json
import asyncio
import pandas as pd
from datetime import datetime
import websockets

# CONFIG
CSV_PATH = "data/BTCUSDT_1m.csv"
SYMBOL = "btcusdt"
INTERVAL = "1m"
WS_URL = f"wss://stream.binance.com:9443/ws/{SYMBOL}@kline_{INTERVAL}"

# Load existing CSV
def load_csv():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError("CSV not found. Run backfill.py first!")

    df = pd.read_csv(CSV_PATH)
    df["time"] = pd.to_datetime(df["time"])
    df = df.sort_values("time").drop_duplicates(subset=["time"], keep="last")
    return df

# Append new row and save
def append_and_save(df, new_row):
    df = pd.concat([df, new_row], ignore_index=True)
    df = df.drop_duplicates(subset=["time"], keep="last")
    df = df.sort_values("time")
    df = df.tail(1000)
    df.to_csv(CSV_PATH, index=False)
    return df

# WebSocket stream
async def stream_and_save():
    df = load_csv()
    print("Loaded rows:", len(df))
    print("Connecting to:", WS_URL)

    async with websockets.connect(WS_URL) as ws:
        while True:
            message = await ws.recv()
            data = json.loads(message)
            k = data["k"]

            if k["x"]:  # candle closed
                open_time = int(k["t"])

                row = {
                    "time": datetime.fromtimestamp(open_time / 1000),
                    "open": float(k["o"]),
                    "high": float(k["h"]),
                    "low": float(k["l"]),
                    "close": float(k["c"]),
                    "volume": float(k["v"]),
                }

                new_row = pd.DataFrame([row])
                df = append_and_save(df, new_row)

                print(
                    f"Saved: {row['time']} | Close={row['close']:.2f} | Rows={len(df)}"
                )

if __name__ == "__main__":
    asyncio.run(stream_and_save())
