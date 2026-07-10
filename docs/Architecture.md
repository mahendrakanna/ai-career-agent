# AI Career Agent - Backend Architecture

## Objective

This document defines the architecture, coding standards, and design principles used throughout the project.

The goal is to keep the project:

- Maintainable
- Scalable
- Consistent
- Easy to extend

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.14 |
| Backend | FastAPI |
| ORM | SQLAlchemy 2.x |
| Database | PostgreSQL 16 |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Containerization | Docker |
| Automation | Apify + Playwright |
| AI | OpenAI API |
| Version Control | Git |

---

# Architecture

Presentation Layer
↓
FastAPI

↓

Service Layer

↓

Database Layer

↓

PostgreSQL

External Services

↓

Apify

LinkedIn

Naukri

OpenAI

---

# Design Principles

- Separation of Concerns
- DRY (Don't Repeat Yourself)
- Single Responsibility Principle
- Explicit is better than implicit
- Configuration via Environment Variables
- Type Safety
- Dependency Injection

---

# Engineering Standards

- UUID Primary Keys
- UTC Timestamps
- Snake Case Naming
- SQLAlchemy Declarative Models
- Alembic for Schema Changes
- Environment Variables for Secrets
- Docker for Local Development

---

# Documentation Policy

Every sprint must update:

- README.md
- Relevant file inside docs/


# Database Standards

## Primary Keys

All tables use UUID.

Reason:

- Globally unique
- Production ready
- Secure
- Better for distributed systems

---

## Timestamps

Every table contains

- created_at
- updated_at

Both stored in UTC.

---

## Foreign Keys

Foreign key names follow:

<table_name>_id

Examples:

user_id

company_id

resume_id

job_id

---

## Naming Convention

Tables:

snake_case

Example:

job_applications

Columns:

snake_case

Example:

created_at

Relationships:

Plural

Example:

jobs

applications

skills


# Backend Structure

backend/

app/

api/

core/

db/

models/

schemas/

services/

utils/

main.py

Purpose:

api/

HTTP Routes

core/

Configuration

db/

Database

models/

SQLAlchemy Models

schemas/

Pydantic Schemas

services/

Business Logic

utils/

Helper Functions

# SQLAlchemy Standards

Every model:

- Inherits from BaseModel
- Uses UUID Primary Keys
- Uses UTC timestamps
- Has __tablename__
- Uses SQLAlchemy relationships
- Does not contain business logic

Business logic belongs inside the service layer.

# Environment Variables

Never hardcode:

- Database Passwords
- API Keys
- Tokens
- Secrets

Always use:

.env

Development:

.env

Production:

Environment Variables


# Git Workflow

Every sprint:

Create Feature

Implement

Test

Update Documentation

Commit

Push

Commit Message Format

feat:

fix:

docs:

refactor:

test:

# Error Handling

Never swallow exceptions.

Raise meaningful exceptions.

Log unexpected errors.

Return appropriate HTTP status codes.

# Logging

Development:

INFO

Production:

WARNING

ERROR

Never print secrets.

Never log passwords or API keys.

# our Development workflow 

Requirement
      ↓
Architecture
      ↓
Design
      ↓
Implementation
      ↓
Testing
      ↓
Documentation
      ↓
Git Commit

# Engineering Notes

This project is intentionally built using professional software engineering practices.

The objective is not only to create an AI Career Agent but also to serve as a learning resource for backend architecture, automation, AI integration, and scalable application design.

# API Layer

The API layer uses Pydantic schemas to separate external data contracts from internal SQLAlchemy models.

Benefits:

- Input validation
- Response serialization
- Security (hide internal fields)
- Automatic OpenAPI documentation