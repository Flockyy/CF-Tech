# User model
import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from datetime import datetime


class User(SQLModel, table=True):
    """
    User model that serves as a base for other user types like Trainee and Trainer.
    This model can be extended with additional fields specific to different user roles.
    """

    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(unique=True, max_length=255)
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)
    role: str = Field(default="user", max_length=20)

    class Config:
        # Allows compatibility with ORM models like SQLModel or SQLAlchemy
        orm_mode = True
