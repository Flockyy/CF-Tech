from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
import uuid


class Duty(SQLModel, table=True):
    """
    Duty model that represents the various duties assigned to staff.
    """

    __tablename__ = "duties"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    staff_id: uuid.UUID = Field(foreign_key="staff.id")
    description: str = Field(..., max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
