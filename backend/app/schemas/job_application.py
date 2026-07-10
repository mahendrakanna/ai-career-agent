from __future__ import annotations

from datetime import datetime
from uuid import UUID

from app.schemas.base import BaseSchema, TimestampSchema


class JobApplicationBase(BaseSchema):
    """
    Shared job application fields.
    """

    resume_id: UUID
    job_id: UUID
    status: str
    applied_at: datetime | None = None
    cover_letter: str | None = None


class JobApplicationCreate(JobApplicationBase):
    """
    Request body for creating a job application.
    """

    pass


class JobApplicationUpdate(BaseSchema):
    """
    Request body for updating a job application.
    """

    status: str | None = None
    applied_at: datetime | None = None
    cover_letter: str | None = None


class JobApplicationResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    resume_id: UUID
    job_id: UUID
    status: str
    applied_at: datetime | None = None
    cover_letter: str | None = None