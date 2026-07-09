from app.models.base_model import Base #, BaseModel
from app.models.user import User
from app.models.resume import Resume
from app.models.company import Company
from app.models.job import Job
from app.models.skill import Skill
from app.models.resume_skill import ResumeSkill
from app.models.job_skill import JobSkill
from app.models.job_application import JobApplication
from app.models.job_match import JobMatch

__all__ = [
    "Base",
   # "BaseModel",
    "User",
    "Resume",
    "Company",
    "Job",
    "Skill",
    "ResumeSkill",
    "JobSkill",
    "JobApplication",
    "JobMatch",     
]
