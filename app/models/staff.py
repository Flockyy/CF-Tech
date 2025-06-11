from .user import User
from sqlmodel import Field
from datetime import datetime, timezone


class Staff(User, table=True):
    """
    Staff model that inherits from User.
    This model can be extended with additional fields specific to staff members.
    """

    __tablename__ = "staff"

    position: str = Field(..., max_length=100)  # e.g., "Administrator", "Manager"
    hire_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
