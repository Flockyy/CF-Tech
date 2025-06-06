from .user import User
from datetime import datetime, timedelta
from typing import Annotated, Optional
from pydantic import BeforeValidator
from sqlmodel import SQLModel, Field

def is_valid_date_of_birth(date_of_birth: datetime) -> bool:
    """
    Validate the date of birth for a trainee.
    The date of birth must be at least 16 years in the past.
    """
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    if date_of_birth <= datetime.now() - timedelta(days=365 * 16):
        return date_of_birth.strftime("%Y-%m-%d")
    return False

class Trainee(User, table=True):
    """
    Trainee model that inherits from User.
    This model can be extended with additional fields specific to trainees.
    """

    __tablename__ = "trainees"

    date_of_birth: Annotated[datetime, BeforeValidator(is_valid_date_of_birth)]
    study_level: Optional[str] = None  #  e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        ..., regex=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: datetime = Field(default_factory=datetime.now)


class TraineeCreate(User, SQLModel):
    """
    Trainee creation model that can be used for creating new trainees.
    This model can be extended with additional fields specific to trainees.
    """

    date_of_birth: Annotated[str, BeforeValidator(is_valid_date_of_birth)]
    study_level: Optional[str] = None  # e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        ..., regex=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: datetime = Field(default_factory=datetime.now)


class TraineeUpdate(User, SQLModel):
    """
    Trainee update model that can be used for updating existing trainees.
    This model can be extended with additional fields specific to trainees.
    """

    date_of_birth: Annotated[Optional[str], BeforeValidator(is_valid_date_of_birth)]
    study_level: Optional[str] = None  # e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        None, regex=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: Optional[datetime] = None
