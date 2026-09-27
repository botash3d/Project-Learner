# Learning App: Build Plan

> One app that turns any curriculum into an interactive graph of topics, tracks your progress, shows how curricula overlap, and suggests career paths and projects.

**Status:** Planning · **Budget:** 30–45 min/day · **Target:** Live V1 in about 6–7 weeks

---

## 🧰 Tech Stack

### Frontend

| Tech | Logo | Purpose |
|---|---|---|
| React | ![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black) | UI components and pages |
| TypeScript | ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white) | Type safety |
| Vite | ![Vite](https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white) | Dev server and build |
| React Router | ![React Router](https://img.shields.io/badge/React_Router-CA4245?logo=reactrouter&logoColor=white) | Page routing |
| Tailwind CSS | ![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white) | Styling |
| TanStack Query | ![TanStack Query](https://img.shields.io/badge/TanStack_Query-FF4154?logo=reactquery&logoColor=white) | Server data fetching and caching |
| React Flow | ![React Flow](https://img.shields.io/badge/React_Flow-FF0072?logoColor=white) | Interactive graph rendering |

### Backend

| Tech | Logo | Purpose |
|---|---|---|
| Python | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Backend language |
| FastAPI | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) | REST API |
| SQLAlchemy | ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logoColor=white) | ORM and database access |
| Pydantic | ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white) | Request and response validation |
| Alembic | ![Alembic](https://img.shields.io/badge/Alembic-6C6C6C?logoColor=white) | Database migrations |

### Database and Deployment

| Tech | Logo | Purpose |
|---|---|---|
| PostgreSQL | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) | Relational data (curricula, nodes, edges, progress) |
| Docker | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) | Packaging and deployment |

---

## 🔌 APIs

### Internal REST endpoints (V1)

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/curricula` | List all curricula |
| `GET` | `/api/curricula/{id}/graph` | Get nodes and edges for one curriculum |
| `GET` | `/api/progress` | Get the user's progress |
| `PUT` | `/api/progress/{node_id}` | Mark a node done or not done |
| `GET` | `/api/curricula/{id}/coverage` | Get the coverage percentage |

### Later endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/compare?a={id}&b={id}` | Overlap between two curricula |
| `GET` | `/api/career-paths` | Career paths and what they unlock |
| `CRUD` | `/api/admin/*` | Admin panel editing |

### External APIs (optional, later)

| Service | Logo | Used for |
|---|---|---|
| Claude API | ![Claude](https://img.shields.io/badge/Claude_API-D97757?logoColor=white) | Hint layer for the DSA feature |
| LeetCode (community library) | ![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?logo=leetcode&logoColor=black) | Live DSA problems with fallback |

---

## 🗺️ Phases

| Phase | Name | Time | What it builds |
|---|---|---|---|
| 1 | 🗄️ Data and graph foundation | ~2 weeks | Database schema, migrations, one seeded curriculum, graph read endpoint |
| 2 | 🕸️ Roadmap viewer | ~2 weeks | React Flow graph with zoom, pan, and node detail panel |
| 3 | ✅ Progress and coverage | ~1–2 weeks | Mark nodes done, coverage percentage per curriculum |
| 4 | 🚀 Deploy and ship | ~1 week | Docker setup, live public URL, first YouTube episode |

**Total to live V1:** about 6–7 weeks

### Phase details

**Phase 1: Data and graph foundation**
- Define tables: `curricula`, `nodes`, `edges`, `users`, `progress`
- Write the first Alembic migration
- Seed one curriculum from a JSON file
- Expose `GET /api/curricula/{id}/graph`

**Phase 2: Roadmap viewer**
- Build the Roadmap Viewer page
- Render nodes and edges with React Flow
- Add zoom, pan, and a node detail panel

**Phase 3: Progress and coverage**
- Add the user model and progress endpoints
- Add checkboxes or toggles on nodes
- Calculate coverage as done nodes divided by total nodes

**Phase 4: Deploy and ship**
- Dockerize the backend and frontend
- Deploy a live version
- Record the first YouTube episode

---

## 🔭 Later (not scheduled)

- Compare curricula (overlap and unique topics)
- Career paths and what they unlock
- Project suggestions per topic
- Admin panel for editing roadmaps
- DSA lock feature (phone lock + PC judge)

These stay unscheduled until V1 ships.
