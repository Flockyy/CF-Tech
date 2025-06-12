import os
import sys
from typing import Optional

sys.path.append(os.getcwd())

from app.crud.course_crud import get_course_by_title
from app.crud.trainee_crud import get_trainee
from app.schemas.trainee_schema import TraineeCreate

from sqlmodel import Session, create_engine, SQLModel
from app.models.registration import RegistrationBase
from app.schemas.registration_schema import RegistrationCreate, RegistrationStatus
import uuid
from datetime import date, datetime


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


def get_registration(
    session: Session, trainee_id: uuid.UUID, course_id: uuid.UUID
) -> Optional[RegistrationBase]:
    """
    Retrieve a registration by it's trainee_id and it's course_id from the database.
    """
    return session.get(
        entity=RegistrationBase,
        ident={"trainee_id": trainee_id, "course_id": course_id},
    )


def test():
    """Test the module functions"""

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        trainee1 = TraineeCreate(
            first_name="Cesar",
            last_name="Gattano",
            email="cesar.gattano@gmail.com",
            role="user",
            date_of_birth=datetime(
                year=1995, month=7, day=25, hour=0, minute=0, second=0
            ),
            study_level="PHD",
            phone_number="+33658596061",
            registration_date=datetime(
                year=2025, month=5, day=20, hour=0, minute=0, second=0
            ),
        )

        # trainee_db = create_trainee(session=session, trainee=trainee1)
        trainee_db = get_trainee(
            session=session, trainee_id=uuid.UUID("f74c4f9d619649369b0c7afda2a29835")
        )

        course_db = get_course_by_title(db=session, title="Data Eng")

        reg1 = RegistrationCreate(
            trainee_id=trainee_db.id,
            course_id=course_db.id,
            registration_date=date.today(),
            registration_status=RegistrationStatus.pending,
        )
        print(reg1)

        registration_db = get_registration(
            session=session, trainee_id=trainee_db.id, course_id=course_db.id
        )
        # registration_db = create_registration(session, reg1)
        print(
            f"Registration: {registration_db} suivie par {registration_db.trainee.first_name} au cours de {registration_db.course.title}"
        )


if __name__ == "__main__":
    test()
