import uuid
from sqlmodel import Field, SQLModel
from datetime import date


class RegistrationBase(SQLModel, table=True):
    """
    Registration model to describe a regisration that can be linked to a trainee for a course.
    The rules applied here are directly the rules applied to the SQL database.
    """

    __tablename__ = "registration"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # TODO: add the foreign key constraint
    trainee_id: uuid.UUID = Field(...)
    # TODO: add the foreign key constraint
    course_id: uuid.UUID = Field(...)
    registration_date: date = Field(...)
    registration_status: str = Field(...)


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
