from models.user import User
from typing import Optional
from sqlmodel import Field
from datetime import datetime


class Staff(User, table=True):
    """
    Staff model that inherits from User.
    This model can be extended with additional fields specific to staff members.
    """

    __tablename__ = "staff"

    position: str = Field(..., max_length=100)  # e.g., "Administrator", "Manager"
    hire_date: datetime = Field(default_factory=datetime.now)
    responsibilities: Optional[dict] = Field(
        default=None, max_length=100
    )  # e.g., "HR", "IT"

    class Config:
        # Allows compatibility with ORM models like SQLModel or SQLAlchemy
        orm_mode = True
