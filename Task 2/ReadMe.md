# 📌 Finance News + Stock Assistant (Groq API)

This project is a simple finance assistant built in a Jupyter Notebook.  
It can fetch stock prices, read finance/news updates, store context using a vector database, and generate responses using the Groq API.

---

## Features
- Fetch stock market data using **yfinance**
- Read finance/news content using **RSS feeds**
- Store and search information using **ChromaDB**
- Generate answers using **Groq API**
- Sentence embeddings using **sentence-transformers**

---

## Requirements
- Python 3.9+
- Jupyter Notebook / Google Colab
- Active internet connection

---

## How to Run

1. Open the project folder in VS Code / Jupyter / Colab.
2. Open the notebook file:
   - `chatbotgroqapi.ipynb`
3. Install required libraries by running the installation cell (or use terminal):

   ```bash
   pip install -U chromadb yfinance pandas feedparser groq
   pip install scipy sentence-transformers rfc3987

4. Add your **Groq API key** in the notebook where required.
5. Run all cells in order (top to bottom).
6. Enter your finance queries (stocks/news) and check the output responses.
