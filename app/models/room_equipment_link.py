from sqlmodel import Field, SQLModel


class RoomEquipmentLink(SQLModel, table=True):
    room_id: int | None = Field(default=None, foreign_key="room.id", primary_key=True)
    equipment_id: int | None = Field(default=None, foreign_key="equipment.id", primary_key=True)
    quantity: int = Field(default=1, ge=1)