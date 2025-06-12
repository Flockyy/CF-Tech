from app.schemas.admin_schema import AdminCreate, AdminUpdate
from app.models.admin import AdminBase
from sqlmodel import Session, select
import uuid


def create_admin(session: Session, admin: AdminCreate) -> AdminBase:
    """Create a new admin in the database.

    Args:
        session (Session): The database session.
        admin (AdminCreate): The admin data to create.

    Returns:
        Admin: The created admin.
    """

    db_admin = AdminBase.model_validate(admin)
    session.add(db_admin)
    session.commit()
    session.refresh(db_admin)
    return db_admin


def get_admin(session: Session, admin_id: uuid.UUID) -> AdminBase:
    """
    Retrieve an admin by ID from the database.
    Args:
        session (Session): The database session.
        admin_id (uuid.UUID): The ID of the admin to retrieve.
    Returns:
        Admin: The admin object if found, otherwise None.
    """

    return session.get(AdminBase, admin_id)


def get_all_admins(session: Session) -> list[AdminBase]:
    """
    Retrieve all admins from the database.
    Args:
        session (Session): The database session.
    Returns:
        list[Admin]: A list of all admin objects.
    """
    statement = select(AdminBase)
    return session.exec(statement).all()


def get_admin_by_email(session: Session, email: str) -> AdminBase:
    """
    Retrieve an admin by email from the database.
    Args:
        session (Session): The database session.
        email (str): The email of the admin to retrieve.
    Returns:
        Admin: The admin object if found, otherwise None.
    """
    statement = select(AdminBase).where(AdminBase.email == email)
    return session.exec(statement).first()


def update_admin(
    session: Session, admin_id: uuid.UUID, admin_update: AdminUpdate
) -> AdminBase:
    """
    Update an existing admin in the database.
    Args:
        session (Session): The database session.
        admin_id (uuid.UUID): The ID of the admin to update.
        admin_update (AdminUpdate): The data to update the admin with.
    Returns:
        Admin: The updated admin object if successful, otherwise None.
    """
    db_admin = session.get(AdminBase, admin_id)
    if not db_admin:
        return None
    update_data = admin_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_admin, key, value)
    session.add(db_admin)
    session.commit()
    session.refresh(db_admin)
    return db_admin


def delete_admin(session, admin_id: uuid.UUID) -> bool:
    """
    Delete an admin from the database.
    Args:
        session (Session): The database session.
        admin_id (uuid.UUID): The ID of the admin to delete.
    Returns:
        bool: True if the admin was deleted successfully, otherwise False.
    """
    db_admin = session.get(AdminBase, admin_id)
    if not db_admin:
        return False
    session.delete(db_admin)
    session.commit()
    return True
