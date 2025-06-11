from pydantic import BaseModel
from typing import Optional
import uuid


class DutyStaffCreate(BaseModel):
    staff_id: uuid.UUID
    duty_id: list[uuid.UUID]


class DutyStaffUpdate(BaseModel):
    staff_id: Optional[uuid.UUID]
    duty_id: Optional[uuid.UUID]


class DutyStaffPublic(BaseModel):
    staff_id: uuid.UUID
    duty_id: uuid.UUID
