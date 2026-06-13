# Finance Coding Lab

AI-powered financial coding lab for automating Excel workflows, reconciliation, and building production-ready data tools.

------------------------------------------------------------------------

## 🚀 Features

- Excel reconciliation automation
- Financial data processing with Python
- API development using FastAPI
- AI-powered explanations of discrepancies
- Scalable backend architecture (Docker, PostgreSQL)
- JWT authentication system
- Async SQLAlchemy integration
- Alembic database migrations
- Dockerized PostgreSQL environment
- Role-based access system (admin/user)
- Production-oriented backend architecture

------------------------------------------------------------------------

## 📁 Project Structure

learning/ → Input/output files + Experiments and analysis
backend/ → API + AI
frontend/ → UI
docker/ → infrastructure

------------------------------------------------------------------------

📁 Backend Structure
1.backend/
│
├── alembic/                 → Database migrations
├── app/
│   │
│   ├── api/                 → API routers aggregation
│   ├── auth/                → JWT auth + dependencies
│   ├── core/                → Config + security + settings
│   ├── db/                  → Database session + Base
│   ├── models/              → SQLAlchemy models
│   ├── routes/              → FastAPI routes
│   ├── services/            → Business logic layer
│   ├── schemas/             → Pydantic schemas
│   └── utils/               → Utility functions
│
├── requirements.txt
├── .env
├── alembic.ini
└── README.md

------------------------------------------------------------------------

## 🛠️ Tech Stack

🛠️ Tech Stack
Python 3.12.9
FastAPI
PostgreSQL
SQLAlchemy (Async)
Alembic
Docker
JWT Authentication
Passlib / bcrypt
React (Frontend)
AI (LLM / Copilot)

------------------------------------------------------------------------

## ▶️ Getting Started

``` bash
git clone https://github.com/userikzhan/finance-coding-lab.git
cd finance-coding-lab
docker-compose up --build
```

------------------------------------------------------------------------

## 🎯 Goals

-   Replace Excel workflows with code
-   Build scalable financial tools
-   Learn production-level backend development

------------------------------------------------------------------------

## 📌 Status

🚧 In development
