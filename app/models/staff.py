from .user import User
from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Staff(User, table=True):
    """
    Staff model that inherits from User.
    This model can be extended with additional fields specific to staff members.
    """

    __tablename__ = "staff"

    position: str = Field(..., max_length=100)  # e.g., "Administrator", "Manager"
    hire_date: datetime = Field(default_factory=datetime.now)


class StaffCreate(User, SQLModel):
    """
    Staff creation model that can be used for creating new staff members.
    This model can be extended with additional fields specific to staff members.
    """

    position: str = Field(..., max_length=100)


class StaffUpdate(User, SQLModel):
    """
    Staff update model that can be used for updating existing staff members.
    This model can be extended with additional fields specific to staff members.
    """

    position: Optional[str] = Field(None, max_length=100)
