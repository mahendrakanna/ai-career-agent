from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.user import User
from app.schemas.resume import ResumeCreate, ResumeUpdate


class ResumeService:
    """
    Handles all resume-related database operations.
    """

    @staticmethod
    def create_resume(
        db: Session,
        resume_data: ResumeCreate,
    ) -> Resume:
        """
        Create a new resume.
        """

        user = (
            db.query(User)
            .filter(User.id == resume_data.user_id)
            .first()
        )

        if user is None:
            raise ValueError("User not found")

        resume = Resume(
            user_id=resume_data.user_id,
            title=resume_data.title,
            file_name=resume_data.file_name,
            file_path=resume_data.file_path,
            file_type=resume_data.file_type,
            extracted_text=resume_data.extracted_text,
            is_default=resume_data.is_default,
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def get_resume(
        db: Session,
        resume_id: UUID,
    ) -> Resume | None:
        """
        Get a resume by ID.
        """

        return (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    @staticmethod
    def get_resumes(
        db: Session,
    ) -> list[Resume]:
        """
        Return all resumes.
        """

        return db.query(Resume).all()

    @staticmethod
    def update_resume(
        db: Session,
        resume: Resume,
        resume_data: ResumeUpdate,
    ) -> Resume:
        """
        Update an existing resume.
        """

        update_data = resume_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(resume, key, value)

        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def delete_resume(
        db: Session,
        resume: Resume,
    ) -> None:
        """
        Delete a resume.
        """

        db.delete(resume)
        db.commit()