from pydantic import BaseModel, Field
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from datetime import datetime
import uuid


class AdminCreate(UserCreate, BaseModel):
    """
    Admin creation model that can be used for creating new administrators.
    This model can be extended with additional fields specific to administrators.
    """

    admin_level: int = Field(
        ..., ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(default_factory=datetime.now)


class AdminUpdate(UserUpdate, BaseModel):
    """
    Admin update model that can be used for updating existing administrators.
    This model can be extended with additional fields specific to administrators.
    """

    admin_level: int = Field(
        None, ge=1, le=2
    )  # Level of administrative privileges (1-2)
    promotion_date: datetime = Field(None)  # Date of promotion or last update


class AdminPublic(User):
    id: uuid.UUID
