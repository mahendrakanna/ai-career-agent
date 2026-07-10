from __future__ import annotations

from app.schemas.base import BaseSchema, TimestampSchema


class SkillBase(BaseSchema):
    """
    Shared skill fields.
    """

    name: str


class SkillCreate(SkillBase):
    """
    Request body for creating a skill.
    """

    pass


class SkillUpdate(BaseSchema):
    """
    Request body for updating a skill.
    """

    name: str | None = None


class SkillResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    name: str