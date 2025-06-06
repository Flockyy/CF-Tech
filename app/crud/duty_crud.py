from app.models.duty import Duty
from app.schemas.duties_schema import DutyCreate, DutyUpdate
from sqlmodel import Session


def create_duty(session: Session, duty: DutyCreate) -> Duty:
    """
    Create a new duty in the database.
    """
    db_duty = Duty.model_validate(duty)
    session.add(db_duty)
    session.commit()
    session.refresh(db_duty)
    return db_duty


def get_duty(session: Session, duty_id: str) -> Duty:
    """
    Retrieve a duty by ID from the database.
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")
    return db_duty


def update_duty(session: Session, duty_id: str, duty_update: DutyUpdate) -> Duty:
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


def delete_duty(session: Session, duty_id: str) -> None:
    """
    Delete a duty from the database.
    """
    db_duty = session.get(Duty, duty_id)
    if not db_duty:
        raise ValueError("Duty not found")

    session.delete(db_duty)
    session.commit()
