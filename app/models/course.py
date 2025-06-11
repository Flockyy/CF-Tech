import uuid
from sqlmodel import Field, Relationship, SQLModel
from datetime import date
from typing import List, Optional
import enum

from app.models.trainer import Trainer


class CourseStatus(str, enum.Enum):
    open = "OPEN"
    closed = "CLOSED"
    archived = "ARCHIVED"


class CourseBase(SQLModel, table=True):
    """Course model to describe a course that can be linked
    to registrations and attendances.
    The rules applied here are directly the rules applied to the SQL database.
    """

    __tablename__ = "courses"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = None
    date_start: date = Field(...)
    date_end: date = Field(...)
    room_id: Optional[uuid.UUID] = Field(default=None, foreign_key="rooms.id")
    trainer_id: Optional[uuid.UUID] = Field(default=None, foreign_key="trainers.id")
    max_capacity: int = Field(...)
    status: str = Field(default=CourseStatus.open)
    prerequisite: Optional[str] = None

    trainer: Optional[Trainer] = Relationship(back_populates="courses")
    registrations: List["RegistrationBase"] = Relationship(back_populates="course")


def test():
    course1 = CourseBase(
        title="Data Eng",
        description="Third Data eng session",
        date_start="2025-06-30",
        date_end="2025-08-29",
        room_id=uuid.uuid4(),
        trainer_id=uuid.uuid4(),
        max_capacity=10,
        prerequisite="SQL, Python",
    )
    print(course1)


if __name__ == "__main__":
    test()
