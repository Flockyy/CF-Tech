import uuid
from pydantic import BaseModel, Field
from datetime import date


# Properties to receive via API on creation
class AttendanceCreate(BaseModel):
    """
    Rules applied via pydantic for the creation of an attendance in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    trainee_id: uuid.UUID = Field(...)
    course_id: uuid.UUID = Field(...)
    date_course: date = Field(...)
    am: bool = Field(default=False)
    pm: bool = Field(default=False)


def test():

    attendance1 = AttendanceCreate(
        trainee_id=uuid.uuid4(), course_id=uuid.uuid4(), date_course="2025-07-04"
    )
    print(attendance1)


if __name__ == "__main__":
    test()
