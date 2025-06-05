from user import User
from datetime import datetime
from typing import Annotated, Optional
from pydantic import AfterValidator
from sqlmodel import SQLModel, Field


def is_valid_date_of_birth(date_of_birth: str) -> bool:
    # if user is a trainee, check if date of birth is more than 16 years ago
    from datetime import datetime, timedelta

    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        return dob <= datetime.now() - timedelta(days=365 * 16)
    except ValueError:
        return False


class Trainee(User, table=True):
    """
    Trainee model that inherits from User.
    This model can be extended with additional fields specific to trainees.
    """

    __tablename__ = "trainees"

    date_of_birth: Annotated[str, AfterValidator(is_valid_date_of_birth)]
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

    date_of_birth: Annotated[str, AfterValidator(is_valid_date_of_birth)]
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

    date_of_birth: Annotated[Optional[str], AfterValidator(is_valid_date_of_birth)]
    study_level: Optional[str] = None  # e.g., "Bac", "Bac +2", "Bac +3", etc.
    phone_number: Optional[str] = Field(
        None, regex=r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    )
    registration_date: Optional[datetime] = None
