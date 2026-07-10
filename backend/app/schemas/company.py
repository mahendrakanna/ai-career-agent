from __future__ import annotations

from app.schemas.base import BaseSchema, TimestampSchema


class CompanyBase(BaseSchema):
    """
    Shared company fields.
    """

    name: str
    website: str | None = None
    linkedin_url: str | None = None


class CompanyCreate(CompanyBase):
    """
    Request body for creating a company.
    """

    pass


class CompanyUpdate(BaseSchema):
    """
    Request body for updating a company.
    """

    name: str | None = None
    website: str | None = None
    linkedin_url: str | None = None


class CompanyResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    name: str
    website: str | None = None
    linkedin_url: str | None = None