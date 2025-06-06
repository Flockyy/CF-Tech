from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.user_schema import UserCreate, UserUpdate


class StaffCreate(UserCreate, BaseModel):
    """
    Staff creation model that can be used for creating new staff members.
    This model can be extended with additional fields specific to staff members.
    """

    position: str = Field(..., max_length=100)


class StaffUpdate(UserUpdate, BaseModel):
    """
    Staff update model that can be used for updating existing staff members.
    This model can be extended with additional fields specific to staff members.
    """

    position: Optional[str] = Field(None, max_length=100)
