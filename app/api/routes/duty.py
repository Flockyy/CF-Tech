from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.duty_schema import DutyCreate, DutyPublic
from app.crud import duty_crud
import uuid

router = APIRouter(prefix="/duty", tags=["duty"])


@router.post("/", response_model=DutyPublic)
def create_duty(*, session: SessionDep, duty_in: DutyCreate):
    """
    Create a new duty.
    """
    duty = duty_crud.get_duty_by_name(session=session, name=duty_in.name)
    if duty:
        raise HTTPException(
            status_code=400,
            detail="The duty with this name already exists in the system.",
        )

    duty = duty_crud.create_duty(session=session, duty=duty_in)

    return duty


@router.get("/{duty_id}", response_model=DutyPublic)
def get_duty(*, session: SessionDep, duty_id: uuid.UUID):
    """
    Get a duty by ID.
    """
    duty = duty_crud.get_duty(session=session, duty_id=duty_id)
    if not duty:
        raise HTTPException(status_code=404, detail="Duty not found")

    return duty


@router.put("/{duty_id}", response_model=DutyPublic)
def update_duty(*, session: SessionDep, duty_id: uuid.UUID, duty_in: DutyCreate):
    """
    Update a duty by ID.
    """
    duty = duty_crud.get_duty(session=session, duty_id=duty_id)
    if not duty:
        raise HTTPException(status_code=404, detail="Duty not found")

    updated_duty = duty_crud.update_duty(
        session=session, duty_id=duty_id, duty_update=duty_in
    )

    return updated_duty


@router.delete("/{duty_id}", response_model=dict)
def delete_duty(*, session: SessionDep, duty_id: uuid.UUID):
    """
    Delete a duty by ID.
    """
    duty = duty_crud.get_duty(session=session, duty_id=duty_id)
    if not duty:
        raise HTTPException(status_code=404, detail="Duty not found")

    duty_crud.delete_duty(session=session, duty_id=duty_id)

    return {"detail": "Duty deleted successfully"}
