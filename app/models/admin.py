from user import User
from datetime import datetime
from sqlmodel import SQLModel, Field


class Admin(User, table=True):
    """
    Admin model that inherits from User.
    This model can be extended with additional fields specific to administrators.
    """

    __tablename__ = "admins"

    admin_level: int = Field(
        ..., ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(default_factory=datetime.now)


class AdminCreate(User, SQLModel):
    """
    Admin creation model that can be used for creating new administrators.
    This model can be extended with additional fields specific to administrators.
    """

    admin_level: int = Field(
        ..., ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(default_factory=datetime.now)


class AdminUpdate(User, SQLModel):
    """
    Admin update model that can be used for updating existing administrators.
    This model can be extended with additional fields specific to administrators.
    """

    admin_level: int = Field(
        None, ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(None)  # Date of promotion or last update
