import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field


class Duty(SQLModel, table=True):
    """
    Duty model that represents the various duties assigned to staff.
    """

    __tablename__ = "duties"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    staff_id: uuid.UUID = Field(foreign_key="staff.id")
    description: str = Field(..., max_length=255)
    created_at: datetime = Field(default_factory=datetime.now)


class DutyCreate(SQLModel):
    """
    Duty creation model that can be used for creating new duties.
    """

    staff_id: uuid.UUID = Field(..., foreign_key="staff.id")
    description: str = Field(..., max_length=255)


class DutyUpdate(SQLModel):
    """
    Duty update model that can be used for updating existing duties.
    """

    description: str = Field(
        None, max_length=255
    )  # Optional field for updating the description
    staff_id: uuid.UUID = Field(
        None, foreign_key="staff.id"
    )  # Optional field for updating the staff ID
