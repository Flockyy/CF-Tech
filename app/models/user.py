from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from datetime import datetime, timezone
import uuid


class User(SQLModel, table=False):
    """
    User model that serves as a base for other user types like Trainee and Trainer.

    Args:
        SQLModel (SQLModel): Base class for SQLAlchemy models.
        table (bool, optional): Whether the model is a SQLAlchemy table. Defaults to False.
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(unique=True, max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: bool = Field(default=True)
    role: str = Field(default="user", max_length=20)
