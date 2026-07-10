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



### Phase 4.3 - SQLAlchemy Connection

Completed:
- Created SQLAlchemy engine
- Configured session factory
- Created Declarative Base
- Connected FastAPI to PostgreSQL
- Added `/health` endpoint
- Verified database connectivity using `SELECT 1`
What Comes Next?

Once /health is working, we'll move to Sprint 4.4, where we'll initialize Alembic.

This is an exciting step because from then on, you'll never manually create database tables again. Every schema change will be version-controlled and managed through migrations—exactly how professional teams work.

One Small Improvement

From this sprint onward, I'd also like to introduce a CHANGELOG.md at the root of the project. The README tells the story of the project, while the changelog records version-by-version changes. It's a common practice in open-source and production projects and will make your repository even more polished.

For now, complete the /health endpoint. Once you get the expected JSON response, send me:

The JSON output from http://localhost:8000/health.
Any SQL logs that appear in the terminal (because echo=True is enabled).

🧠 What You Learned in Sprint 4.4

You introduced one of FastAPI's core design patterns:

Dependency Injection with Depends
A reusable get_db() session provider
Automatic resource cleanup using yield and finally
Cleaner, more maintainable endpoint code

These patterns will be reused throughout the project—for database access today, and later for authentication, AI clients, and configuration.

⏸️ Stop Here

After you've completed these steps, let me know:

✅ Does /health still return "database": "connected"?
✅ Did main.py work without any import or runtime errors?

### Phase 4.5 - Alembic Initialization

in the backend folder run this command
 - alembic init alembic
Completed:
- Initialized Alembic
- Created migration environment
- Created migrations folder
- Generated alembic.ini
- Verified migration structure

Outcome:
The project is now ready for version-controlled database schema migrations.


🚀 Sprint 5 Begins

This is where the project starts becoming an AI Career Agent instead of just infrastructure.

Before writing any SQLAlchemy models, we need to design the database.

This is exactly what software architects do.

Sprint 5 Goal

By the end of Sprint 5, we'll have a database like this:

                 User
                   │
         ┌─────────┴─────────┐
         │                   │
      Resume          JobApplication
         │                   │
         └──────────┐   ┌────┘
                    ▼   ▼
                   Job
                    │
                    ▼
                 Company
                    │
                    ▼
                JobMatch
Why Design First?

Suppose we start coding immediately.

After two weeks, we realize:

A job can have multiple skills.
A user can have multiple resumes.
One company has many jobs.

Changing the database later becomes painful.

Professional teams spend time designing first because it avoids expensive refactoring.

Sprint 5 Roadmap

We'll divide it into four phases.

Phase 5.1 – Database Design

We'll decide:

Which tables do we need?
What columns belong in each?
Relationships
Indexes
Constraints

No coding yet.

Phase 5.2 – SQLAlchemy Models

Convert the design into Python classes.

Example:

class Job(Base):
    ...
Phase 5.3 – Alembic Migration

Generate the first migration:

alembic revision --autogenerate -m "Initial schema"
Phase 5.4 – Apply Migration
alembic upgrade head

At that point, PostgreSQL will contain all our tables.

My Proposed Database

For our AI Career Agent, I recommend these core tables:

Table	Purpose
users	User profile and preferences
resumes	Multiple resume versions
companies	Company information
jobs	Jobs collected from LinkedIn, Naukri, etc.
job_applications	Track every application
skills	Master list of skills
job_matches	AI-generated resume/job match scores

This design supports the features you've planned:

LinkedIn scraping
Naukri scraping
Resume tailoring
Cover letter generation
Automated applications
Application tracking
AI scoring
One Architectural Improvement

Before Sprint 5.1, I'd like to add something that many tutorials skip but professional projects include:

docs/
├── architecture.md
├── database.md
├── api.md
└── roadmap.md

We'll document our architecture as we build it. This has two benefits:

You'll always have a clear reference for how the system is designed.
If this becomes an open-source project or you collaborate with others, the documentation will already be in place.
📈 Overall Progress
Infrastructure          ████████████████████ 100%

Backend Foundation      ████████████████████ 100%

Database Design         ░░░░░░░░░░░░░░░░░░░   0%

Business Logic          ░░░░░░░░░░░░░░░░░░░   0%

AI Layer                ░░░░░░░░░░░░░░░░░░░   0%

Automation              ░░░░░░░░░░░░░░░░░░░   0%

Dashboard               ░░░░░░░░░░░░░░░░░░░   0%


Sprint 5 Roadmap (Updated)

Instead of rushing into models, here's how I'd like us to proceed:

Sprint 5.1 (Current Sprint)
✅ Design the database
✅ Define relationships
✅ Create docs/database.md
🔄 Expand the document with columns, data types, enums, and ER diagram
Sprint 5.2
Create SQLAlchemy models
Add relationships (ForeignKey, relationship)
Create a shared BaseModel for common fields like id, created_at, and updated_at
Sprint 5.3
Configure Alembic
Generate the initial migration
Review the generated SQL
Sprint 5.4
Apply the migration
Verify all tables in PostgreSQL
Add seed data (a few skills and statuses)
One Last Recommendation

I'd also like to create a docs/architecture.md before we write models.

We'll capture:

Overall system architecture
Backend components
Scraper pipeline
AI pipeline
Database interactions

As the project grows, this document will become invaluable—not just for us, but for anyone else who looks at the repository.

## Sprint Progress

- ✅ Sprint 1 – Project Initialization
- ✅ Sprint 2 – Docker & PostgreSQL
- ✅ Sprint 3 – Backend Setup
- ✅ Sprint 4 – FastAPI & Database Connection
- ✅ Sprint 5.1 – Database Design
- ✅ Sprint 5.2 – SQLAlchemy Models


## Sprint 5.3 - Alembic Database Migrations

### Goal

Manage PostgreSQL schema changes using Alembic.

### Tasks

- Initialize Alembic
- Configure database connection
- Generate migrations
- Apply migrations
- Track schema changes

## Sprint 5 – Database Layer

### Completed

- Designed normalized database schema
- Implemented SQLAlchemy ORM models
- Created reusable BaseModel
- Configured Alembic
- Generated initial migration
- Applied migration to PostgreSQL
- Verified all tables successfully