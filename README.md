# ai-career-agent
to automate job finding and apply 

# AI Career Agent

## Project Status

🚧 Under active development.
## Vision

AI Career Agent is an end-to-end automation platform that helps software engineers discover jobs, analyze job descriptions, tailor resumes, generate cover letters, and automate job applications using AI.

## Features (Planned)

- Job scraping (LinkedIn & Naukri)
- AI resume optimization
- Cover letter generation
- Application tracking
- Dashboard
- Local LLM with Ollama
- n8n workflow automation
- PostgreSQL database
- FastAPI backend
- Dockerized deployment

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Docker
- n8n
- Ollama
- Streamlit
- Apify

#  tools to install
- docker 
- docker compose 
- python, pip 
- node, npm


# Postgres DB connection
- docker exec -it career-postgres psql -U career_user -d career_agent


1. Project Overview
2. Vision
3. Tech Stack
4. Architecture
5. Project Roadmap
6. Sprint Log
7. How to Run
8. Current Status
9. Next Sprint

# Sprint Log

---

## Sprint 0 - Repository Setup ✅

### Goal

Set up the project repository and Git configuration.

### Completed

- Created GitHub repository
- Cloned repository locally
- Configured local Git username
- Configured local Git email
- Connected repository to GitHub
- Successfully pushed first commit

### Learnings

- Difference between global and local Git configuration
- Difference between Git commit identity and GitHub authentication
- Repository-level Git configuration

### Deliverable

A working Git repository connected to GitHub.

---

## Sprint 1 - Project Foundation ✅

### Goal

Create the initial project structure.

### Completed

- Created project folders
- Added `.gitignore`
- Added `.env.example`
- Added `LICENSE`
- Added initial `docker-compose.yml`
- Created project documentation

### Learnings

- Why a clean folder structure matters
- Why we keep secrets in `.env`
- Why Docker Compose is used

### Deliverable

Project skeleton ready for development.

---

## Sprint 2 - PostgreSQL Infrastructure ✅

### Goal

Run PostgreSQL locally using Docker.

### Completed

- Created `database/`
- Created `database/init`
- Configured PostgreSQL Docker container
- Configured persistent Docker volume
- Added environment variables
- Successfully connected to PostgreSQL

### Commands Used

```bash```
docker compose config
docker compose up -d
docker ps
docker logs career-postgres
docker exec -it career-postgres psql -U career_user -d career_agent

# verification 
SELECT version();
\l
\q

Sprint 3 - FastAPI Backend 🚧
Goal

Create the first backend API.

Planned Tasks
Create backend folder structure
Create Python virtual environment
Install FastAPI
Install Uvicorn
Create first API
Test API
Open Swagger documentation
Expected Deliverable

Open:

http://localhost:8000

Response:

{
    "application": "AI Career Agent",
    "version": "0.1.0",
    "status": "running"
}

---

# Add another section at the end

```markdown
# Engineering Notes

At the end of every sprint we will:

1. Review what we built.
2. Understand why we designed it that way.
3. Plan the next sprint.

Each sprint should leave the repository in a working state.

No sprint ends with broken code.
Why I want this

This project isn't just about getting an AI to apply for jobs. It's also about creating something you can confidently show to a recruiter or hiring manager.

A well-maintained README.md demonstrates:

You can plan work in iterations.
You document technical decisions.
You keep a record of progress.
You understand software engineering practices, not just coding.

By the time we finish, your GitHub repository will tell the story of how the project evolved, making it much more compelling than a repository that simply contains code.

One more suggestion

As the project grows, I'd also like to add a docs/ folder with dedicated documents:

docs/
├── architecture.md      # System architecture and design decisions
├── roadmap.md           # Overall project roadmap
├── sprint-log.md        # Detailed sprint history
├── setup.md             # Local environment setup
├── api.md               # Backend API documentation
└── database.md          # Database schema and relationships


Sprint 3 - FastAPI Backend
Sprint Goal

By the end of this sprint, we want this architecture:

Browser
    │
    ▼
http://localhost:8000
    │
    ▼
FastAPI

No PostgreSQL integration yet.

No AI.

No n8n.

Just a healthy backend.

Step 1 - Create the Backend Structure

From the project root:

mkdir backend
mkdir backend\app
mkdir backend\app\api
mkdir backend\app\core
mkdir backend\app\models
mkdir backend\app\schemas
mkdir backend\app\services
mkdir backend\app\agents
mkdir backend\app\scrapers
mkdir backend\app\utils
Why these folders?
Folder	Purpose
app	Main application code
api	API routes/endpoints
core	Configuration, settings, logging
models	Database models (SQLAlchemy later)
schemas	Request/response models (Pydantic)
services	Business logic
agents	AI agents
scrapers	LinkedIn/Naukri integrations
utils	Common helper functions

This separation keeps the code organized as it grows.

Step 2 - Create Python Files
ni backend\app\main.py
ni backend\requirements.txt
ni backend\.env.example
ni backend\.gitignore
Step 3 - Create a Virtual Environment

Move into the backend directory:

cd backend

Create the virtual environment:

python -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1

You should now see:

(.venv) PS C:\...
Why a Virtual Environment?

This project should be self-contained.

Instead of installing Python packages globally, everything stays inside:

backend/
    .venv/

If you clone the project on another machine later, you can recreate the exact same environment.

Step 4 - Install the First Dependencies
pip install fastapi uvicorn

Freeze the dependencies:

pip freeze > requirements.txt

Your requirements.txt should contain FastAPI, Uvicorn, and their dependencies.

Step 5 - Create the First API

Open:

backend/app/main.py

Replace the contents with:

from fastapi import FastAPI

app = FastAPI(
    title="AI Career Agent",
    version="0.1.0",
    description="Local-first AI-powered job automation platform"
)

@app.get("/")
def root():
    return {
        "application": "AI Career Agent",
        "version": "0.1.0",
        "status": "running"
    }
Step 6 - Run the API

From the backend folder:

uvicorn app.main:app --reload

Expected output:

INFO:     Uvicorn running on http://127.0.0.1:8000
Step 7 - Verify

Open these URLs:

Home
http://localhost:8000

Expected response:

{
    "application": "AI Career Agent",
    "version": "0.1.0",
    "status": "running"
}
Swagger UI
http://localhost:8000/docs

You should see FastAPI's interactive API documentation.

Step 8 - Update README

Add a new section under Sprint 3 documenting:

Backend folder structure
Virtual environment setup
FastAPI installation
Uvicorn server
Root endpoint
Swagger documentation

This keeps the README synchronized with the project's progress.

Step 9 - Commit

Once everything works:

git add .
git commit -m "feat(api): initialize FastAPI backend"
git push origin main