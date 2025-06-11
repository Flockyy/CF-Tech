import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine
from app.models.admin import AdminBase
from app.models.user import UserBase
from app.models.trainer import TrainerBase
from app.models.trainee import TraineeBase
from app.models.staff import StaffBase, DutyBase, DutyStaffLink
from app.models.attendance import AttendanceBase
from app.models.course import CourseBase
from app.models.registration import RegistrationBase
from app.models.room import RoomBase, EquipmentBase, RoomEquipmentLink
from app.core.config import settings

engine = create_engine(str(settings.SQLITE_DB), echo=True)

load_dotenv()


def init_db():
    # print("Creating tables...")
    # SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        from sqlmodel import select
        from app.schemas.admin_schema import AdminCreate
        from app.schemas.trainee_schema import TraineeCreate
        from app.schemas.trainer_schema import TrainerCreate
        from app.schemas.staff_schema import StaffCreate
        from app.schemas.duty_schema import DutyCreate
        from app.schemas.room_schema import (
            ClassroomCreate,
            EquipmentCreate,
            RegisteredEquipmentCreate,
            InRoomRegisteredEquipmentCreate,
            InRoomEquipmentCreate,
        )
        from app.schemas.course_schema import CourseCreate
        from app.schemas.registration_schema import RegistrationCreate, RegistrationStatus
        from app.crud.admin_crud import create_admin
        from app.crud.trainee_crud import create_trainee, get_all_trainees
        from app.crud.trainer_crud import create_trainer, get_all_trainers
        from app.crud.staff_crud import create_staff
        from app.crud.duty_crud import create_duty
        from app.crud.room_crud import create_classroom, create_equipment, get_all_rooms
        from app.crud.course_crud import create_course, get_all_courses
        from app.crud.registration_crud import create_registration
        from app.core.config import settings
        from datetime import datetime, timedelta, timezone
        import random
        from faker import Faker

        fake = Faker()

        print(SQLModel.metadata.tables.keys())

        # Create admin
        admin = session.exec(
            select(AdminBase).where(AdminBase.email == settings.FIRST_SUPERUSER)
        ).first()

        if not admin:
            admin_in = AdminCreate(
                first_name=os.getenv("DB_ADMIN_FIRSTNAME"),
                last_name=os.getenv("DB_ADMIN_LASTNAME"),
                email=settings.FIRST_SUPERUSER,
                role="admin",
                admin_level=2,
            )
            create_admin(session=session, admin=admin_in)
            print("Default admin created.")

        # Create 31 Trainees
        trainee1 = TraineeCreate(
            first_name="Cesar",
            last_name="Gattano",
            email="cesar.gattano@gmail.com",
            date_of_birth=datetime(
                year=1995,
                month=7,
                day=25,
                hour=0,
                minute=0,
                second=0,
                tzinfo=timezone.utc,
            ),
            study_level="PHD",
            phone_number="+33 6 58 59 60 61",
            registration_date=datetime(
                year=2025,
                month=5,
                day=20,
                hour=0,
                minute=0,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        create_trainee(session=session, trainee=trainee1)
        print("One trainee created.")

        study_levels = ["High School", "Bachelor", "Master", "PHD"]
        base_date = datetime(year=2025, month=5, day=20, tzinfo=timezone.utc)

        for _ in range(30):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = first_name + "." + last_name + "@example.org"
            role = "user"
            date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=55)
            study_level = random.choice(study_levels)
            phone_number = (
                "+33 "
                + str(random.randint(1, 9))
                + " "
                + str(random.randint(1, 9))
                + str(random.randint(1, 9))
                + " "
                + str(random.randint(1, 9))
                + str(random.randint(1, 9))
                + " "
                + str(random.randint(1, 9))
                + str(random.randint(1, 9))
                + " "
                + str(random.randint(1, 9))
                + str(random.randint(1, 9))
            )
            registration_date = base_date + timedelta(days=random.randint(0, 10))

            trainee = TraineeCreate(
                first_name=first_name,
                last_name=last_name,
                email=email,
                role=role,
                date_of_birth=datetime.combine(
                    date_of_birth, datetime.min.time(), tzinfo=timezone.utc
                ),
                study_level=study_level,
                phone_number=phone_number,
                registration_date=registration_date,
            )
            create_trainee(session=session, trainee=trainee)
            print("One trainee created.")

        # Create 6 Trainers
        trainer1 = TrainerCreate(
            first_name="Jean",
            last_name="Sérien",
            email="jean.serien@gmail.com",
            role="user",
            specialty="Pot-au-feu",
            hourly_rate=40.21,
            bio="Rien du tout",
        )

        create_trainer(session, trainer1)
        print("One trainer created.")

        specialties = [
            "Data Engineering",
            "Machine Learning",
            "Cybersecurity",
            "DevOps",
            "Cloud Computing",
            "Web Development",
            "Agile Coaching",
            "AI Ethics",
            "Software Architecture",
        ]

        for _ in range(5):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = first_name + "." + last_name + "@example.org"
            specialty = random.choice(specialties)
            hourly_rate = round(random.uniform(35, 100), 2)
            bio = fake.sentence(nb_words=10)

            trainer = TrainerCreate(
                first_name=first_name,
                last_name=last_name,
                email=email,
                role="user",
                specialty=specialty,
                hourly_rate=hourly_rate,
                bio=bio,
            )

            create_trainer(session, trainer)
            print("One trainer created.")

        # Create 10 Staff
        positions = [
            "Community manager",
            "Developer",
            "Manager",
            "Accounting officer",
            "Informatician",
            "Secretarian",
        ]

        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = first_name + "." + last_name + "@example.org"
            position = random.choice(positions)
            hourly_rate = round(random.uniform(35, 100), 2)
            bio = fake.sentence(nb_words=10)

            staff = StaffCreate(
                first_name=first_name,
                last_name=last_name,
                email=email,
                role="user",
                position=position,
            )

            create_staff(session, staff)
            print("One staff created.")

        # Create 8 Duties
        titles = [
            "Accountability",
            "Company contact",
            "Trainee contact",
            "Trainer contact",
            "Social network",
            "Plan courses",
            "Manage equipments",
            "Direction feedback",
        ]

        for i in range(8):
            title = titles[i]
            description = fake.sentence(nb_words=20)

            duty = DutyCreate(
                title=title,
                description=description,
            )

            create_duty(session, duty)
            print("One duty created.")

        # Create 20 rooms
        rooms = []

        for i in range(10):
            name = "A" + str(i // 3) + "0" + str(i % 3 + 1)
            capacity = random.randint(15, 50)
            location = "Building A, floor " + str(i // 3)

            room = ClassroomCreate(name=name, capacity=capacity, location=location)

            room_db = create_classroom(room)
            rooms.append(room_db)
            print("One classroom created.")

            name = "B" + str(i // 3) + "0" + str(i % 3 + 1)
            capacity = random.randint(15, 50)
            location = "Building B, floor " + str(i // 3)

            room = ClassroomCreate(name=name, capacity=capacity, location=location)

            room_db = create_classroom(room)
            rooms.append(room_db)
            print("One classroom created.")

        # Create equipments
        equipment = EquipmentCreate(name="Welcome desk")
        create_equipment(equipment, True, session)
        print("One equipment created.")

        for i in range(10):
            equipment = RegisteredEquipmentCreate(
                name="Computer" + str(i), serial_number=fake.pystr(10, 10)
            )
            create_equipment(equipment, True, session)
            print("One equipment created.")

        equipment = InRoomEquipmentCreate(name="White board", rooms=rooms)
        create_equipment(equipment, True, session)
        print("One equipment created.")

        equipment = InRoomEquipmentCreate(name="Chair", rooms=rooms)
        create_equipment(equipment, True, session)
        print("One equipment created.")

        equipment = InRoomEquipmentCreate(name="Table", rooms=rooms)
        create_equipment(equipment, True, session)
        print("One equipment created.")

        rooms_subset = random.sample(rooms, 9)
        for i in range(9):
            equipment = InRoomRegisteredEquipmentCreate(
                name="Beamer" + str(i), serial_number=fake.pystr(10, 10), rooms=[rooms_subset[i]]
            )
            create_equipment(equipment, True, session)
            print("One equipment created.")

        equipment = InRoomEquipmentCreate(name="TV", rooms=random.sample(rooms, 8))
        create_equipment(equipment, True, session)
        print("One equipment created.")

        titles = [
            "Dev Ia", "Data eng", "Cybersecurity", "Tech Infra",
            "Apple Pie", "Cobol", "No Code", "Data science"
        ]
        base_date = datetime(year=2025, month=5, day=20, tzinfo=timezone.utc)
        trainers = get_all_trainers(session)
        rooms = get_all_rooms(session)

        # Create 8 courses
        for i in range(8):
            title = titles[i]
            description = fake.sentence(nb_words=20)
            date_start = base_date + timedelta(days=random.randint(-30, 30))
            date_end = date_start + timedelta(days=random.randint(100, 500))
            room = random.choice(rooms)
            trainer = random.choice(trainers)
            prerequisite = fake.sentence(nb_words=30)
            
            course = CourseCreate(
                title = title,
                description = description,
                date_start = date_start,
                date_end = date_end,
                room_id = room.id,
                trainer_id = trainer.id,
                max_capacity = room.capacity,
                prerequisite = prerequisite,
            )
            create_course(session, course)
            print("One course created.")


        # Create registrations
        trainees = get_all_trainees(session)
        courses = get_all_courses(session)
        base_date = datetime(year=2025, month=5, day=20, tzinfo=timezone.utc)

        for trainee in trainees:
            course = random.choice(courses)
            registration_date = base_date + timedelta(days=random.randint(-100, -50))

            registration = RegistrationCreate(
                trainee_id=trainee.id,
                course_id=course.id,
                registration_date=registration_date,
                registration_status=random.choice([RegistrationStatus.registered, RegistrationStatus.pending]),
            )

            create_registration(session, registration)
            print("One registration created.")
