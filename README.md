# 💰 FinWise AI — AI-Powered Personal Finance Assistant

> An AI-powered personal finance assistant built with Python and Streamlit to help users manage expenses, plan budgets and savings, perform financial calculations, analyze spending, and receive personalized financial guidance.

🌐 **Live Demo:** https://finwise-financial-assistant.streamlit.app/

---

## 📌 Overview

**FinWise AI** is a personal finance management application that combines traditional financial planning tools with an **LLM-powered AI assistant**.

The application helps users track and analyze expenses, manage budgets, set savings goals, calculate SIP returns and loan EMIs, generate financial reports, and interact with an AI assistant for personalized financial guidance.

The project integrates **GPT OSS 20B through the OpenRouter API** and includes a **Retrieval-Augmented Generation (RAG)** component to retrieve relevant financial information and provide additional context to the language model.

---

## ✨ Key Features

- 🤖 **AI Financial Assistant** — Get AI-powered financial guidance using GPT OSS 20B.
- 💸 **Expense Analyzer** — Track expenses and understand spending patterns.
- 💰 **Budget Planner** — Create and monitor personal budgets.
- 🎯 **Savings Goal Planner** — Set and track savings goals.
- 📈 **SIP Calculator** — Calculate estimated SIP returns.
- 🏦 **EMI Calculator** — Calculate loan EMI and repayment amounts.
- 📊 **Dashboard & Reports** — View financial summaries, insights, and visualizations.
- 🔎 **RAG-based Assistance** — Retrieve relevant financial information using RAG, FAISS, and embeddings to provide additional context to the LLM.

---

## 🛠️ Tech Stack

**Languages & Framework:** Python, Streamlit

**AI & LLM:** OpenRouter API, GPT OSS 20B, LLMs, RAG, LangChain

**RAG & Embeddings:** FAISS, HuggingFace Embeddings, Sentence Transformers, all-MiniLM-L6-v2

**Data & Visualization:** Pandas, NumPy, Plotly

**Other:** REST APIs, python-dotenv, PyPDF

---

## 🧠 How It Works

FinWise AI uses the OpenRouter API to connect the application with GPT OSS 20B.

For RAG-based queries, relevant information is retrieved from the financial knowledge base using embeddings and FAISS. The retrieved context is then provided to the LLM along with the user's query to generate a more context-aware response.

```text
User Query
    ↓
Financial Context / RAG Retrieval
    ↓
Relevant Information
    ↓
GPT OSS 20B via OpenRouter
    ↓
AI Response

```


🌐 **Live Demo:** https://finwise-financial-assistant.streamlit.app/

```
## 🚀 Run Locally

```bash
git clone https://github.com/AshnaKazii/FinWise-AI.git
cd FinWise-AI
pip install -r requirements.txt
streamlit run app.py

---
```
## 👩‍💻 Author

**Ashna Kazi**

B.Tech Information Technology Student @ SAKEC

🔗 [GitHub](https://github.com/AshnaKazii)  
🔗 [LinkedIn](https://www.linkedin.com/in/ashna-kazi/)
