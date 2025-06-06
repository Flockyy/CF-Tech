import os, sys

sys.path.append(os.getcwd())
from sqlmodel import Session, create_engine, SQLModel
from app.models.room import RoomBase
from app.schemas.room_schema import ClassroomCreate


def create_classroom(db: Session, room_in: ClassroomCreate) -> RoomBase:
    """Insert an entity in the table Room of the database connected as 'db',
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


def main():
    """Test the module functions"""

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    room = ClassroomCreate(
        name="A101", capacity=18, location="Building North, 1st floor"
    )
    print(room)

    with Session(engine) as session:
        room_db = create_classroom(session, room)


if __name__ == "__main__":
    main()
