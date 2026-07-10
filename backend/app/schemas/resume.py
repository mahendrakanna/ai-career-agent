from __future__ import annotations

from uuid import UUID

from app.schemas.base import BaseSchema, TimestampSchema


class ResumeBase(BaseSchema):
    """
    Shared resume fields.
    """

    title: str
    file_name: str
    file_path: str
    file_type: str
    extracted_text: str | None = None
    is_default: bool = False


class ResumeCreate(ResumeBase):
    """
    Request body for creating a resume.
    """

    user_id: UUID


class ResumeUpdate(BaseSchema):
    """
    Request body for updating a resume.
    """

    title: str | None = None
    file_name: str | None = None
    file_path: str | None = None
    file_type: str | None = None
    extracted_text: str | None = None
    is_default: bool | None = None


class ResumeResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    user_id: UUID
    title: str
    file_name: str
    file_path: str
    file_type: str
    extracted_text: str | None
    is_default: bool