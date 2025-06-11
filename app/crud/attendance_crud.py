import os
import sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel
from app.models.attendance import AttendanceBase
from app.schemas.attendance_schema import AttendanceCreate
import uuid


def create_attendance(db: Session, attendance_in: AttendanceCreate) -> AttendanceBase:
    """
    Insert an entity in the table attendances of the database connected as 'db',
    based on the object 'attendance_in'. 'attendance_in' is already filtered on the pydantic
    rules set-up in the class AttendanceCreate.

    Args:
        db (Session): The session connected to the database
        attendance_in (AttendanceCreate): The attendance to instert respecting the pydantic rules set-up in the class AttendanceCreate.

    Returns:
        AttendanceBase: The content of the entry in the database.
    """
    attendance_db = AttendanceBase(
        trainee_id=attendance_in.trainee_id,
        course_id=attendance_in.course_id,
        date_course=attendance_in.date_course,
    )
    db.add(attendance_db)
    db.commit()
    db.refresh(attendance_db)

    return attendance_db


def test():
    """Test the module functions"""

    sqlite_file_name = "ceb.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    attendance1 = AttendanceCreate(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        date_course="2025-06-30",
    )
    print(attendance1)

    with Session(engine) as session:
        create_attendance(session, attendance1)
        # TODO : return attendance_db ?


if __name__ == "__main__":
    test()
