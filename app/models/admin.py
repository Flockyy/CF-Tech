from .user import UserBase
from datetime import datetime, timezone
from sqlmodel import Field


class AdminBase(UserBase, table=True):
    """
    Admin model that inherits from User.

    Args:
        User (User): Base user model that provides common user fields.
        table (bool, optional): Whether the model is a SQLAlchemy table. Defaults to True.
    """

    __tablename__ = "admins"

    admin_level: int = Field(
        ..., ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
