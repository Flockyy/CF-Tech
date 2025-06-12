from typing import Optional
import uuid
from sqlmodel import Field, Relationship, SQLModel
from datetime import date

from app.models.course import CourseBase
from app.models.trainee import TraineeBase


class RegistrationBase(SQLModel, table=True):
    """
    Registration model to describe a regisration that can be linked to a trainee for a course.
    The rules applied here are directly the rules applied to the SQL database.
    """

    __tablename__ = "registrations"

    trainee_id: uuid.UUID = Field(primary_key=True, foreign_key="trainees.id")
    course_id: uuid.UUID = Field(primary_key=True, foreign_key="courses.id")
    registration_date: date = Field(...)
    registration_status: str = Field(...)

    trainee: Optional[TraineeBase] = Relationship(back_populates="registrations")
    course: Optional[CourseBase] = Relationship(back_populates="registrations")


def test():
    reg1 = RegistrationBase(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        registration_date="2025-06-06",
        registration_status="PENDING",
    )
    print(reg1)


if __name__ == "__main__":
    test()
