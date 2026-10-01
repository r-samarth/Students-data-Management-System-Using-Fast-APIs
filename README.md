# Student Management System — FastAPI

A simple REST API for managing student records using **FastAPI, SQLAlchemy, and SQLite**.

## Tech stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (default)
- PostgreSQL supported through `DATABASE_URL`

## Run locally

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

Health check:

```
http://127.0.0.1:8000/health
```

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | API welcome message |
| GET | /health | Health check |
| POST | /students | Create a student |
| GET | /students | Get all students |
| GET | /students/{student_id} | Get one student |
| PUT | /students/{student_id} | Update a student |
| DELETE | /students/{student_id} | Delete a student |

### Example POST body

```json
{
  "name": "Samarth",
  "department": "CSE",
  "semester": 3
}
```

## Deploy on Render

Use these Render settings:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

For a persistent production database, set `DATABASE_URL` to a PostgreSQL connection string instead of relying on the default local SQLite database.

## Project structure

```
.
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .gitignore
└── README.md
```
