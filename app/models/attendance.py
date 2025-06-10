import uuid
from sqlmodel import Field, SQLModel
from datetime import date
from typing import Optional


class AttendanceBase(SQLModel, table=True):
    """
    Attendance model to describe an attendance that can be linked
    to courses and trainees.
    The rules applied here are directly the rules applied to the SQL database.
    """

    __tablename__ = "attendances"

    # TODO: add the foreign key constraint
    trainee_id: uuid.UUID = Field(primary_key=True)
    # TODO: add the foreign key constraint
    course_id: uuid.UUID = Field(primary_key=True)
    date_course: date = Field(...)
    am: bool = Field(default=False)
    pm: bool = Field(default=False)


def test():
    attendance1 = AttendanceBase(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        date_course="2025-06-30",
    )
    print(attendance1)


if __name__ == "__main__":
    test()
