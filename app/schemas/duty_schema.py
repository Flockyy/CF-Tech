from pydantic import BaseModel, Field
import uuid


class DutyCreate(BaseModel):
    """
    Duty creation model that can be used for creating new duties.
    """

    title: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., max_length=255)


class DutyUpdate(BaseModel):
    """
    Duty update model that can be used for updating existing duties.
    """

    title: str = Field(
        None, min_length=2, max_length=100
    )  # Optional field for updating the title
    description: str = Field(
        None, max_length=255
    )  # Optional field for updating the description


class DutyPublic(DutyCreate):
    id: uuid.UUID
