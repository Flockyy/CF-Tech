from sqlmodel import Field, SQLModel, Relationship, create_engine
from app.models.room_equipment_link import RoomEquipmentLink
from app.models.equipment import Equipment


class Room(SQLModel, table=True):
    """
    Room model to describe each room in the training center.
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    capacity: int = Field(ge=1)
    location: str = Field(schema_extra={"example": "Building North, 1st floor"})
    is_active: bool = Field(default=True)

    equipments: list[Equipment] = Relationship(back_populates="rooms", link_model=RoomEquipmentLink)


def test():
    room1 = Room(name="A101", capacity=12, location="Building North, 1st floor")
    print(room1)


if __name__ == "__main__":
    test()