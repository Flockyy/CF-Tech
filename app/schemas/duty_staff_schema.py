from pydantic import BaseModel
from typing import Optional
import uuid


class DutyStaffCreate(BaseModel):
    """
    DutyStaff creation model that can be used for creating new duty assignments.

    Args:
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    staff_id: uuid.UUID
    duty_id: list[uuid.UUID]


class DutyStaffUpdate(BaseModel):
    """
    DutyStaff update model that can be used for updating existing duty assignments.

    Args:
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    staff_id: Optional[uuid.UUID]
    duty_id: Optional[uuid.UUID]


class DutyStaffPublic(BaseModel):
    """
    Public representation of a duty assignment.

    Args:
        BaseModel (BaseModel): Base model for Pydantic schemas.
    """

    staff_id: uuid.UUID
    duty_id: uuid.UUID
