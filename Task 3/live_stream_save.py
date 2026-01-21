import os
import json
import asyncio
import pandas as pd
from datetime import datetime
import websockets

# =========================
# CONFIG
# =========================
CSV_PATH = "data/BTCUSDT_1m.csv"
SYMBOL = "btcusdt"
INTERVAL = "1m"

WS_URL = f"wss://stream.binance.com:9443/ws/{SYMBOL}@kline_{INTERVAL}"


# =========================
# LOAD CSV
# =========================
def load_csv():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError("❌ CSV not found. Run backfill.py first!")

    df = pd.read_csv(CSV_PATH)

    # convert time column back to datetime
    df["time"] = pd.to_datetime(df["time"])

    # sort and remove duplicates
    df = df.sort_values("time").drop_duplicates(subset=["time"], keep="last")

    return df


# =========================
# APPEND + SAVE CSV
# =========================
def append_and_save(df, new_row):
    df = pd.concat([df, new_row], ignore_index=True)

    # remove duplicates based on time
    df = df.drop_duplicates(subset=["time"], keep="last")

    # sort again
    df = df.sort_values("time")

    # keep last 1000 rows (optional for speed)
    df = df.tail(1000)

    # save back to same CSV (constant saving)
    df.to_csv(CSV_PATH, index=False)
    return df


# =========================
# WEBSOCKET STREAM
# =========================
async def stream_and_save():
    df = load_csv()
    print("✅ Loaded existing CSV rows:", len(df))
    print("✅ WebSocket connecting:", WS_URL)

    async with websockets.connect(WS_URL) as ws:
        while True:
            message = await ws.recv()
            data = json.loads(message)

            k = data["k"]  # candle object
            is_closed = k["x"]  # True when candle closes

            # Only save when 1-minute candle closes
            if is_closed:
                open_time = int(k["t"])  # candle open time in ms

                row = {
                    "time": datetime.fromtimestamp(open_time / 1000),
                    "open": float(k["o"]),
                    "high": float(k["h"]),
                    "low": float(k["l"]),
                    "close": float(k["c"]),
                    "volume": float(k["v"]),
                }

                new_row = pd.DataFrame([row])

                # Append into dataframe + save into SAME CSV file
                df = append_and_save(df, new_row)

                print(
                    f"✅ Saved 1m candle: {row['time']} | Close={row['close']:.2f} | Rows={len(df)}"
                )


if __name__ == "__main__":
    asyncio.run(stream_and_save())
