from sqlmodel import Field, SQLModel, Column, JSON


class Room(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    capacity: int = Field(ge=1)
    location: str
    equipments: dict = Field(default=None, sa_column=Column(JSON))
    is_active: bool = Field(default=True)


def test():
    room1 = Room(name="A101", capacity=12, location="Building North, 1st floor", equipments={"beamer": 1, "white board": 1})
    print(room1)

if __name__ == "__main__":
    test()