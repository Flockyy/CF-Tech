from pydantic import BaseModel, Field, field_validator
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from datetime import datetime, timedelta, timezone
from typing import Optional
import uuid


class TraineeCreate(UserCreate, BaseModel):
    """
    Trainee creation model that can be used for creating new trainees.
    This model can be extended with additional fields specific to trainees.
    """

    date_of_birth: datetime = Field(
        ...,
        description="Date of birth in ISO format (YYYY-MM-DD), must be at least 16 years old",
    )
    study_level: Optional[str] = None  # e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        ..., pattern=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: datetime = Field(default_factory=datetime.now)

    @field_validator("date_of_birth")
    def is_valid_date_of_birth(cls, value: datetime) -> datetime:
        """
        Validate that the date of birth is at least 16 years ago.
        """
        if value > datetime.now(timezone.utc) - timedelta(days=365 * 16):
            raise ValueError("Trainee must be at least 16 years old.")
        return value


class TraineeUpdate(UserUpdate, BaseModel):
    """
    Trainee update model that can be used for updating existing trainees.
    This model can be extended with additional fields specific to trainees.
    """

    date_of_birth: Optional[datetime] = Field(
        ...,
        description="Date of birth in ISO format (YYYY-MM-DD), must be at least 16 years old",
    )
    study_level: Optional[str] = None  # e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        None, pattern=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: Optional[datetime] = None

    @field_validator("date_of_birth")
    def is_valid_date_of_birth(cls, value: datetime) -> datetime:
        """
        Validate that the date of birth is at least 16 years ago.
        """
        if value and value > datetime.now() - timedelta(days=365 * 16):
            raise ValueError("Trainee must be at least 16 years old.")
        return value


class TraineePublic(User):
    """
    Public model for Trainee that can be used for displaying trainee information.
    This model can be extended with additional fields specific to public views.
    """

    id: uuid.UUID
