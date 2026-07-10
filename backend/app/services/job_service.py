from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate


class JobService:
    """
    Handles all job-related database operations.
    """

    @staticmethod
    def create_job(
        db: Session,
        job_data: JobCreate,
    ) -> Job:
        """
        Create a new job.
        """

        company = (
            db.query(Company)
            .filter(Company.id == job_data.company_id)
            .first()
        )

        if company is None:
            raise ValueError("Company not found")

        job = Job(
            company_id=job_data.company_id,
            title=job_data.title,
            location=job_data.location,
            employment_type=job_data.employment_type,
            experience_level=job_data.experience_level,
            salary=job_data.salary,
            description=job_data.description,
            source=job_data.source,
            source_url=job_data.source_url,
            posted_date=job_data.posted_date,
        )

        db.add(job)
        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def get_job(
        db: Session,
        job_id: UUID,
    ) -> Job | None:

        return (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    @staticmethod
    def get_jobs(
        db: Session,
    ) -> list[Job]:

        return db.query(Job).all()

    @staticmethod
    def update_job(
        db: Session,
        job: Job,
        job_data: JobUpdate,
    ) -> Job:

        update_data = job_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(job, key, value)

        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def delete_job(
        db: Session,
        job: Job,
    ) -> None:

        db.delete(job)
        db.commit()