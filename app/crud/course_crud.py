import os, sys

sys.path.append(os.getcwd())
from app.crud.room_crud import get_room
from app.crud.trainer_crud import create_trainer, get_trainer
from app.schemas.trainer_schema import TrainerCreate
from sqlmodel import Session, create_engine, SQLModel, select
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


def get_course(db: Session, course_id: uuid.UUID) -> CourseBase:
    """Select a course in the database given its ID.

    Args:
        db (Session): The session connected to the database
        course_id (UUID): The course ID in the database

    Raises:
        ValueError: No course found with this ID

    Returns:
        CourseBase: The course
    """
    course_db = db.get(CourseBase, course_id)
    if not course_db:
        raise ValueError(f"Course with ID {course_id} not found")
    return course_db


def get_all_courses(db: Session) -> list[CourseBase]:
    """Select all courses in the database and return them in a list.

    Args:
        db (Session): The session connected to the database

    Returns:
        list[CourseBase]: The list of courses
    """
    courses_db = db.exec(select(CourseBase)).all()
    return courses_db


def get_course_by_title(db: Session, title: str) -> CourseBase:
    """Select a course given its title.

    Args:
        db (Session): The session connected to the database
        title (str): The title of the course

    Returns:
        CourseBase: The course
    """
    course_db = db.exec(select(CourseBase).where(CourseBase.title == title)).one()
    return course_db


def test():
    """Test the module functions"""

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        trainer1 = TrainerCreate(
            first_name="Jean",
            last_name="Sérien",
            email="jean.serien@gmail.com",
            role="user",
            specialty="Pot-au-feu",
            hourly_rate=40.21,
            bio="Rien du tout",
        )

        # trainer_in = create_trainer(session, trainer1)

        trainer_db = get_trainer(
            session=session, trainer_id=uuid.UUID("c7fe916901154c6ab87a595b4a700d32")
        )

        room_db = get_room(
            db=session, room_id=uuid.UUID("338ece5b75b44823af06623422b531f1")
        )

        course1 = CourseCreate(
            title="Dev IA",
            description="Third dev IA course",
            date_start="2025-06-30",
            date_end="2025-08-29",
            room_id=room_db.id,
            trainer_id=trainer_db.id,
            max_capacity=room_db.capacity,
            prerequisite="SQL, Python",
        )
        print(course1)

        # course_db = create_course(db=session, course_in=course1)

        courses_db = get_all_courses(db=session)
        print(f"All courses: {courses_db}")

        course_di = get_course_by_title(db=session, title="Dev IA")
        print(f"Course dev IA: {course_di} presenté par {course_di.trainer.first_name}")


if __name__ == "__main__":
    test()
