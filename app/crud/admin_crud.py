from app.schemas.admin_schema import AdminCreate, AdminUpdate
from app.models.admin import Admin
from sqlmodel import Session


def create_admin(session: Session, admin: AdminCreate) -> Admin:
    """
    Create a new admin in the database.
    """

    db_admin = Admin.model_validate(admin)
    session.add(db_admin)
    session.commit()
    session.refresh(db_admin)
    return db_admin


def get_admin(session: Session, admin_id: str) -> Admin:
    """
    Retrieve an admin by ID from the database.
    """
    return session.get(Admin, admin_id)


def get_all_admins(session: Session) -> list[Admin]:
    """
    Retrieve all admins from the database.
    """
    return session.exec(Admin.select()).all()


def update_admin(session: Session, admin_id: str, admin_update: AdminUpdate) -> Admin:
    """
    Update an existing admin in the database.
    """
    db_admin = session.get(Admin, admin_id)
    if not db_admin:
        return None
    update_data = admin_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_admin, key, value)
    session.add(db_admin)
    session.commit()
    session.refresh(db_admin)
    return db_admin


def delete_admin(session, admin_id: str) -> bool:
    """
    Delete an admin from the database.
    """
    db_admin = session.get(Admin, admin_id)
    if not db_admin:
        return False
    session.delete(db_admin)
    session.commit()
    return True
