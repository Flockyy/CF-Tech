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


class ClassroomUpdate(BaseModel):
    """
    Rules applied via pydantic for the update of a classroom in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    name: str | None = Field(default=None, pattern=r"^[A-Z][0-9]{3}$")
    location: str | None = Field(default=None, min_length=2, max_length=50)
    capacity: int | None = Field(default=None, ge=15)


class EquipmentCreate(BaseModel):
    """
    Rules applied via pydantic for the creation of an equipment in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    name: str = Field(...)


class RegisteredEquipmentCreate(EquipmentCreate):
    """
    Rules applied via pydantic for the creation of a registered equipment in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    serial_number: str = Field(
        ..., min_length=10, max_length=10, pattern=r"^([a-z]|[A-Z]|[0-9])+$"
    )


class EquipmentUpdate(BaseModel):
    """
    Rules applied via pydantic for the update of an equipment in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    name: str | None = Field(default=None)
    serial_number: str | None = Field(
        default=None, min_length=10, max_length=10, pattern=r"^([a-z]|[A-Z]|[0-9])+$"
    )


class InRoomEquipmentCreate(EquipmentCreate):
    """
    Rules applied via pydantic for the creation of an equipment placed in some rooms in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    rooms: list[RoomBase] = Field(...)


class InRoomRegisteredEquipmentCreate(RegisteredEquipmentCreate, InRoomEquipmentCreate):
    """
    Rules applied via pydantic for the creation of a registered equipment placed in some rooms in the database.
    The rules are applied by Python before the request to the database is pushed.
    """

    pass


def test():
    # Test create
    room1 = ClassroomCreate(
        name="A101", location="Building North, 1st floor", capacity=15
    )
    print(room1)
    room1_db = RoomBase(name="A101", location="Building North, 1st floor", capacity=15)
    room2 = ClassroomCreate(
        name="A102", location="Building North, 1st floor", capacity=30
    )
    print(room2)
    room2_db = RoomBase(name="A102", location="Building North, 1st floor", capacity=30)
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

    # Test update
    room1 = ClassroomUpdate(
        name="A101", location="Building North, 1st floor", capacity=15
    )
    print(room1)
    room1_db = RoomBase(name="A101", location="Building North, 1st floor", capacity=15)
    room2 = ClassroomUpdate(
        name="A102", location="Building North, 1st floor", capacity=30
    )
    print(room2)
    room2_db = RoomBase(name="A102", location="Building North, 1st floor", capacity=30)
    equipment1 = EquipmentUpdate(name="Welcome desk")
    print(equipment1)
    equipment2 = RegisteredEquipmentUpdate(name="TV", serial_number="aU1854Eqd4")
    print(equipment2)
    equipment3 = InRoomEquipmentUpdate(name="TV", rooms=[room1_db, room2_db])
    print(equipment3)
    equipment4 = InRoomRegisteredEquipmentUpdate(
        name="TV", rooms=[room1_db], serial_number="aU1854Eqd4"
    )
    print(equipment4)


if __name__ == "__main__":
    test()
