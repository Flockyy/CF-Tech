import os, sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel
from app.models.room import RoomBase, EquipmentBase
from app.schemas.room_schema import (
    ClassroomCreate,
    EquipmentCreate,
    RegisteredEquipmentCreate,
    InRoomEquipmentCreate,
    InRoomRegisteredEquipmentCreate,
)


def create_classroom(
    room_in: ClassroomCreate, add_to_db: bool = False, db: Session | None = None
) -> RoomBase:
    """Insert an entity in the table rooms of the database connected as 'db',
    based on the object 'room_in'. 'room_in' is already filtered on the pydantic
    rules set-up in the class ClassroomCreate.

    Args:
        room_in (ClassroomCreate): The classroom to insert respecting the pydantic rules set-up in the class ClassroomCreate.
        add_to_db (bool): Should the classroom be already added to the database ? If False, means that if will be added via a relationship.
        db (Session): The session connected to the database

    Returns:
        RoomBase: The content of the entry in the database.
    """
    room_db = RoomBase(
        name=room_in.name, capacity=room_in.capacity, location=room_in.location
    )
    if add_to_db and db:
        db.add(room_db)
        db.commit()
        db.refresh(room_db)

    return room_db


def create_equipment(
    equipment_in: EquipmentCreate, add_to_db: bool = False, db: Session | None = None
) -> EquipmentBase:
    """Insert an entity in the table equipments of the database connected as 'db',
    based on the object 'equipment_in'. 'equipment_in' is already filtered on the pydantic
    rules set-up in the class EquipmentCreate.

    Args:
        equipment_in (EquipmentCreate): The equipment to insert respecting the pydantic rules set-up in the class EquipmentCreate.
        add_to_db (bool): Should the equipment be already added to the database ? If False, means that if will be added via a relationship.
        db (Session): The session connected to the database

    Returns:
        RoomBase: The content of the entry in the database.
    """
    params = {"name": equipment_in.name}
    if isinstance(equipment_in, RegisteredEquipmentCreate):
        params["serial_number"] = equipment_in.serial_number
    if isinstance(equipment_in, InRoomEquipmentCreate):
        params["room"] = equipment_in.room

    equipment_db = EquipmentBase(**params)
    if add_to_db and db:
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
    room_db = create_classroom(room)

    equipment1 = EquipmentCreate(name="Welcome desk")
    print(equipment1)
    equipment2 = RegisteredEquipmentCreate(name="Computer", serial_number="aU1854Eqd4")
    print(equipment2)
    equipment3 = InRoomEquipmentCreate(name="White board", room=room_db)
    print(equipment3)
    equipment4 = InRoomRegisteredEquipmentCreate(
        name="TV", room=room_db, serial_number="yU1854Eqd5"
    )
    print(equipment4)

    with Session(engine) as session:
        equipment_db = create_equipment(equipment1, True, session)
        equipment_db = create_equipment(equipment2, True, session)
        equipment_db = create_equipment(equipment3, True, session)
        equipment_db = create_equipment(equipment4, True, session)


if __name__ == "__main__":
    test()
