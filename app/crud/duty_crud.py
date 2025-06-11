from app.models.duty import Duty
from app.schemas.duty_schema import DutyCreate, DutyUpdate
from sqlmodel import Session, select
import uuid


def create_duty(session: Session, duty: DutyCreate) -> Duty:
    """
    Create a new duty in the database.
    """
    db_duty = Duty.model_validate(duty)
    session.add(db_duty)
    session.commit()
    session.refresh(db_duty)
    return db_duty


def get_duty(session: Session, duty_id: uuid.UUID) -> Duty:
    """
    Retrieve a duty by ID from the database.
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")
    return db_duty


def get_all_duties(session: Session) -> list[Duty]:
    """
    Retrieve all duties from the database.
    """
    statement = select(Duty)
    return session.exec(statement).all()


def get_duty_by_name(session: Session, duty_name: str) -> Duty:
    """
    Retrieve a duty by its name from the database.
    """
    statement = select(Duty).where(Duty.name == duty_name)
    db_duty = session.exec(statement).first()
    return db_duty


def update_duty(session: Session, duty_id: uuid.UUID, duty_update: DutyUpdate) -> Duty:
    """
    Update an existing duty in the database.
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
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")

    session.delete(db_duty)
    session.commit()
