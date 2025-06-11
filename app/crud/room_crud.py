import os, sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel, select, Sequence
from uuid import UUID
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


def get_room(db: Session, room_id: UUID) -> RoomBase:
    """Select a room in the database given its ID.

    Args:
        db (Session): The session connected to the database
        room_id (UUID): The room ID in the database

    Raises:
        ValueError: No room found with this ID

    Returns:
        RoomBase: The room and its equipments
    """
    room_db = db.get(RoomBase, room_id)
    if not room_db:
        raise ValueError("Room with ID {} member not found")
    return room_db


def select_all_rooms(db: Session) -> list[RoomBase]:
    """Select all rooms in the database and return them in a list.

    Args:
        db (Session): The session connected to the database

    Returns:
        list[RoomBase]: The list of rooms with their equipments 
    """
    rooms_db = db.exec(select(RoomBase)).all()
    return rooms_db


def select_room(db: Session, name: str) -> RoomBase:
    """Select a room given its name.

    Args:
        db (Session): The session connected to the database
        name (str): The name of the room

    Returns:
        RoomBase: The room and its equipments
    """
    room_db = db.exec(select(RoomBase).where(RoomBase.name == name)).one()
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
        params["rooms"] = equipment_in.rooms

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

    # Create 3 rooms (but do not push them yet in the database)
    room1 = ClassroomCreate(
        name="A101", capacity=18, location="Building North, 1st floor"
    )
    print(room1)
    room1_db = create_classroom(room1)
    room2 = ClassroomCreate(
        name="A102", capacity=36, location="Building North, 1st floor"
    )
    print(room2)
    room2_db = create_classroom(room2)
    room3 = ClassroomCreate(
        name="A103", capacity=18, location="Building North, 1st floor"
    )
    print(room3)
    room3_db = create_classroom(room3)

    equipment1 = EquipmentCreate(name="Welcome desk")
    print(equipment1)
    equipment2 = RegisteredEquipmentCreate(name="Computer", serial_number="aU1854Eqd4")
    print(equipment2)
    equipment3 = InRoomEquipmentCreate(
        name="White board", rooms=[room1_db, room2_db, room3_db]
    )
    print(equipment3)
    equipment4 = InRoomRegisteredEquipmentCreate(
        name="TV", rooms=[room2_db], serial_number="yU1854Eqd5"
    )
    print(equipment4)

    with Session(engine) as session:
        equipment_db = create_equipment(equipment1, True, session)
        equipment_db = create_equipment(equipment2, True, session)
        equipment_db = create_equipment(equipment3, True, session)
        equipment_db = create_equipment(equipment4, True, session)

        rooms = select_all_rooms(session)
        for room in rooms:
            print(room)

        room = select_room(session, "A103")
        print(room)
        print(room.equipments)

        room_bis = get_room(session, room.id)
        print(room_bis)
        print(room_bis.equipments)

if __name__ == "__main__":
    test()
