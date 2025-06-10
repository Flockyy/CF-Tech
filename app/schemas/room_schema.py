import os, sys

sys.path.append(os.getcwd())
from pydantic import BaseModel, Field
from app.models.room import RoomBase


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
    rooms: list[RoomBase] = Field(...)


class InRoomRegisteredEquipmentCreate(RegisteredEquipmentCreate, InRoomEquipmentCreate):
    pass


def test():
    room1 = ClassroomCreate(
        name="A101", location="Building North, 1st floor", capacity=15
    )
    print(room1)
    room1_db = RoomBase(
        name="A101", location="Building North, 1st floor", capacity=15
    )
    room2 = ClassroomCreate(
        name="A102", location="Building North, 1st floor", capacity=30
    )
    print(room2)
    room2_db = RoomBase(
        name="A102", location="Building North, 1st floor", capacity=30
    )
    equipment1 = EquipmentCreate(name="Welcome desk")
    print(equipment1)
    equipment2 = RegisteredEquipmentCreate(name="TV", serial_number="aU1854Eqd4")
    print(equipment2)
    equipment3 = InRoomEquipmentCreate(name="TV", rooms=[room1_db, room2_db])
    print(equipment3)
    equipment4 = InRoomRegisteredEquipmentCreate(
        name="TV", rooms=[room1_db], serial_number="aU1854Eqd4"
    )
    print(equipment4)


if __name__ == "__main__":
    test()
