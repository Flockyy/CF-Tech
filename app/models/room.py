from sqlmodel import Field, SQLModel, create_engine


class Room(SQLModel, table=True):
    """
    Room model to describe each room in the training center.
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    capacity: int = Field(ge=1)
    location: str = Field(schema_extra={"example": "Building North, 1st floor"})
    is_active: bool = Field(default=True)


def test():
    room1 = Room(name="A101", capacity=12, location="Building North, 1st floor")
    print(room1)

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=True)

    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    test()