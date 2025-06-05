from pydantic import model_validator
from typing_extensions import Self
from sqlmodel import Field, SQLModel, Session, Enum, create_engine
import enum
from datetime import date


class TrainingStatus(str, enum.Enum):
    registered_for_training = "REGISTERED"
    training = "TRAINING"
    trained = "TRAINED"


class Registration(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # TODO: add the foreign key constraint
    trainee_id: int | None = Field(default=None)
    # TODO: add the foreign key constraint
    session_id: int | None = Field(default=None)
    registration_date: date = Field(default=date.today())
    # TODO: check if the registration_status is in TrainingStatus
    registration_status: str = Field(
        default=TrainingStatus.registered_for_training, sa_column=TrainingStatus
    )


# def create_registrations():
#     reg1 = Registration(
#         id=None,
#         trainee_id=1,
#         session_id=1,
#         registration_date=date.today(),
#         registration_status=TrainingStatus.registered_for_training,
#     )
#     reg2 = Registration(
#         id=None,
#         trainee_id=2,
#         session_id=1,
#         registration_date=date.today(),
#         registration_status=TrainingStatus.training,
#     )
#     reg3 = Registration(
#         id=None,
#         trainee_id="es",
#         session_id="de",
#         registration_date=date.today(),
#         registration_status="status",
#     )
#     print(f"{reg1.__repr__}")
#     print(f"{reg2.__repr__}")
#     print(f"{reg3.__repr__}")

#     with Session(engine) as session:
#         session.add(reg1)
#         session.commit()

#         if not reg1.id:
#             print(f"problem creating reg1")

#         session.add(reg2)
#         session.commit()
#         if not reg2.id:
#             print(f"problem creating reg2")

#         session.add(reg3)
#         session.commit()
#         if not reg3.id:
#             print(f"problem creating reg3")


# sqlite_f_n = "ceb.db"
# sqlite_url = f"sqlite:///{sqlite_f_n}"

# engine = create_engine(sqlite_url, echo=True)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


# if __name__ == "__main__":
#     create_db_and_tables()
#     create_registrations()
