from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime, timezone
from app.models.user import User
import uuid


class DutyStaffLink(SQLModel, table=True):
    """
    DutyStaffLink model that represents the many-to-many relationship between Duty and Staff.
    This model links a duty to a staff member.
    """

    __tablename__ = "duty_staff_links"

    duty_id: uuid.UUID = Field(foreign_key="duties.id", primary_key=True)
    staff_id: uuid.UUID = Field(foreign_key="staff.id", primary_key=True)

    duties: "Duty" = Relationship(back_populates="staff_links")
    staff: "Staff" = Relationship(back_populates="duty_links")


class Staff(User, table=True):
    """
    Staff model that inherits from User.
    This model can be extended with additional fields specific to staff members.
    """

    __tablename__ = "staff"

    position: str = Field(..., max_length=100)  # e.g., "Administrator", "Manager"
    hire_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    duty_links: list[DutyStaffLink] = Relationship(back_populates="staff")


class Duty(SQLModel, table=True):
    """
    Duty model that represents the various duties assigned to staff.
    """

    __tablename__ = "duties"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    staff_links: list[DutyStaffLink] = Relationship(back_populates="duties")
