from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.company import Company
    from app.models.job_skill import JobSkill
    from app.models.job_application import JobApplication


class Job(BaseModel):
    """
    Represents a scraped job posting.
    """

    __tablename__ = "jobs"

    # -------------------------
    # Columns
    # -------------------------

    company_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("companies.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    experience_level: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    salary: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    source_url: Mapped[str] = mapped_column(
        String(500),
        unique=True,
        nullable=False,
    )

    posted_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # -------------------------
    # Relationships
    # -------------------------

    company: Mapped["Company"] = relationship(
        back_populates="jobs",
    )

    job_skills: Mapped[list["JobSkill"]] = relationship(
        back_populates="job",
        cascade="all, delete-orphan",
    )

    job_applications: Mapped[list["JobApplication"]] = relationship(
    back_populates="job",
    cascade="all, delete-orphan",
    )

    job_matches: Mapped[list["JobMatch"]] = relationship(
    back_populates="job",
    cascade="all, delete-orphan",
    )

    

