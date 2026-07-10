# AI Career Agent Database Design

## Objective

Design a scalable database to support:

- Resume management
- Job scraping
- AI job matching
- Resume tailoring
- Cover letter generation
- Automated job applications
- Application tracking

---

## Core Entities

- User
- Resume
- Company
- Job
- Job Application
- Skill
- Job Match

---

## Relationships

User
└── Resume

Company
└── Job

Resume
└── Job Application

Job
└── Job Application

Resume
↔ Job Match ↔ Job

1. Add an ER Diagram

Let's make the document visual.

Add this after Relationships:

+---------+
|  users  |
+---------+
     |
     | 1
     |
     | N
+-----------+
| resumes   |
+-----------+
     |
     | 1
     |
     | N
+-------------------+
| job_applications  |
+-------------------+
     |
     | N
     |
     | 1
+--------+
| jobs   |
+--------+
     |
     | N
     |
     | 1
+-----------+
| companies |
+-----------+

resumes ----< job_matches >---- jobs
2. We Need More Fields

Right now we only have entity names.

Let's define every table properly.

For example:

users
Column	Type	Notes
id	UUID	Primary Key
name	VARCHAR	
email	VARCHAR	Unique
created_at	TIMESTAMP	
updated_at	TIMESTAMP	
resumes
Column	Type
id	UUID
user_id	UUID
name	VARCHAR
file_path	TEXT
parsed_text	TEXT
summary	TEXT
created_at	TIMESTAMP
updated_at	TIMESTAMP


1. users

Purpose: Stores user profile information.

Column	Type	Constraints	Description
id	UUID	PK	Unique user ID
full_name	VARCHAR(255)	NOT NULL	User's full name
email	VARCHAR(255)	UNIQUE, NOT NULL	Login email
phone	VARCHAR(20)	NULL	Contact number
location	VARCHAR(255)	NULL	Current location
linkedin_url	TEXT	NULL	LinkedIn profile
github_url	TEXT	NULL	GitHub profile
portfolio_url	TEXT	NULL	Portfolio website
created_at	TIMESTAMP	NOT NULL	Record creation
updated_at	TIMESTAMP	NOT NULL	Last update
2. resumes

Purpose: Stores all resume versions.

Column	Type	Constraints	Description
id	UUID	PK	Resume ID
user_id	UUID	FK → users.id	Owner
resume_name	VARCHAR(255)	NOT NULL	Resume name
file_path	TEXT	NOT NULL	PDF location
parsed_text	TEXT	NULL	Extracted text
summary	TEXT	NULL	AI summary
resume_type	VARCHAR(50)	NULL	Master, Tailored, ATS
version	INTEGER	DEFAULT 1	Resume version
is_active	BOOLEAN	DEFAULT TRUE	Current resume
created_at	TIMESTAMP	NOT NULL	Created
updated_at	TIMESTAMP	NOT NULL	Updated
3. companies

Purpose: Company master data.

Column	Type	Constraints	Description
id	UUID	PK	Company ID
company_name	VARCHAR(255)	NOT NULL	Company name
website	TEXT	NULL	Official website
linkedin_url	TEXT	NULL	LinkedIn page
careers_url	TEXT	NULL	Careers page
industry	VARCHAR(100)	NULL	Industry
company_size	VARCHAR(50)	NULL	Startup, Mid, Enterprise
headquarters	VARCHAR(255)	NULL	HQ
created_at	TIMESTAMP	NOT NULL	Created
updated_at	TIMESTAMP	NOT NULL	Updated
4. jobs (Most Important Table)

Purpose: Every scraped job.

Column	Type	Constraints	Description
id	UUID	PK	Job ID
company_id	UUID	FK → companies.id	Company
title	VARCHAR(255)	NOT NULL	Job title
platform	VARCHAR(50)	NOT NULL	LinkedIn, Naukri, etc.
employment_type	VARCHAR(50)	NULL	Full-time, Contract
work_mode	VARCHAR(50)	NULL	Remote, Hybrid, Onsite
experience_level	VARCHAR(50)	NULL	Fresher, Mid, Senior
experience_required	VARCHAR(50)	NULL	3-5 Years
salary_min	DECIMAL	NULL	Minimum salary
salary_max	DECIMAL	NULL	Maximum salary
currency	VARCHAR(10)	NULL	INR, USD
location	VARCHAR(255)	NULL	Job location
job_url	TEXT	UNIQUE	Original URL
description	TEXT	NOT NULL	Job description
requirements	TEXT	NULL	Requirements
posted_date	DATE	NULL	Posted by company
scraped_at	TIMESTAMP	NOT NULL	Scraped time
is_active	BOOLEAN	DEFAULT TRUE	Job availability
created_at	TIMESTAMP	NOT NULL	Created
updated_at	TIMESTAMP	NOT NULL	Updated
5. job_applications

Purpose: Tracks every application.

Column	Type	Constraints	Description
id	UUID	PK	Application ID
user_id	UUID	FK	Applicant
job_id	UUID	FK	Applied job
resume_id	UUID	FK	Resume used
status	VARCHAR(50)	NOT NULL	Current stage
cover_letter_path	TEXT	NULL	Cover letter
applied_at	TIMESTAMP	NULL	Apply time
recruiter_name	VARCHAR(255)	NULL	Recruiter
recruiter_email	VARCHAR(255)	NULL	Recruiter email
notes	TEXT	NULL	Personal notes
created_at	TIMESTAMP	NOT NULL	Created
updated_at	TIMESTAMP	NOT NULL	Updated
6. skills

