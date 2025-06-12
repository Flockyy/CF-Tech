from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.admin_schema import AdminCreate, AdminPublic
from app.crud import admin_crud
import uuid


router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/", response_model=AdminPublic)
def create_admin(*, session: SessionDep, admin_in: AdminCreate):
    """
    Create a new admin.

    Args:
        session (SessionDep): The database session dependency.
        admin_in (AdminCreate): The admin creation data.

    Raises:
        HTTPException: If the admin with this email already exists.

    Returns:
        AdminPublic: The created admin data.
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

    Args:
        session (SessionDep): The database session dependency.
        admin_id (uuid.UUID): The ID of the admin to retrieve.

    Raises:
        HTTPException: If the admin is not found.

    Returns:
        AdminPublic: The retrieved admin data.
    """

    admin = admin_crud.get_admin(session=session, admin_id=admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return admin


@router.put("/{admin_id}", response_model=AdminPublic)
def update_admin(*, session: SessionDep, admin_id: uuid.UUID, admin_in: AdminCreate):
    """
    Update an admin by ID.

    Args:
        session (SessionDep): The database session dependency.
        admin_id (uuid.UUID): The ID of the admin to update.
        admin_in (AdminCreate): The admin update data.

    Raises:
        HTTPException: If the admin is not found.
        HTTPException: If the admin update fails.

    Returns:
        AdminPublic: The updated admin data.
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

    Args:
        session (SessionDep): The database session dependency.
        admin_id (uuid.UUID): The ID of the admin to delete.

    Raises:
        HTTPException: If the admin is not found.

    Returns:
        dict: A success message.
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

    Args:
        session (SessionDep): The database session dependency.

    Returns:
        list[AdminPublic]: The list of all admins.
    """

    admins = admin_crud.get_all_admins(session=session)
    return admins
