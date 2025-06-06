import uuid
from pydantic import BaseModel, Field


class ClassroomCreate(BaseModel):
    """
    Rules applied via pydantic for the creation of a classroom in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    name: str = Field(..., pattern=r"^[A-Z][0-9]{3}$")
    location: str = Field(..., min_length=2, max_length=50)
    capacity: int | None = Field(default=None, ge=15)


class EquipmentCreate(BaseModel):
    name: str = Field(...)


class RegisteredEquipmentCreate(EquipmentCreate):
    serial_number: str = Field(
        ..., min_length=10, max_length=10, pattern=r"^([a-z]|[A-Z]|[0-9])+$"
    )


class InRoomEquipmentCreate(EquipmentCreate):
    id_room: uuid.UUID = Field(...)

class InRoomRegisteredEquipmentCreate(RegisteredEquipmentCreate, InRoomEquipmentCreate):
    pass


def test():
    room1 = ClassroomCreate(
        name="A101", location="Building North, 1st floor", capacity=15
    )
    print(room1)
    equipment1 = EquipmentCreate(name="Welcome desk")
    print(equipment1)
    equipment2 = RegisteredEquipmentCreate(name="TV", serial_number="aU1854Eqd4")
    print(equipment2)
    equipment3 = InRoomEquipmentCreate(name="TV", id_room=uuid.uuid4())
    print(equipment3)
    equipment4 = InRoomRegisteredEquipmentCreate(name="TV", id_room=uuid.uuid4(), serial_number="aU1854Eqd4")
    print(equipment4)


if __name__ == "__main__":
    test()
