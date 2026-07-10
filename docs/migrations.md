# Database Migrations

## Migration Tool

Alembic

Purpose:

- Version control database schema
- Automatically generate migrations
- Apply schema updates safely
- Roll back changes if needed

## Migration 001 - Initial Database Schema

Generated using:

```bash```
alembic revision --autogenerate -m "Initial database schema"  

## Purpose:

- Create all application tables
- Add primary keys
- Add foreign keys
- Add indexes
- Establish relationships

## Migration 001

Revision:
30399fece5b5

Description:

Initial database schema

Created:

- users
- resumes
- companies
- jobs
- skills
- resume_skills
- job_skills
- job_applications
- job_matches

Applied Successfully