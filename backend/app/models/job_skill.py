from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.job import Job
    from app.models.skill import Skill


class JobSkill(BaseModel):
    """
    Associates a Job with a Skill.
    """

    __tablename__ = "job_skills"

    # -------------------------
    # Columns
    # -------------------------

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id"),
        nullable=False,
    )

    skill_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("skills.id"),
        nullable=False,
    )

    importance: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    # -------------------------
    # Relationships
    # -------------------------

    job: Mapped["Job"] = relationship(
        back_populates="job_skills",
    )

    skill: Mapped["Skill"] = relationship(
        back_populates="job_skills",
    )