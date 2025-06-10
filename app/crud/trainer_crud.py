from app.schemas.trainer_schema import TrainerCreate, TrainerUpdate
from app.models.trainer import Trainer
from typing import Optional
from sqlmodel import Session


def create_trainer(session: Session, trainer: TrainerCreate) -> Trainer:
    """
    Create a new trainer in the database.
    """
    db_trainer = Trainer.model_validate(trainer)
    session.add(db_trainer)
    session.commit()
    session.refresh(db_trainer)
    return db_trainer


def get_trainer(session: Session, trainer_id: str) -> Optional[Trainer]:
    """
    Retrieve a trainer by ID from the database.
    """
    return session.get(Trainer, trainer_id)

def get_all_trainers(session: Session) -> list[Trainer]:
    """
    Retrieve all trainers from the database.
    """
    return session.exec(Trainer.select()).all()

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


def delete_trainer(session: Session, trainer_id: str) -> bool:
    """
    Delete a trainer by ID from the database.
    """
    db_trainer = session.get(Trainer, trainer_id)
    if not db_trainer:
        return False

    session.delete(db_trainer)
    session.commit()
    return True
