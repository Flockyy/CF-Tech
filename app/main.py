import os,sys
sys.path.append(os.getcwd())
from sqlmodel import create_engine, SQLModel
# import app.models.room
# import app.models.equipment
from app.models import (
    room,
    equipment,
    room_equipment_link
)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)