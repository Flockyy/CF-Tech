from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.admin_schema import AdminCreate, AdminPublic
from app.crud import admin_crud
import uuid


router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/", response_model=AdminPublic)
def create_admin(*, session: SessionDep, admin_in: AdminCreate):
    """
    Create new admin.
    """
    admin = admin_crud.get_admin_by_email(session=session, email=admin_in.email)
    if admin:
        raise HTTPException(
            status_code=400,
            detail="The admin with this email already exists in the system.",
        )

    admin = admin_crud.create_admin(session=session, admin=admin_in)

    return admin


@router.get("/{admin_id}", response_model=AdminPublic)
def get_admin(*, session: SessionDep, admin_id: uuid.UUID):
    """
    Get an admin by ID.
    """
    admin = admin_crud.get_admin(session=session, admin_id=admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return admin


@router.put("/{admin_id}", response_model=AdminPublic)
def update_admin(*, session: SessionDep, admin_id: uuid.UUID, admin_in: AdminCreate):
    """
    Update an admin by ID.
    """
    admin = admin_crud.get_admin(session=session, admin_id=admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    updated_admin = admin_crud.update_admin(
        session=session, admin_id=admin_id, admin_update=admin_in
    )

    return updated_admin


@router.delete("/{admin_id}", response_model=dict)
def delete_admin(*, session: SessionDep, admin_id: uuid.UUID):
    """
    Delete an admin by ID.
    """
    admin = admin_crud.get_admin(session=session, admin_id=admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    admin_crud.delete_admin(session=session, admin_id=admin_id)

    return {"detail": "Admin deleted successfully"}


@router.get("/", response_model=list[AdminPublic])
def list_admins(*, session: SessionDep):
    """
    List all admins.
    """
    admins = admin_crud.get_all_admins(session=session)
    return admins
