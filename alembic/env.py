import os, sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import sqlalchemy.dialects

from alembic import context

from dotenv import load_dotenv
from sqlmodel import SQLModel

from app.models.admin import Admin
from app.models.staff import Staff
from app.models.trainee import Trainee
from app.models.trainer import Trainer
from app.models.attendance import AttendanceBase
from app.models.course import CourseBase
from app.models.duty import Duty
from app.models.registration import RegistrationBase
from app.models.room import RoomBase, EquipmentBase, RoomEquipmentLink


sys.path.insert(
    0, os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
)  # Add project root to sys.path

load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    # url = config.get_main_option(datab_url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        naming_convention=naming_convention,
        render_as_batch=True,
    )

    naming_convention = {
        "ix": "ix_%(table_name)_%(column_0_label)s",  # Added table_name for more uniqueness
        "uq": "uq_%(table_name)_%(column_0_name)s",
        "ck": "ck_%(table_name)_%(constraint_name)s",  # Used constraint_name for check constraints
        "fk": "fk_%(table_name)_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)",
    }

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    naming_convention = {
        "ix": "ix_%(table_name)_%(column_0_label)s",  # Added table_name for more uniqueness
        "uq": "uq_%(table_name)_%(column_0_name)s",
        "ck": "ck_%(table_name)_%(constraint_name)s",  # Used constraint_name for check constraints
        "fk": "fk_%(table_name)_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)",
    }

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            naming_convention=naming_convention,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
