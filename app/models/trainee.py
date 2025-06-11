from .user import User
from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field


class Trainee(User, table=True):
    """
    Trainee model that inherits from User.
    This model can be extended with additional fields specific to trainees.
    """

    __tablename__ = "trainees"

    date_of_birth: datetime = Field(..., description="Date of birth of the trainee")
    study_level: Optional[str] = None  #  e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        ..., regex=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
