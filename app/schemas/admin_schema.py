from pydantic import BaseModel, Field
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from datetime import datetime, timezone
import uuid


class AdminCreate(UserCreate, BaseModel):
    """
    Admin creation model that can be used for creating new administrators.

    Args:
        UserCreate (UserCreate): Base model for user creation.
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    admin_level: int = Field(
        ..., ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AdminUpdate(UserUpdate, BaseModel):
    """
    Admin update model that can be used for updating existing administrators.

    Args:
        UserUpdate (UserUpdate): Base model for user updates.
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    admin_level: int = Field(
        None, ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(None)  # Date of promotion or last update


class AdminPublic(User):
    """
    Public representation of an admin user.

    Args:
        User (User): Base user model that provides common user fields.
    """

    id: uuid.UUID
