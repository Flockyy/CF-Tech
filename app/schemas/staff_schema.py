from pydantic import BaseModel, Field
from typing import Optional
from app.models.user import UserBase
from app.schemas.user_schema import UserCreate, UserUpdate
import uuid


class StaffCreate(UserCreate, BaseModel):
    """
    Staff creation model that can be used for creating new staff members.

    Args:
        UserCreate (UserCreate): Base model for user creation.
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    position: str = Field(..., max_length=100)


class StaffUpdate(UserUpdate, BaseModel):
    """
    Staff update model that can be used for updating existing staff members.

    Args:
        UserUpdate (UserUpdate): Base model for user updates.
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    position: Optional[str] = Field(None, max_length=100)


class StaffPublic(UserBase):
    """
    Public representation of a staff member.

    Args:
        User (User): Base user model that provides common user fields.
    """

    id: uuid.UUID
