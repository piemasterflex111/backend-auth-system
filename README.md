# Backend Auth System

Minimal production-style FastAPI backend.

## Stack

- Python 3.x
- FastAPI
- Uvicorn
- Virtual Environment
- Git Versioned

## Endpoints

GET / → Service running  
GET /health → Health check  

## Run Locally

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload


