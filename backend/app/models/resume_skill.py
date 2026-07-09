from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.resume import Resume
    from app.models.skill import Skill


class ResumeSkill(BaseModel):
    """
    Associates a Resume with a Skill.
    """

    __tablename__ = "resume_skills"

    # -------------------------
    # Columns
    # -------------------------

    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("resumes.id"),
        nullable=False,
    )

    skill_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("skills.id"),
        nullable=False,
    )

    proficiency: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    years_experience: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    # -------------------------
    # Relationships
    # -------------------------

    resume: Mapped["Resume"] = relationship(
        back_populates="resume_skills",
    )

    skill: Mapped["Skill"] = relationship(
        back_populates="resume_skills",
    )