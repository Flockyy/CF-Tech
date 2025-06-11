import os, sys

sys.path.append(os.getcwd())
from app.crud.room_crud import get_room
from app.crud.trainer_crud import create_trainer, get_trainer
from app.schemas.trainer_schema import TrainerCreate
from sqlmodel import Session, create_engine, SQLModel
from app.models.course import CourseBase
from app.schemas.course_schema import CourseCreate
import uuid


def create_course(db: Session, course_in: CourseCreate) -> CourseBase:
    """Insert an entity in the table courses of the database connected as 'db',
    based on the object 'course_in'. 'course_in' is already filtered on the pydantic
    rules set-up in the class CourseCreate.

    Args:
        db (Session): The session connected to the database
        course_in (CourseCreate): The course to instert respecting the pydantic rules set-up in the class CourseCreate.

    Returns:
        CourseBase: The content of the entry in the database.
    """
    course_db = CourseBase(
        title=course_in.title,
        description=course_in.description,
        date_start=course_in.date_start,
        date_end=course_in.date_end,
        room_id=course_in.room_id,
        trainer_id=course_in.trainer_id,
        max_capacity=course_in.max_capacity,
        prerequisite=course_in.prerequisite,
    )
    db.add(course_db)
    db.commit()
    db.refresh(course_db)

    return course_db


def test():
    """Test the module functions"""

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        trainer1 = TrainerCreate(
            first_name="Benjamin",
            last_name="Quinet",
            email="benjamin.quinet@gmail.com",
            role="user",
            specialty="Millions de souffrances",
            hourly_rate=50.21,
            bio="Voir linkedIn",
        )

        trainer_db = get_trainer(
            session=session, trainer_id=uuid.UUID("c14fcc6173ab4396aa4405867845c900")
        )

        room_db = get_room(
            db=session, room_id=uuid.UUID("3281cb2cb0144a059aad70e43aa640a2")
        )

        course1 = CourseCreate(
            title="Data Eng",
            description="First data eng course",
            date_start="2025-06-30",
            date_end="2025-08-29",
            room_id=room_db.id,
            trainer_id=trainer_db.id,
            max_capacity=room_db.capacity,
            prerequisite="SQL, Python",
        )
        print(course1)

        course_db = create_course(session, course1)


if __name__ == "__main__":
    test()
