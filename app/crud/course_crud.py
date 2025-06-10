import os, sys

sys.path.append(os.getcwd())
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

    sqlite_file_name = "ceb.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    course1 = CourseCreate(
        title="Data Eng",
        description="First data eng course",
        date_start="2025-06-30",
        date_end="2025-08-29",
        room_id=uuid.uuid4(),
        trainer_id=uuid.uuid4(),
        max_capacity=10,
        prerequisite=None,
    )
    print(course1)

    with Session(engine) as session:
        course_db = create_course(session, course1)


if __name__ == "__main__":
    test()
