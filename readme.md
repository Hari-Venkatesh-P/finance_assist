# Finance Assist 💰

An AI-powered Personal Finance Assistant that analyzes bank transaction emails, generates embeddings, stores them in a vector database, and enables conversational financial insights using Retrieval-Augmented Generation (RAG).

---

## Overview

Finance Assist automatically fetches transaction-related emails from Gmail, converts them into structured financial context, generates vector embeddings using Google's Gemini Embedding Model, and allows users to ask natural language questions about their spending, income, merchants, and financial activity.

Examples:

* How much did I spend on medical expenses?
* What are my biggest expenses this week?
* Show all transactions above ₹1,000.
* How much money was credited to my account?
* Which merchants did I spend the most money with?

---

## Features

### Gmail Integration

* Connects to Gmail using Gmail API
* Fetches emails from a configured Gmail label
* Supports automated transaction ingestion

### Transaction Processing

* Extracts financial transaction details from bank emails
* Cleans and normalizes email content
* Converts transactions into embedding-friendly text

### Vector Search

* Generates embeddings using Gemini Embedding API
* Stores vectors in FAISS index
* Supports semantic retrieval

### Conversational Finance Assistant

* Uses RAG architecture
* Retrieves relevant transactions
* Generates natural language financial insights using Gemini

### REST APIs

* Sync latest transaction emails
* Rebuild embeddings and index
* Ask finance-related questions

---

# Architecture

```text
                    ┌─────────────┐
                    │   Gmail     │
                    │ Transaction │
                    │   Emails    │
                    └──────┬──────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Gmail API Fetcher  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Transaction Parser │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Embedding Builder  │
                │ Gemini Embeddings  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    FAISS Index     │
                └─────────┬──────────┘
                          │
                          ▼
                    User Query
                          │
                          ▼
                ┌────────────────────┐
                │    Retriever       │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Gemini 2.0 Flash   │
                └─────────┬──────────┘
                          │
                          ▼
                    AI Response
```

---

# Technology Stack

| Component        | Technology           |
| ---------------- | -------------------- |
| Backend          | FastAPI              |
| LLM              | Gemini 2.0 Flash     |
| Embeddings       | Gemini Embedding 001 |
| Vector Store     | FAISS                |
| Email Source     | Gmail API            |
| Language         | Python               |
| Deployment       | Google Cloud Run     |
| Containerization | Docker               |

---

# Project Structure

```text
finance-assist/

├── app/
│   ├── api/
│   ├── services/
│   ├── gmail/
│   ├── embeddings/
│   ├── rag/
│   └── models/
│
├── finance_index/
│
├── credentials/
│
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# API Endpoints

## Sync Emails

Fetch latest transaction emails from Gmail.

```http
POST /sync
```

Response

```json
{
  "status": "success",
  "emails_fetched": 125
}
```

---

## Rebuild Index

Creates embeddings and rebuilds the FAISS index.

```http
POST /reindex
```

Response

```json
{
  "status": "success",
  "documents_indexed": 125
}
```

---

## Chat

Ask finance-related questions.

```http
POST /chat
```

Request

```json
{
  "question": "What are my top expenses this week?"
}
```

Response

```json
{
  "answer": "Your highest expense was ₹10,000 at Thangamayil Jewellery."
}
```

---

# Local Setup

## Clone Repository

```bash
git clone <repository-url>

cd finance-assist
```

## Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=<gemini_api_key>

LABEL_NAME=Finance

GMAIL_CLIENT_SECRET=<gmail_secret>
```

---

# Run Application

```bash
uvicorn main:app --reload
```

Application will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Docker

Build image

```bash
docker build -t finance-assist .
```

Run container

```bash
docker run -p 8080:8080 finance-assist
```

---

# Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* Gmail API Integration
* FastAPI Development
* LLM Integration
* FAISS Vector Store
* Docker Containerization
* Cloud Deployment

---

# Disclaimer

This project is intended for personal finance analysis purposes only. Users should verify all financial information independently before making financial decisions.
