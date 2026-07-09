from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.resume import Resume
    from app.models.job import Job


class JobMatch(BaseModel):
    """
    Stores AI-generated match results between a Resume and a Job.
    """

    __tablename__ = "job_matches"

    # -------------------------
    # Columns
    # -------------------------

    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("resumes.id"),
        nullable=False,
    )

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id"),
        nullable=False,
    )

    match_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    missing_skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    ai_feedback: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # -------------------------
    # Relationships
    # -------------------------

    resume: Mapped["Resume"] = relationship(
        back_populates="job_matches",
    )

    job: Mapped["Job"] = relationship(
        back_populates="job_matches",
    )