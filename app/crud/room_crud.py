import os, sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel, select, Sequence
from uuid import UUID
from app.models.room import RoomBase, EquipmentBase
from app.schemas.room_schema import (
    ClassroomCreate,
    ClassroomUpdate,
    EquipmentCreate,
    RegisteredEquipmentCreate,
    InRoomEquipmentCreate,
    InRoomRegisteredEquipmentCreate,
    EquipmentUpdate,
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
        raise ValueError(f"Room with ID {room_id} not found")
    return room_db


def get_all_rooms(db: Session) -> list[RoomBase]:
    """Select all rooms in the database and return them in a list.

    Args:
        db (Session): The session connected to the database

    Returns:
        list[RoomBase]: The list of rooms with their equipments
    """
    rooms_db = db.exec(select(RoomBase)).all()
    return rooms_db


def get_room_by_name(db: Session, name: str) -> RoomBase:
    """Select a room given its name.

    Args:
        db (Session): The session connected to the database
        name (str): The name of the room

    Returns:
        RoomBase: The room and its equipments
    """
    room_db = db.exec(select(RoomBase).where(RoomBase.name == name)).one()
    return room_db


def update_classroom(
    db: Session,
    room_id: UUID,
    room_update: ClassroomUpdate,
    apply_update_to_db: bool = False,
) -> RoomBase:
    """Update the entity with ID 'room_id' in the table rooms of the database connected as 'db',
    based on the object 'room_update'. 'room_update' is already filtered on the pydantic
    rules set-up in the class ClassroomUpdate.

    Args:
        db (Session): The session connected to the database
        room_id (UUID): The ID of the room
        room_update (ClassroomUpdate): The classroom data to consider in the update respecting the pydantic rules set-up in the class ClassroomUpdate.
        apply_update_to_db (bool): Should the update be already committed to the database ? If False, commit is postponed.

    Returns:
        RoomBase: The content of the entry in the database after the update.
    """
    room_db = get_room(db, room_id)
    room_data = room_update.model_dump(exclude_unset=True)
    for key, value in room_data.items():
        setattr(room_db, key, value)

    db.add(room_db)
    if apply_update_to_db:
        db.commit()
        db.refresh(room_db)

    return room_db


def put_equipments_in_classroom(
    db: Session,
    room_id: UUID,
    equipment_ids: list[UUID],
    apply_update_to_db: bool = False,
) -> RoomBase:
    """Associate some equipments with IDs 'equipment_ids' with the entity
    of the table rooms with ID 'room_id' of the database connected as 'db'.
    The commit to the database may be postponed using 'apply_update_to_db'.

    Args:
        db (Session): The session connected to the database
        room_id (UUID): The ID of the classroom
        equipment_ids (list[UUID]): The list of IDs of the equipments
        apply_update_to_db (bool): Should the update be already committed to the database ? If False, commit is postponed.

    Returns:
        RoomBase: The content of the entry in the database.
    """
    room_db = get_room(db, room_id)
    for equipment_id in equipment_ids:
        equipment_db = get_equipment(db, equipment_id)
        room_db.equipments.append(equipment_db)

    db.add(room_db)
    if apply_update_to_db:
        db.commit()
        db.refresh(room_db)

    return room_db


def delete_classroom(
    db: Session,
    room_id: UUID,
    apply_delete_to_db: bool = False,
) -> bool:
    """Remove the entity with ID 'room_id' in the table rooms of the database connected as 'db'.

    Args:
        db (Session): The session connected to the database
        room_id (UUID): The ID of the room
        apply_delete_to_db (bool): Should the delete be already committed to the database ? If False, delete is postponed.

    Returns:
        bool: Was the entry removed ?
    """
    room_db = get_room(db, room_id)
    db.delete(room_db)
    if apply_delete_to_db:
        db.commit()

    return True


def remove_equipments_from_classroom(
    db: Session,
    room_id: UUID,
    equipment_ids: list[UUID],
    apply_update_to_db: bool = False,
) -> RoomBase:
    """Disassociate some equipments with IDs 'equipment_ids' with the entity
    of the table rooms with ID 'room_id' of the database connected as 'db'.
    The commit to the database may be postponed using 'apply_update_to_db'.

    Args:
        db (Session): The session connected to the database
        room_id (UUID): The ID of the classroom
        equipment_ids (list[UUID]): The list of IDs of the equipments
        apply_update_to_db (bool): Should the update be already committed to the database ? If False, commit is postponed.

    Returns:
        RoomBase: The content of the entry in the database.
    """
    room_db = get_room(db, room_id)
    for equipment_id in equipment_ids:
        equipment_db = get_equipment(db, equipment_id)
        room_db.equipments.remove(equipment_db)

    db.add(room_db)
    if apply_update_to_db:
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
        params["rooms"] = equipment_in.rooms

    equipment_db = EquipmentBase(**params)
    if add_to_db and db:
        db.add(equipment_db)
        db.commit()
        db.refresh(equipment_db)

    return equipment_db


def get_equipment(db: Session, equipment_id: UUID) -> EquipmentBase:
    """Select an equipment in the database given its ID.

    Args:
        db (Session): The session connected to the database
        equipment_id (UUID): The equipment ID in the database

    Raises:
        ValueError: No equipment found with this ID

    Returns:
        EquipmentBase: The equipment and the associated rooms
    """
    equipment_db = db.get(EquipmentBase, equipment_id)
    if not equipment_db:
        raise ValueError(f"Equipment with ID {equipment_id} not found")
    return equipment_db


def get_all_equipments(db: Session) -> list[EquipmentBase]:
    """Select all equipments in the database and return them in a list.

    Args:
        db (Session): The session connected to the database

    Returns:
        list[EquipmentBase]: The list of equipments with their associated rooms
    """
    equipments_db = db.exec(select(EquipmentBase)).all()
    return equipments_db


def get_equipment_by_name(db: Session, name: str) -> EquipmentBase:
    """Select an equipment given its name.

    Args:
        db (Session): The session connected to the database
        name (str): The name of the equipment

    Returns:
        EquipmentBase: The equipment and its associated rooms
    """
    equipment_db = db.exec(
        select(EquipmentBase).where(EquipmentBase.name == name)
    ).one()
    return equipment_db


def update_equipment(
    db: Session,
    equipment_id: UUID,
    equipment_update: EquipmentUpdate,
    apply_update_to_db: bool = False,
) -> EquipmentBase:
    """Update the entity with ID 'equipment_id' in the table equipments of the database connected as 'db',
    based on the object 'equipment_update'. 'equipment_update' is already filtered on the pydantic
    rules set-up in the class EquipmentUpdate.

    Args:
        db (Session): The session connected to the database
        equipment_id (UUID): The ID of the equipment
        equipment_update (EquipmentUpdate): The equipment data to consider in the update respecting the pydantic rules set-up in the class EquipmentUpdate.
        apply_update_to_db (bool): Should the update be already committed to the database ? If False, commit is postponed.

    Returns:
        EquipmentBase: The content of the entry in the database after the update.
    """
    equipment_db = get_equipment(db, equipment_id)
    equipment_data = equipment_update.model_dump(exclude_unset=True)
    for key, value in equipment_data.items():
        setattr(equipment_db, key, value)

    db.add(equipment_db)
    if apply_update_to_db:
        db.commit()
        db.refresh(equipment_db)

    return equipment_db


def put_equipment_in_classrooms(
    db: Session,
    equipment_id: UUID,
    room_ids: list[UUID],
    apply_update_to_db: bool = False,
) -> EquipmentBase:
    """Associate an equipment with ID 'equipment_id' with the entities
    of the table rooms with IDs 'room_ids' of the database connected as 'db'.
    The commit to the database may be postponed using 'apply_update_to_db'.

    Args:
        db (Session): The session connected to the database
        equipment_id (UUID): The ID of the equipment
        room_ids (list[UUID]): The list of IDs of the rooms
        apply_update_to_db (bool): Should the update be already committed to the database ? If False, commit is postponed.

    Returns:
        EquipmentBase: The content of the entry in the database.
    """
    equipment_db = get_equipment(db, equipment_id)
    for room_id in room_ids:
        room_db = get_room(db, room_id)
        equipment_db.rooms.append(room_db)

    db.add(equipment_db)
    if apply_update_to_db:
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

    # Create 4 equipments
    equipment1 = EquipmentCreate(name="Welcome desk")
    print(equipment1)
    equipment2_1 = RegisteredEquipmentCreate(
        name="Computer1", serial_number="aU1854Eqd4"
    )
    print(equipment2_1)
    equipment2_2 = RegisteredEquipmentCreate(
        name="Computer2", serial_number="54FREZKfNf"
    )
    print(equipment2_2)
    equipment2_3 = RegisteredEquipmentCreate(
        name="Computer3", serial_number="fre4GR56E8"
    )
    print(equipment2_3)
    equipment3 = InRoomEquipmentCreate(
        name="White board", rooms=[room1_db, room2_db, room3_db]
    )
    print(equipment3)
    equipment4 = InRoomRegisteredEquipmentCreate(
        name="TV", rooms=[room2_db], serial_number="yU1854Eqd5"
    )
    print(equipment4)
    equipment5 = EquipmentCreate(name="Table")
    print(equipment5)

    # Push everything in the database
    with Session(engine) as session:
        create_equipment(equipment1, True, session)
        create_equipment(equipment2_1, True, session)
        create_equipment(equipment2_2, True, session)
        create_equipment(equipment2_3, True, session)
        create_equipment(equipment3, True, session)
        create_equipment(equipment4, True, session)
        create_equipment(equipment5, True, session)

        # Select some rooms from the database
        rooms = get_all_rooms(session)
        for room in rooms:
            print(room)

        room = get_room_by_name(session, "A103")
        print(room)
        print(room.equipments)

        room_bis = get_room(session, room.id)
        print(room_bis)
        print(room_bis.equipments)

        # Select some equipments from the database
        equipments = get_all_equipments(session)
        for equipment in equipments:
            print(equipment)

        equipment = get_equipment_by_name(session, "White board")
        print(equipment)
        print(equipment.rooms)

        equipment_bis = get_room(session, room.id)
        print(equipment_bis)
        print(equipment_bis.equipments)

        # Update a room
        room_db = get_room_by_name(session, "A103")
        print(room_db)
        room_update = ClassroomUpdate(capacity=36)
        room_db = update_classroom(session, room_db.id, room_update)
        print(room_db)
        room_update = ClassroomUpdate(name="B209")
        room_db = update_classroom(session, room_db.id, room_update)
        print(room_db)
        room_update = ClassroomUpdate(location="Building B, floor 2")
        room_db = update_classroom(session, room_db.id, room_update, True)
        print(room_db)

        # Add equipments to room
        room_db = get_room_by_name(session, "A102")
        equipment_ids = []
        equipment_ids.append(get_equipment_by_name(session, "Computer1").id)
        equipment_ids.append(get_equipment_by_name(session, "Computer2").id)
        equipment_ids.append(get_equipment_by_name(session, "Computer3").id)
        room_db = put_equipments_in_classroom(session, room_db.id, equipment_ids, True)
        print(room_db)

        # Update an equipment
        equipment_db = get_equipment_by_name(session, "Welcome desk")
        print(equipment_db)
        equipment_update = EquipmentUpdate(serial_number="dzlehr4945")
        equipment_db = update_equipment(session, equipment_db.id, equipment_update)
        print(equipment_db)
        equipment_update = EquipmentUpdate(name="Welcome IA robot Alfonzo")
        equipment_db = update_equipment(session, equipment_db.id, equipment_update)
        print(equipment_db)

        # Add rooms to equipment
        equipment_db = get_equipment_by_name(session, "Table")
        room_ids = []
        room_ids.append(get_room_by_name(session, "A101").id)
        room_ids.append(get_room_by_name(session, "A102").id)
        room_ids.append(get_room_by_name(session, "B209").id)
        equipment_db = put_equipment_in_classrooms(
            session, equipment_db.id, room_ids, True
        )
        print(equipment_db)

        # Remove a room
        new_room = ClassroomCreate(
            name="A301", capacity=150, location="Building North, 3rd floor"
        )
        print(new_room)
        new_room_db = create_classroom(new_room, True, session)
        delete_classroom(session, new_room_db.id, True)

        # Remove equipments to room
        room_db = get_room_by_name(session, "A102")
        equipment_ids = []
        equipment_ids.append(get_equipment_by_name(session, "Computer1").id)
        equipment_ids.append(get_equipment_by_name(session, "Computer2").id)
        equipment_ids.append(get_equipment_by_name(session, "Computer3").id)
        room_db = remove_equipments_from_classroom(
            session, room_db.id, equipment_ids, True
        )
        print(room_db)


if __name__ == "__main__":
    test()
