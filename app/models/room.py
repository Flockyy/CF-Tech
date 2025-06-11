import uuid

from sqlmodel import Field, SQLModel, Relationship


class RoomEquipmentLink(SQLModel, table=True):
    """
    Model for linking a room and an equipment (they are described below).
    The rules applied here are directly the rule applied to the SQL database.
    """

    room_id: uuid.UUID = Field(default=None, foreign_key="rooms.id", primary_key=True)
    equipment_id: uuid.UUID = Field(
        default=None, foreign_key="equipments.id", primary_key=True
    )
    quantity: int = Field(default=1, ge=1)


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
    color: str = Field(default="white", sa_column_kwargs={"server_default": "white"})

    equipments: list["EquipmentBase"] = Relationship(
        back_populates="rooms", link_model=RoomEquipmentLink
    )


class EquipmentBase(SQLModel, table=True):
    """
    Equipment model to describe an equipment that can be link
    to a room of the training center.
    The rules applied here are directly the rule applied to the SQL database.
    """

    __tablename__ = "equipments"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., unique=True, min_length=2, max_length=50)
    serial_number: str | None = Field(
        default=None, unique=True, min_length=2, max_length=50
    )

    rooms: list[RoomBase] = Relationship(
        back_populates="equipments", link_model=RoomEquipmentLink
    )

def test():
    room1 = RoomBase(name="A101", location="Building North, 1st floor", capacity=12)
    print(room1)
    equipment1 = EquipmentBase(name="Welcome desk")
    print(equipment1)
    equipment2 = EquipmentBase(name="TV", serial_number="fraetrae42064a1et6re4t")
    print(equipment2)
    link1 = RoomEquipmentLink(
        room_id=uuid.uuid4(), equipment_id=uuid.uuid4(), quantity=3
    )
    print(link1)

    room2 = RoomBase(
        name="A102",
        location="Building North, 1st floor",
        capacity=36,
        equipments=[equipment1, equipment2],
    )
    print(room2)
    equipment3 = EquipmentBase(name="White board", rooms=[room1])
    print(equipment3)


if __name__ == "__main__":
    test()
