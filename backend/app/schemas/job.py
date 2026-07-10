from __future__ import annotations

from datetime import datetime
from uuid import UUID

from app.schemas.base import BaseSchema, TimestampSchema


class JobBase(BaseSchema):
    """
    Shared job fields.
    """

    company_id: UUID
    title: str
    location: str | None = None
    employment_type: str | None = None
    experience_level: str | None = None
    salary: str | None = None
    description: str
    source: str
    source_url: str
    posted_date: datetime | None = None


class JobCreate(JobBase):
    """
    Request body for creating a job.
    """

    pass


class JobUpdate(BaseSchema):
    """
    Request body for updating a job.
    """

    title: str | None = None
    location: str | None = None
    employment_type: str | None = None
    experience_level: str | None = None
    salary: str | None = None
    description: str | None = None
    source: str | None = None
    source_url: str | None = None
    posted_date: datetime | None = None
    is_active: bool | None = None


class JobResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    company_id: UUID
    title: str
    location: str | None = None
    employment_type: str | None = None
    experience_level: str | None = None
    salary: str | None = None
    description: str
    source: str
    source_url: str
    posted_date: datetime | None = None
    is_active: bool