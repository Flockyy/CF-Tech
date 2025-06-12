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

    Args:
        session (SessionDep): The database session dependency.
        duty_in (DutyCreate): The duty creation data.

    Raises:
        HTTPException: If the duty with this title already exists.
        HTTPException: If the duty creation fails.

    Returns:
        DutyPublic: The created duty data.
    """

    duty = duty_crud.get_duty_by_title(session=session, title=duty_in.title)
    if duty:
        raise HTTPException(
            status_code=400,
            detail="The duty with this title already exists in the system.",
        )

    duty = duty_crud.create_duty(session=session, duty=duty_in)

    return duty


@router.get("/{duty_id}", response_model=DutyPublic)
def get_duty(*, session: SessionDep, duty_id: uuid.UUID):
    """
    Get a duty by ID.

    Args:
        session (SessionDep): The database session dependency.
        duty_id (uuid.UUID): The ID of the duty to retrieve.

    Raises:
        HTTPException: If the duty is not found.

    Returns:
        DutyPublic: The retrieved duty data.
    """
    duty = duty_crud.get_duty(session=session, duty_id=duty_id)
    if not duty:
        raise HTTPException(status_code=404, detail="Duty not found")

    return duty


@router.put("/{duty_id}", response_model=dict)
def update_duty(*, session: SessionDep, duty_id: uuid.UUID, duty_in: DutyCreate):
    """
    Update a duty by ID.

    Args:
        session (SessionDep): The database session dependency.
        duty_id (uuid.UUID): The ID of the duty to update.
        duty_in (DutyCreate): The duty update data.

    Raises:
        HTTPException: If the duty is not found.
        HTTPException: If the duty update fails.

    Returns:
        DutyPublic: The updated duty data.
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

    Args:
        session (SessionDep): The database session dependency.
        duty_id (uuid.UUID): The ID of the duty to delete.

    Raises:
        HTTPException: If the duty is not found.

    Returns:
        dict: A success message.
    """

    duty = duty_crud.get_duty(session=session, duty_id=duty_id)
    if not duty:
        raise HTTPException(status_code=404, detail="Duty not found")

    duty_crud.delete_duty(session=session, duty_id=duty_id)

    return {"detail": "Duty deleted successfully"}
