from app.models.admin import AdminBase
from app.schemas.admin_schema import AdminCreate, AdminUpdate
from datetime import datetime


def test_admin_create():
    """
    Test the creation of an Admin instance.
    """

    admin_data = AdminCreate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        admin_level=1,
        promotion_date=datetime.now(),
    )

    assert isinstance(
        admin_data, AdminCreate
    ), "admin_data should be an instance of AdminCreate"
    assert admin_data.first_name == "John", "First name should be 'John'"
    assert admin_data.last_name == "Doe", "Last name should be 'Doe'"
    assert (
        admin_data.email == "john.doe@example.com"
    ), "Email should be 'john.doe@example.com'"
    assert admin_data.admin_level == 1, "Admin level should be 1"
    assert admin_data.promotion_date is not None, "Promotion date should not be None"


def test_admin_update():
    """
    Test the update of an Admin instance.
    """

    admin_data = AdminUpdate(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        admin_level=2,
        promotion_date=datetime.now(),
    )

    assert isinstance(
        admin_data, AdminUpdate
    ), "admin_data should be an instance of AdminUpdate"
    assert admin_data.first_name == "Jane", "First name should be 'Jane'"
    assert admin_data.last_name == "Doe", "Last name should be 'Doe'"
    assert (
        admin_data.email == "jane.doe@example.com"
    ), "Email should be 'jane.doe@example.com'"
    assert admin_data.admin_level == 2, "Admin level should be 2"
    assert admin_data.promotion_date is not None, "Promotion date should not be None"


def test_admin_instance():
    """
    Test the creation of an Admin instance.
    """

    admin_data = AdminBase(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        admin_level=1,
        promotion_date=datetime.now(),
    )

    assert isinstance(
        admin_data, AdminBase
    ), "admin_data should be an instance of Admin"
    assert admin_data.first_name == "Alice", "First name should be 'Alice'"
    assert admin_data.last_name == "Smith", "Last name should be 'Smith'"
    assert (
        admin_data.email == "alice.smith@example.com"
    ), "Email should be 'alice.smith@example.com'"
    assert admin_data.admin_level == 1, "Admin level should be 1"
    assert admin_data.promotion_date is not None, "Promotion date should not be None"
