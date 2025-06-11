from app.models.staff import Staff
from app.schemas.staff_schema import StaffCreate, StaffUpdate
from sqlmodel import Session


def create_staff(session: Session, staff: StaffCreate) -> Staff:
    """
    Create a new staff member in the database.
    """
    db_staff = Staff.model_validate(staff)
    session.add(db_staff)
    session.commit()
    session.refresh(db_staff)
    return db_staff


def get_staff(session: Session, staff_id: str) -> Staff:
    """
    Retrieve a staff member by ID from the database.
    """
    db_staff = session.get(Staff, staff_id)
    if not db_staff:
        raise ValueError("Staff member not found")
    return db_staff


def get_all_staff(session: Session) -> list[Staff]:
    """
    Retrieve all staff members from the database.
    """
    return session.exec(Staff.select()).all()


def update_staff(session: Session, staff_id: str, staff_update: StaffUpdate) -> Staff:
    """
    Update an existing staff member in the database.
    """
    db_staff = session.get(Staff, staff_id)
    if not db_staff:
        raise ValueError("Staff member not found")

    staff_data = staff_update.model_dump(exclude_unset=True)
    for key, value in staff_data.items():
        setattr(db_staff, key, value)

    session.add(db_staff)
    session.commit()
    session.refresh(db_staff)
    return db_staff


def delete_staff(session: Session, staff_id: str) -> None:
    """
    Delete a staff member from the database.
    """
    db_staff = session.get(Staff, staff_id)
    if not db_staff:
        raise ValueError("Staff member not found")

    session.delete(db_staff)
    session.commit()
