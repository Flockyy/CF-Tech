from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.staff_schema import StaffCreate, StaffPublic
from app.crud import staff_crud
import uuid


router = APIRouter(prefix="/staff", tags=["staff"])


@router.post("/", response_model=StaffPublic)
def create_staff(*, session: SessionDep, staff_in: StaffCreate):
    """
    Create new staff member.
    """
    staff = staff_crud.get_staff_by_email(session=session, email=staff_in.email)
    if staff:
        raise HTTPException(
            status_code=400,
            detail="The staff member with this email already exists in the system.",
        )

    staff = staff_crud.create_staff(session=session, staff=staff_in)

    return staff


@router.get("/{staff_id}", response_model=StaffPublic)
def get_staff(*, session: SessionDep, staff_id: uuid.UUID):
    """
    Get a staff member by ID.
    """
    staff = staff_crud.get_staff(session=session, staff_id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")

    return staff


@router.put("/{staff_id}", response_model=StaffPublic)
def update_staff(*, session: SessionDep, staff_id: uuid.UUID, staff_in: StaffCreate):
    """
    Update a staff member by ID.
    """
    staff = staff_crud.get_staff(session=session, staff_id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")

    updated_staff = staff_crud.update_staff(
        session=session, staff_id=staff_id, staff_update=staff_in
    )

    return updated_staff


@router.delete("/{staff_id}", response_model=dict)
def delete_staff(*, session: SessionDep, staff_id: uuid.UUID):
    """
    Delete a staff member by ID.
    """
    staff = staff_crud.get_staff(session=session, staff_id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")

    staff_crud.delete_staff(session=session, staff_id=staff_id)

    return {"detail": "Staff member deleted successfully"}


@router.get("/", response_model=list[StaffPublic])
def list_staff(*, session: SessionDep):
    """
    List all staff members.
    """
    staff_list = staff_crud.get_all_staff(session=session)
    return staff_list
