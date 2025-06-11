from app.models.staff import Staff
from app.models.staff import DutyStaffLink
from app.schemas.staff_schema import StaffCreate, StaffUpdate
from sqlmodel import Session, select
import uuid


def create_staff(session: Session, staff: StaffCreate) -> Staff:
    """
    Create a new staff member in the database.
    """
    db_staff = Staff.model_validate(staff)
    session.add(db_staff)
    session.commit()
    session.refresh(db_staff)
    return db_staff


# TODO: Change all str to uuid.UUID for staff_id in the CRUD functions
def get_staff(session: Session, staff_id: uuid.UUID) -> Staff:
    """
    Retrieve a staff member by ID from the database.
    """
    db_staff = session.get(Staff, staff_id)
    return db_staff


def get_all_staff(session: Session) -> list[Staff]:
    """
    Retrieve all staff members from the database.
    """
    statement = select(Staff)
    return session.exec(statement).all()


def update_staff(
    session: Session, staff_id: uuid.UUID, staff_update: StaffUpdate
) -> Staff:
    """
    Update an existing staff member in the database.
    Args:
        session (Session): The database session.
        staff_id (uuid.UUID): The ID of the staff member to update.
        staff_update (StaffUpdate): The updated staff data.
    Returns:
        Staff: The updated staff member.
    Raises:
        ValueError: If the staff member is not found.
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


def delete_staff(session: Session, staff_id: uuid.UUID) -> None:
    """
    Delete a staff member from the database.
    Args:
        session (Session): The database session.
        staff_id (uuid.UUID): The ID of the staff member to delete.
    Raises:
        ValueError: If the staff member is not found.
    """
    db_staff = session.get(Staff, staff_id)
    if not db_staff:
        raise ValueError("Staff member not found")

    session.delete(db_staff)
    session.commit()


def get_staff_by_email(session: Session, email: str) -> Staff:
    """
    Retrieve a staff member by their email from the database.
    Args:
        session (Session): The database session.
        email (str): The email of the staff member to retrieve.
    Returns:
        Staff: The staff member if found, otherwise None.
    """
    statement = select(Staff).where(Staff.email == email)
    result = session.exec(statement).first()
    return result


def add_duty_to_staff(
    session: Session, staff_id: uuid.UUID, duty_id: uuid.UUID
) -> Staff:
    """
    Add a duty to a staff member.
    Args:
        session (Session): The database session.
        staff_id (uuid.UUID): The ID of the staff member.
        duty_id (uuid.UUID): The ID of the duty to add.
    Returns:
        Staff: The updated staff member with the new duty.
    """
    db_staff = session.get(Staff, staff_id)
    if not db_staff:
        raise ValueError("Staff member not found")

    duty_link = DutyStaffLink(staff_id=staff_id, duty_id=duty_id)
    session.add(duty_link)
    session.commit()
    session.refresh(db_staff)
    return duty_link
