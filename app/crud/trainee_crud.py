from app.models.trainee import Trainee
from app.schemas.trainee_schema import TraineeCreate, TraineeUpdate
from sqlmodel import Session, select
import uuid


def create_trainee(session: Session, trainee: TraineeCreate) -> Trainee:
    """
    Create a new trainee in the database.
    Args:
        session (Session): The database session.
        trainee (TraineeCreate): The trainee data to create.
    Returns:
        Trainee: The created trainee.
    """

    db_trainee = Trainee.model_validate(trainee)
    session.add(db_trainee)
    session.commit()
    session.refresh(db_trainee)
    return db_trainee


def get_trainee(session: Session, trainee_id: uuid.UUID) -> Trainee:
    """
    Retrieve a trainee by their ID from the database.
    Args:
        session (Session): The database session.
        trainee_id (uuid.UUID): The ID of the trainee to retrieve.
    Returns:
        Trainee: The trainee object if found.
    Raises:
        ValueError: If the trainee is not found.
    """
    db_trainee = session.get(Trainee, trainee_id)
    if not db_trainee:
        raise ValueError("Trainee not found")
    return db_trainee


def get_all_trainees(session: Session) -> list[Trainee]:
    """
    Retrieve all trainees from the database.
    Args:
        session (Session): The database session.
    Returns:
        list[Trainee]: A list of all trainee objects.
    """
    statement = select(Trainee)
    return session.exec(statement).all()


def update_trainee(
    session: Session, trainee_id: uuid.UUID, trainee_update: TraineeUpdate
) -> Trainee:
    """
    Update an existing trainee in the database.
    Args:
        session (Session): The database session.
        trainee_id (uuid.UUID): The ID of the trainee to update.
        trainee_update (TraineeUpdate): The updated trainee data.
    Returns:
        Trainee: The updated trainee object.
    Raises:
        ValueError: If the trainee is not found.
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


def delete_trainee(session: Session, trainee_id: uuid.UUID) -> None:
    """
    Delete a trainee from the database.
    Args:
        session (Session): The database session.
        trainee_id (uuid.UUID): The ID of the trainee to delete.
    Raises:
        ValueError: If the trainee is not found.
    """
    db_trainee = session.get(Trainee, trainee_id)
    if not db_trainee:
        raise ValueError("Trainee not found")

    session.delete(db_trainee)
    session.commit()


def get_trainee_by_email(session: Session, email: str) -> Trainee:
    """
    Retrieve a trainee by their email from the database.
    Args:
        session (Session): The database session.
        email (str): The email of the trainee to retrieve.
    Returns:
        Trainee: The trainee object if found.
    """
    statement = select(Trainee).where(Trainee.email == email)
    result = session.exec(statement).first()
    return result
