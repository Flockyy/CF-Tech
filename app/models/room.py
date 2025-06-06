import uuid

from sqlmodel import Field, SQLModel#, Relationship, create_engine
# from app.models.room_equipment_link import RoomEquipmentLink
# from app.models.equipment import Equipment


class RoomBase(SQLModel, table=True):
    """
    Room model to describe each entry of room in the database.
    The rules applied here are directly the rule applied to the SQL database.
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True)
    location: str = Field(..., min_length=2, max_length=50)
    capacity: int | None = Field(default=None, ge=1)
    is_active: bool = Field(default=True)

#    equipments: list[Equipment] | None = Relationship(back_populates="rooms", link_model=RoomEquipmentLink)


def test():
    room1 = RoomBase(name="A101", capacity=12, location="Building North, 1st floor")
    print(room1)


if __name__ == "__main__":
    test()