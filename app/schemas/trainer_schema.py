from pydantic import BaseModel, Field
from app.models.user import UserBase
from app.schemas.user_schema import UserCreate, UserUpdate
from typing import Optional
import uuid


class TrainerCreate(UserCreate, BaseModel):
    """
    Trainer creation model that can be used for creating new trainers.
    This model can be extended with additional fields specific to trainers.
    """

    specialty: str = Field(..., max_length=100)
    hourly_rate: float = Field(..., ge=0)
    bio: Optional[str] = Field(default=None, max_length=500)


class TrainerUpdate(UserUpdate, BaseModel):
    """
    Trainer update model that can be used for updating existing trainers.
    This model can be extended with additional fields specific to trainers.
    """

    specialty: Optional[str] = Field(default=None, max_length=100)
    hourly_rate: Optional[float] = Field(default=None, ge=0)
    bio: Optional[str] = Field(default=None, max_length=500)


class TrainerPublic(UserBase):
    id: uuid.UUID
