from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
import uuid


def test_user_create():
    """
    Test the creation of a User instance.
    """

    user_data = UserCreate(
        first_name="Alice", last_name="Smith", email="alice.smith@example.com"
    )
    assert isinstance(user_data, UserCreate), (
        "user_data should be an instance of UserCreate"
    )
    assert user_data.first_name == "Alice", "First name should be 'Alice'"
    assert user_data.last_name == "Smith", "Last name should be 'Smith'"
    assert user_data.email == "alice.smith@example.com", (
        "Email should be 'alice.smith@example.com'"
    )


def test_user_update():
    """
    Test the update of a User instance.
    """

    user_data = UserUpdate(
        first_name="Alice", last_name="Smith", email="alice.smith@example.com"
    )
    assert isinstance(user_data, UserUpdate), (
        "user_data should be an instance of UserUpdate"
    )
    assert user_data.first_name == "Alice", "First name should be 'Alice'"
    assert user_data.last_name == "Smith", "Last name should be 'Smith'"
    assert user_data.email == "alice.smith@example.com", (
        "Email should be 'alice.smith@example.com'"
    )


def test_user_instance():
    """
    Test the creation of a User instance.
    """

    user_instance = User(
        id=uuid.uuid4(),
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
    )
    assert isinstance(user_instance, User), (
        "user_instance should be an instance of User"
    )
    assert user_instance.first_name == "Alice", "First name should be 'Alice'"
    assert user_instance.last_name == "Smith", "Last name should be 'Smith'"
    assert user_instance.email == "alice.smith@example.com", (
        "Email should be 'alice.smith@example.com'"
    )
