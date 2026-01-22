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

## Installation
Run the following commands:

```bash
pip install -U chromadb yfinance pandas feedparser groq
pip install scipy sentence-transformers rfc3987
