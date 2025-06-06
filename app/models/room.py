import uuid

from sqlmodel import Field, SQLModel, Relationship

class RoomBase(SQLModel, table=True):
    """
    Room model to describe each entry of room in the database.
    The rules applied here are directly the rule applied to the SQL database.
    """

    __tablename__ = "rooms"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., unique=True, min_length=2, max_length=50)
    location: str = Field(..., min_length=2, max_length=50)
    capacity: int | None = Field(default=None, ge=1)
    is_active: bool = Field(default=True)

    equipments: list["EquipmentBase"] = Relationship(back_populates="room")


class EquipmentBase(SQLModel, table=True):
    """
    Equipment model to describe an equipment that can be link
    to a room of the training center.
    The rules applied here are directly the rule applied to the SQL database.
    """

    __tablename__ = "equipments"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., unique=True, min_length=2, max_length=50)
    serial_number: str | None = Field(default=None, unique=True, min_length=2, max_length=50)

    id_room: uuid.UUID | None = Field(default=None, foreign_key="rooms.id")
    room: RoomBase | None = Relationship(back_populates="equipments")



def test():
    room1 = RoomBase(name="A101", capacity=12, location="Building North, 1st floor")
    print(room1)
    equipment1 = EquipmentBase(name="Welcome desk")
    print(equipment1)
    equipment2 = EquipmentBase(name="White board", id_room=room1.id)
    print(equipment2)


if __name__ == "__main__":
    test()
