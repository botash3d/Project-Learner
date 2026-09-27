# Project Learner

An interactive, graph-based curriculum roadmap. Pick a curriculum, see its topics laid out as a dependency graph, mark what you've covered, and track your coverage as you go.

**Live app:** https://project-learner-jade.vercel.app/
**Live API docs:** https://project-learner-gymi.onrender.com

> Note: both the frontend and backend run on free-tier hosting, so the first load after a period of inactivity can take 10–30 seconds while the services wake up. Subsequent loads are fast.

---

## What it does

- Renders a curriculum as an interactive, zoomable graph, with edges showing prerequisite relationships between topics
- Click any topic to mark it done or not done
- Live coverage percentage — updates instantly as you toggle topics
- Currently seeded with a full **Python Path** curriculum (15 topics, 14 prerequisite relationships)

---

## Tech Stack

**Frontend:** React, TypeScript, Vite, TanStack Query, React Flow, Tailwind CSS

**Backend:** Python, FastAPI, SQLAlchemy, Alembic, Pydantic

**Database:** PostgreSQL (Neon, serverless)

**Deployment:** Vercel (frontend), Render (backend), Docker

---

## Architecture

```
Frontend (Vercel)  →  Backend API (Render)  →  PostgreSQL (Neon)
   React + Vite         FastAPI                  Serverless Postgres
```

The backend exposes a REST API for curriculum graphs, progress tracking, and coverage calculation. The frontend fetches this data and renders it as an interactive graph using React Flow, with TanStack Query handling caching and refetching.

---

## Running locally

### Prerequisites
- Docker Desktop
- Node.js
- Python 3.11+

### 1. Clone the repo

```bash
git clone https://github.com/botash3d/Project-Learner.git
cd Project-Learner
```

### 2. Start Postgres

```bash
docker compose up -d postgres
```

### 3. Set up the backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Create a `.env` file in `backend/`:

```
DATABASE_URL=postgresql+psycopg://learning_app:dev_password@localhost:5432/learning_app_db
```

Run migrations and seed the database:

```bash
alembic upgrade head
python -m app.seed
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

The API is now running at `http://localhost:8000` (interactive docs at `/docs`).

### 4. Set up the frontend

```bash
cd frontend
npm install
npm run dev
```

The app is now running at `http://localhost:5173`.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/curricula/{id}/graph` | Get a curriculum's nodes and edges |
| `GET` | `/api/curricula/{id}/progress` | Get progress for a curriculum |
| `PUT` | `/api/progress/{node_id}` | Mark a node done or not done |
| `GET` | `/api/curricula/{id}/coverage` | Get coverage percentage |

---

## Roadmap

Planned, not yet built:

- [ ] Custom node styling
- [ ] Admin panel for editing curricula
- [ ] Compare curricula (overlap and unique topics)
- [ ] Career paths and what they unlock
- [ ] Project suggestions per topic
- [ ] Real user accounts

---

## About

Built by [Ashwani](https://github.com/botash3d) — ML & Robotics Engineer, currently pursuing a B.Sc. in Data Science and AI at IIT Guwahati.