Purpose: Master list of all skills.

Column	Type	Constraints	Description
id	UUID	PK	Skill ID
skill_name	VARCHAR(100)	UNIQUE	Python
category	VARCHAR(100)	NULL	Programming, Cloud
created_at	TIMESTAMP	NOT NULL	Created
7. resume_skills

Purpose: Skills extracted from resumes.

Column	Type	Constraints	Description
id	UUID	PK	ID
resume_id	UUID	FK	Resume
skill_id	UUID	FK	Skill
proficiency	VARCHAR(50)	NULL	Beginner, Intermediate, Expert
years_experience	DECIMAL	NULL	Years
created_at	TIMESTAMP	NOT NULL	Created
8. job_skills

Purpose: Skills required by jobs.

Column	Type	Constraints	Description
id	UUID	PK	ID
job_id	UUID	FK	Job
skill_id	UUID	FK	Skill
is_required	BOOLEAN	DEFAULT TRUE	Required/Preferred
created_at	TIMESTAMP	NOT NULL	Created
9. job_matches

Purpose: AI-generated matching.

Column	Type	Constraints	Description
id	UUID	PK	Match ID
job_id	UUID	FK	Job
resume_id	UUID	FK	Resume
overall_score	DECIMAL(5,2)	NOT NULL	Overall score (0–100)
skill_score	DECIMAL(5,2)	NULL	Skill match
experience_score	DECIMAL(5,2)	NULL	Experience match
education_score	DECIMAL(5,2)	NULL	Education match
ats_score	DECIMAL(5,2)	NULL	ATS compatibility
missing_skills	TEXT	NULL	Missing skills
ai_feedback	TEXT	NULL	AI explanation
created_at	TIMESTAMP	NOT NULL	Created
Entity Relationship Diagram (ERD)
                    users
                      │
          1           │           N
                      ▼
                  resumes
                      │
          1           │           N
                      ▼
              resume_skills
                      │
                      ▼
                   skills
                      ▲
                      │
              job_skills
                      ▲
          N           │           1
                      │
                    jobs
                      │
          N           │           1
                      ▼
                 companies

jobs
 │
 │1
 ▼
job_applications
 ▲
 │
 │N
resumes

resumes
     \
      \
   job_matches
      /
     /
jobs
Recommended Enums
Job Platform
LINKEDIN
NAUKRI
INDEED
APIFY
COMPANY_CAREER
MANUAL
Work Mode
REMOTE
HYBRID
ONSITE
Employment Type
FULL_TIME
PART_TIME
CONTRACT
INTERNSHIP
FREELANCE
Application Status
DRAFT
PENDING
APPLIED
ASSESSMENT
INTERVIEW
HR_ROUND
REJECTED
OFFER
ACCEPTED
WITHDRAWN

## User Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| full_name | VARCHAR(255) | Not Null |
| email | VARCHAR(255) | Unique, Indexed |
| is_active | BOOLEAN | Default True |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- One User can have many Resumes.

## Company Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| name | VARCHAR(255) | Unique, Indexed |
| website | VARCHAR(500) | Nullable |
| linkedin_url | VARCHAR(500) | Nullable |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- One Company can have many Jobs.

## Job Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| company_id | UUID | Foreign Key → companies.id |
| title | VARCHAR(255) | Indexed |
| location | VARCHAR(255) | Nullable |
| employment_type | VARCHAR(100) | Nullable |
| experience_level | VARCHAR(100) | Nullable |
| salary | VARCHAR(255) | Nullable |
| description | TEXT | Not Null |
| source | VARCHAR(100) | Not Null |
| source_url | VARCHAR(500) | Unique |
| posted_date | TIMESTAMP | Nullable |
| is_active | BOOLEAN | Default True |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- Belongs to one Company
- Can have many Job Applications (future)
- Can have many Job Matches (future)
- Can have many Job Skills (future)

## Skill Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| name | VARCHAR(150) | Unique, Indexed |
| category | VARCHAR(100) | Nullable |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- Referenced by ResumeSkill
- Referenced by JobSkill

## ResumeSkill Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| resume_id | UUID | Foreign Key → resumes.id |
| skill_id | UUID | Foreign Key → skills.id |
| proficiency | INTEGER | Nullable |
| years_experience | INTEGER | Nullable |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- Belongs to one Resume
- Belongs to one Skill

## JobApplication Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| resume_id | UUID | Foreign Key → resumes.id |
| job_id | UUID | Foreign Key → jobs.id |
| status | VARCHAR(50) | Default: Applied |
| applied_at | TIMESTAMP | Nullable |
| cover_letter | TEXT | Nullable |
| notes | TEXT | Nullable |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- Belongs to one Resume
- Belongs to one Job

Typical status values:

- Applied
- Viewed
- Shortlisted
- Interview Scheduled
- Interview Completed
- Offer Received
- Rejected
- Withdrawn


## JobMatch Table

| Column | Type | Constraints |
|---------|------|-------------|
| id | UUID | Primary Key |
| resume_id | UUID | Foreign Key → resumes.id |
| job_id | UUID | Foreign Key → jobs.id |
| match_score | FLOAT | Required |
| missing_skills | TEXT | Nullable |
| ai_feedback | TEXT | Nullable |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

Relationships:
- Belongs to one Resume
- Belongs to one Job

users
resumes
companies
jobs
skills
resume_skills
job_skills
job_applications
job_matches

## Implemented Tables

- users
- resumes
- companies
- jobs
- skills
- resume_skills
- job_skills
- job_applications
- job_matches

Status: ✅ Implemented