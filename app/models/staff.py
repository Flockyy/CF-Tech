from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime, timezone
from app.models.user import UserBase
import uuid


class DutyStaffLink(SQLModel, table=True):
    """
    DutyStaffLink model that represents the many-to-many relationship between Duty and Staff.

    Args:
        SQLModel (SQLModel): Base class for SQLAlchemy models.
        table (bool, optional): Whether the model is a SQLAlchemy table. Defaults to True.
    """

    __tablename__ = "duty_staff_links"

    duty_id: uuid.UUID = Field(foreign_key="duties.id", primary_key=True)
    staff_id: uuid.UUID = Field(foreign_key="staff.id", primary_key=True)

    duties: "DutyBase" = Relationship(back_populates="staff_links")
    staff: "StaffBase" = Relationship(back_populates="duty_links")


class StaffBase(UserBase, table=True):
    """
    Staff model that inherits from User.

    Args:
        User (User): Base user model that provides common user fields.
        table (bool, optional): Whether the model is a SQLAlchemy table. Defaults to True.
    """

    __tablename__ = "staff"

    position: str = Field(..., max_length=100)  # e.g., "Administrator", "Manager"
    hire_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    duty_links: list[DutyStaffLink] = Relationship(back_populates="staff")


class DutyBase(SQLModel, table=True):
    """
    Duty model that represents the various duties assigned to staff.

    Args:
        SQLModel (SQLModel): Base class for SQLAlchemy models.
        table (bool, optional): Whether the model is a SQLAlchemy table. Defaults to True.
    """

    __tablename__ = "duties"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    staff_links: list[DutyStaffLink] = Relationship(back_populates="duties")
