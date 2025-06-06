from pydantic import BaseModel, Field

class ClassroomCreate(BaseModel):
    """
    Rules applied via pydantic for the creation of a classroom in the database.
    The rules are applied by Python before the request to the database is pushed.
    """
    name: str = Field(pattern=r"^[A-Z][0-9]{3}$")
    location: str = Field(..., min_length=2, max_length=50)
    capacity: int | None = Field(default=None, ge=15)


def test():
    room1 = ClassroomCreate(name="toto", location="Building North, 1st floor", capacity=15)
    print(room1)

if __name__ == "__main__":
    test()