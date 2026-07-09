from __future__ import annotations

from typing import TYPE_CHECKING

import uuid

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.resume_skill import ResumeSkill
    from app.models.job_application import JobApplication
    from app.models.job_match import JobMatch


class Resume(BaseModel):
    """
    Represents a resume uploaded by a user.
    """

    __tablename__ = "resumes"

    # -------------------------
    # Columns
    # -------------------------

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # -------------------------
    # Relationships
    # -------------------------

    user: Mapped["User"] = relationship(
        back_populates="resumes",
    )

    resume_skills: Mapped[list["ResumeSkill"]] = relationship(
    back_populates="resume",
    cascade="all, delete-orphan",
)

    job_applications: Mapped[list["JobApplication"]] = relationship(
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    job_matches: Mapped[list["JobMatch"]] = relationship(
    back_populates="resume",
    cascade="all, delete-orphan",
)