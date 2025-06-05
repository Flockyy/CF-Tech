from models.user import User
from typing import Optional
from sqlmodel import Field
from datetime import datetime


class Trainer(User, table=True):
    """
    Trainer model that inherits from User.
    This model can be extended with additional fields specific to trainers.
    """

    __tablename__ = "trainers"

    specialty: str = Field(
        ..., max_length=100
    )  # e.g., "Data Science", "Web Development"
    hire_date: datetime = Field(default_factory=datetime.now)
    hourly_rate: float = Field(..., ge=0)  # Hourly rate for the trainer's services
    bio: Optional[str] = Field(
        default=None, max_length=500
    )  # Short biography of the trainer

    class Config:
        # Allows compatibility with ORM models like SQLModel or SQLAlchemy
        orm_mode = True
