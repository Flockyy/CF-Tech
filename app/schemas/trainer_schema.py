from pydantic import BaseModel, Field
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from typing import Optional
import uuid


class TrainerCreate(UserCreate, BaseModel):
    """
    Trainer creation model that can be used for creating new trainers.

    Args:
        UserCreate (UserCreate): Base model for user creation.
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    specialty: str = Field(..., max_length=100)
    hourly_rate: float = Field(..., ge=0)
    bio: Optional[str] = Field(default=None, max_length=500)


class TrainerUpdate(UserUpdate, BaseModel):
    """
    Trainer update model that can be used for updating existing trainers.
    Args:
        UserUpdate (UserUpdate): Base model for user updates.
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    specialty: Optional[str] = Field(default=None, max_length=100)
    hourly_rate: Optional[float] = Field(default=None, ge=0)
    bio: Optional[str] = Field(default=None, max_length=500)


class TrainerPublic(User):
    """
    Public representation of a trainer.

    Args:
        User (User): Base user model that provides common user fields.
    """

    id: uuid.UUID
