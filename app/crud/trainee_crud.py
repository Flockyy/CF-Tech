from app.models.trainee import Trainee
from app.schemas.trainee_schema import TraineeCreate, TraineeUpdate
from sqlmodel import Session


def create_trainee(session: Session, trainee: TraineeCreate) -> Trainee:
    """
    Create a new trainee in the database.
    """
    db_trainee = Trainee.model_validate(trainee)
    session.add(db_trainee)
    session.commit()
    session.refresh(db_trainee)
    return db_trainee


def get_trainee(session: Session, trainee_id: str) -> Trainee:
    """
    Retrieve a trainee by their ID from the database.
    """
    db_trainee = session.get(Trainee, trainee_id)
    if not db_trainee:
        raise ValueError("Trainee not found")
    return db_trainee

def get_all_trainees(session: Session) -> list[Trainee]:
    """
    Retrieve all trainees from the database.
    """
    return session.exec(Trainee.select()).all()

def update_trainee(
    session: Session, trainee_id: str, trainee_update: TraineeUpdate
) -> Trainee:
    """
    Update an existing trainee in the database.
    """
    db_trainee = session.get(Trainee, trainee_id)
    if not db_trainee:
        raise ValueError("Trainee not found")

    trainee_data = trainee_update.model_dump(exclude_unset=True)
    for key, value in trainee_data.items():
        setattr(db_trainee, key, value)

    session.add(db_trainee)
    session.commit()
    session.refresh(db_trainee)
    return db_trainee


def delete_trainee(session: Session, trainee_id: str) -> None:
    """
    Delete a trainee from the database.
    """
    db_trainee = session.get(Trainee, trainee_id)
    if not db_trainee:
        raise ValueError("Trainee not found")

    session.delete(db_trainee)
    session.commit()


def get_trainee_by_email(session: Session, email: str) -> Trainee:
    """
    Retrieve a trainee by their email from the database.
    """
    db_trainee = session.exec(Trainee.select().where(Trainee.email == email)).first()
    if not db_trainee:
        raise ValueError("Trainee with this email not found")
    return db_trainee
