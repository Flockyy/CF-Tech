from app.schemas.trainer_schema import TrainerCreate, TrainerUpdate
from app.models.trainer import Trainer
from typing import Optional
from sqlmodel import Session, select
import uuid

def create_trainer(session: Session, trainer: TrainerCreate) -> Trainer:
    """
    Create a new trainer in the database.
    """
    db_trainer = Trainer.model_validate(trainer)
    session.add(db_trainer)
    session.commit()
    session.refresh(db_trainer)
    return db_trainer


def get_trainer(session: Session, trainer_id: uuid.UUID) -> Optional[Trainer]:
    """
    Retrieve a trainer by ID from the database.
    """
    return session.get(Trainer, trainer_id)


def get_all_trainers(session: Session) -> list[Trainer]:
    """
    Retrieve all trainers from the database.
    """
    statement = select(Trainer)
    return session.exec(statement).all()


def update_trainer(
    session: Session, trainer_id: str, trainer_update: TrainerUpdate
) -> Optional[Trainer]:
    """
    Update an existing trainer in the database.
    """
    db_trainer = session.get(Trainer, trainer_id)
    if not db_trainer:
        return None

    for key, value in trainer_update.model_dump(exclude_unset=True).items():
        setattr(db_trainer, key, value)

    session.commit()
    session.refresh(db_trainer)
    return db_trainer


def delete_trainer(session: Session, trainer_id: uuid.UUID) -> bool:
    """
    Delete a trainer by ID from the database.
    """
    db_trainer = session.get(Trainer, trainer_id)
    if not db_trainer:
        return False

    session.delete(db_trainer)
    session.commit()
    return True


def get_trainer_by_email(session: Session, email: str) -> Trainer:
    """
    Retrieve a trainer by their email from the database.
    """
    statement = select(Trainer).where(Trainer.email == email)
    result = session.exec(statement).first()
    return result
