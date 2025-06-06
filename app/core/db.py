from sqlmodel import SQLModel, Session, create_engine
from app.models.admin import Admin
from app.models.user import User
from app.models.trainer import Trainer
from app.models.trainee import Trainee
from app.models.staff import Staff
from app.models.duty import Duty
from app.core.config import settings

engine = create_engine(str(settings.SQLITE_DB), echo=True)


def init_db():
    print("Creating tables...")
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        from sqlmodel import select
        from app.schemas.admin_schema import AdminCreate
        from app.crud.admin_crud import create_admin
        from app.core.config import settings

        print(SQLModel.metadata.tables.keys())

        admin = session.exec(
            select(Admin).where(Admin.email == settings.FIRST_SUPERUSER)
        ).first()

        if not admin:
            admin_in = AdminCreate(
                first_name="Admin",
                last_name="User",
                email=settings.FIRST_SUPERUSER,
                role="admin",
                admin_level=2,
            )
            create_admin(session=session, admin=admin_in)
            print("Default admin created.")
