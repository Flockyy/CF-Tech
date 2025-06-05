from sqlmodel import Field, SQLModel


class Equipment(SQLModel, table=True):
    """
    Equipment model to describe an equipment that can be link
    to a room of the training center via the RoomEquipmentLink table.
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    # Optional
    serial_number: str | None = Field(default=None)


def test():
    equipment1 = Equipment(name="Table")
    print(equipment1)
    equipment2 = Equipment(name="Computer", serial_number="enhfc5295aeg")
    print(equipment2)

if __name__ == "__main__":
    test()