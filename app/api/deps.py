from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.core.db import engine


def get_db() -> Generator[Session, None, None]:
    """Get a database session.

    Yields:
        Generator[Session, None, None]: A database session.
    """
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
