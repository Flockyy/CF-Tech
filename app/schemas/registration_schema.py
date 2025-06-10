import uuid
from pydantic import BaseModel, Field
from datetime import date
import enum


class RegistrationStatus(str, enum.Enum):
    registered = "REGISTERED"
    unregistered = "UNREGISTERED"
    pending = "PENDING"


# Properties to receive via API on creation
class RegistrationCreate(BaseModel):
    """
    Rules applied via pydantic for the creation of a classroom in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    trainee_id: uuid.UUID = Field(...)
    course_id: uuid.UUID = Field(...)
    registration_date: date = Field(...)
    registration_status: RegistrationStatus = Field(...)


# # Properties to receive via API on update
# class RegistrationUpdate:
#     trainee_id: uuid
#     course_id: uuid
#     registration_status: str


def test():

    print([t.value for t in RegistrationStatus])

    reg3 = RegistrationCreate(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        registration_date=date.today(),
        registration_status="TRAINING",
    )
    print(reg3)


if __name__ == "__main__":
    test()
