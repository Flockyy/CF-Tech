import os
import sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel
from app.models.registration import RegistrationBase
from app.schemas.registration_schema import RegistrationCreate, RegistrationStatus
import uuid
from datetime import date


def create_registration(
    db: Session, registration_in: RegistrationCreate
) -> RegistrationBase:
    """Insert an entity in the table registrations of the database connected as 'db',
    based on the object 'registration_in'. 'registration_in' is already filtered on the pydantic
    rules set-up in the class RegistrationCreate.

    Args:
        db (Session): The session connected to the database
        registration_in (RegistrationCreate): The registration to instert respecting the pydantic rules set-up in the class RegistrationCreate.

    Returns:
        RegistrationBase: The content of the entry in the database.
    """
    registration_db = RegistrationBase(
        trainee_id=registration_in.trainee_id,
        course_id=registration_in.course_id,
        registration_date=registration_in.registration_date,
        registration_status=registration_in.registration_status,
    )
    db.add(registration_db)
    db.commit()
    db.refresh(registration_db)

    return registration_db


def test():
    """Test the module functions"""

    sqlite_file_name = "ceb.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    reg1 = RegistrationCreate(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        registration_date=date.today(),
        registration_status=RegistrationStatus.training,
    )
    print(reg1)

    with Session(engine) as session:
        create_registration(session, reg1)
        # TODO : return registration_db ?


if __name__ == "__main__":
    test()
