from pydantic import BaseModel, Field
import uuid


class DutyCreate(BaseModel):
    """
    Duty creation model that can be used for creating new duties.
    """

    staff_id: uuid.UUID = Field(..., foreign_key="staff.id")
    description: str = Field(..., max_length=255)


class DutyUpdate(BaseModel):
    """
    Duty update model that can be used for updating existing duties.
    """

    description: str = Field(
        None, max_length=255
    )  # Optional field for updating the description
    staff_id: uuid.UUID = Field(
        None, foreign_key="staff.id"
    )  # Optional field for updating the staff ID
