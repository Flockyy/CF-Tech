from models.user import User
from datetime import datetime
from sqlmodel import Field


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

    class Config:
        # Allows compatibility with ORM models like SQLModel or SQLAlchemy
        orm_mode = True
