from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.resume_skill import ResumeSkill
    from app.models.job_skill import JobSkill


class Skill(BaseModel):
    """
    Represents a technical or professional skill.
    """

    __tablename__ = "skills"

    # -------------------------
    # Columns
    # -------------------------

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # # -------------------------
    # # Relationships
    # # -------------------------

    resume_skills: Mapped[list["ResumeSkill"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
    )

    job_skills: Mapped[list["JobSkill"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
    )