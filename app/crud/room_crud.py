import os, sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel
from app.models.room import RoomBase, EquipmentBase
from app.schemas.room_schema import (
    ClassroomCreate,
    EquipmentCreate,
    RegisteredEquipmentCreate,
    InRoomEquipmentCreate,
    InRoomRegisteredEquipmentCreate
)


def create_classroom(db: Session, room_in: ClassroomCreate) -> RoomBase:
    """Insert an entity in the table rooms of the database connected as 'db',
    based on the object 'room_in'. 'room_in' is already filtered on the pydantic
    rules set-up in the class ClassroomCreate.

    Args:
        db (Session): The session connected to the database
        room_in (ClassroomCreate): The classroom to instert respecting the pydantic rules set-up in the class ClassroomCreate.

    Returns:
        RoomBase: The content of the entry in the database.
    """
    room_db = RoomBase(
        name=room_in.name, capacity=room_in.capacity, location=room_in.location
    )
    db.add(room_db)
    db.commit()
    db.refresh(room_db)

    return room_db


def create_equipment(db: Session, equipment_in: EquipmentCreate) -> EquipmentBase:
    """Insert an entity in the table equipments of the database connected as 'db',
    based on the object 'equipment_in'. 'equipment_in' is already filtered on the pydantic
    rules set-up in the class EquipmentCreate.

    Args:
        db (Session): The session connected to the database
        equipment_in (ClassroomCreate): The classroom to instert respecting the pydantic rules set-up in the class ClassroomCreate.

    Returns:
        RoomBase: The content of the entry in the database.
    """
    params = {"name": equipment_in.name}
    if isinstance(equipment_in, RegisteredEquipmentCreate):
        params["serial_number"] = equipment_in.serial_number
    if isinstance(equipment_in, InRoomEquipmentCreate):
        params["id_room"] = equipment_in.id_room

    equipment_db = EquipmentBase(**params)
    db.add(equipment_db)
    db.commit()
    db.refresh(equipment_db)

    return equipment_db


def test():
    """Test the module functions"""

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    room = ClassroomCreate(
        name="A101", capacity=18, location="Building North, 1st floor"
    )
    print(room)
    equipment1 = EquipmentCreate(name="Welcome desk")
    print(equipment1)
    equipment2 = RegisteredEquipmentCreate(name="Computer", serial_number="aU1854Eqd4")
    print(equipment2)


    with Session(engine) as session:
        room_db = create_classroom(session, room)

        equipment3 = InRoomEquipmentCreate(name="White board", id_room=room_db.id)
        print(equipment3)
        equipment4 = InRoomRegisteredEquipmentCreate(name="TV", id_room=room_db.id, serial_number="yU1854Eqd5")
        print(equipment4)

        equipment_db = create_equipment(session, equipment1)
        equipment_db = create_equipment(session, equipment2)
        equipment_db = create_equipment(session, equipment3)
        equipment_db = create_equipment(session, equipment4)


if __name__ == "__main__":
    test()
