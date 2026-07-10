from __future__ import annotations

from uuid import UUID

from app.schemas.base import BaseSchema, TimestampSchema


class JobMatchBase(BaseSchema):
    """
    Shared job match fields.
    """

    resume_id: UUID
    job_id: UUID
    match_score: float
    explanation: str | None = None


class JobMatchCreate(JobMatchBase):
    """
    Request body for creating a job match.
    """

    pass


class JobMatchUpdate(BaseSchema):
    """
    Request body for updating a job match.
    """

    match_score: float | None = None
    explanation: str | None = None


class JobMatchResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    resume_id: UUID
    job_id: UUID
    match_score: float
    explanation: str | None = None