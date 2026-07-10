from __future__ import annotations

from pydantic import ConfigDict, EmailStr

from app.schemas.base import BaseSchema, TimestampSchema

class UserBase(BaseSchema):
    """
    Shared user fields.
    """

    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    """
    Request body for creating a user.
    """

    pass

class UserUpdate(BaseSchema):
    """
    Request body for updating a user.
    """

    full_name: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None

class UserResponse(TimestampSchema):
    """
    Response returned by the API.
    """

    full_name: str
    email: EmailStr
    is_active: bool