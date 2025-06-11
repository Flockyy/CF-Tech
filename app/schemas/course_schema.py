from typing import Optional, Self
import uuid
from pydantic import BaseModel, Field, model_validator
from datetime import date
import enum
from app.models.course import CourseStatus


# Properties to receive via API on creation
class CourseCreate(BaseModel):
    """
    Rules applied via pydantic for the creation of a course in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    title: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = None
    date_start: date = Field(
        ...,
        description="Starting date of a course in ISO format (YYYY-MM-DD), must be < to ending date",
    )
    date_end: date = Field(
        ...,
        description="Ending date of a course in ISO format (YYYY-MM-DD), must be > to starting date",
    )
    room_id: uuid.UUID = Field(...)
    trainer_id: uuid.UUID = Field(...)
    max_capacity: int = Field(...)
    status: str = Field(default=CourseStatus.open)
    prerequisite: Optional[str] = None

    @model_validator(mode="after")
    def check_valid_period(cls, self) -> Self:
        """
        Validate that the starting date is before the ending date.
        """
        if self.date_start and self.date_end:
            if self.date_start >= self.date_end:
                raise ValueError("Starting date must be < ending date.")
        else:
            raise ValueError("Starting date and ending date must be provided.")
        return self


def test():

    print([t.value for t in CourseStatus])

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


if __name__ == "__main__":
    test()
