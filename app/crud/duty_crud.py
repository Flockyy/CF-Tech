from app.models.staff import Duty
from app.schemas.duty_schema import DutyCreate, DutyUpdate
from sqlmodel import Session, select
import uuid


def create_duty(session: Session, duty: DutyCreate) -> Duty:
    """
    Create a new duty in the database.
    Args:
        session (Session): The database session.
        duty (DutyCreate): The duty data to create.
    Returns:
        Duty: The created duty.
    """
    db_duty = Duty.model_validate(duty)
    session.add(db_duty)
    session.commit()
    session.refresh(db_duty)
    return db_duty


def get_duty(session: Session, duty_id: uuid.UUID) -> Duty:
    """
    Retrieve a duty by ID from the database.
    Args:
        session (Session): The database session.
        duty_id (uuid.UUID): The ID of the duty to retrieve.
    Returns:
        Duty: The duty object if found, otherwise raises ValueError.
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")
    return db_duty


def get_all_duties(session: Session) -> list[Duty]:
    """
    Retrieve all duties from the database.
    Args:
        session (Session): The database session.
    Returns:
        list[Duty]: A list of all duty objects.
    """
    statement = select(Duty)
    return session.exec(statement).all()


def get_duty_by_title(session: Session, title: str) -> Duty:
    """
    Retrieve a duty by its title from the database.
    Args:
        session (Session): The database session.
        title (str): The title of the duty to retrieve.
    Returns:
        Duty: The duty object if found, otherwise raises ValueError.
    """
    statement = select(Duty).where(Duty.title == title)
    db_duty = session.exec(statement).first()
    return db_duty


def update_duty(session: Session, duty_id: uuid.UUID, duty_update: DutyUpdate) -> Duty:
    """
    Update an existing duty in the database.
    Args:
        session (Session): The database session.
        duty_id (uuid.UUID): The ID of the duty to update.
        duty_update (DutyUpdate): The updated duty data.
    Returns:
        Duty: The updated duty object.
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")

    duty_data = duty_update.model_dump(exclude_unset=True)
    for key, value in duty_data.items():
        setattr(db_duty, key, value)

    session.add(db_duty)
    session.commit()
    session.refresh(db_duty)
    return db_duty


def delete_duty(session: Session, duty_id: uuid.UUID) -> None:
    """
    Delete a duty from the database.
    Args:
        session (Session): The database session.
        duty_id (uuid.UUID): The ID of the duty to delete.
    Raises:
        ValueError: If the duty with the given ID does not exist.
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")

    session.delete(db_duty)
    session.commit()
