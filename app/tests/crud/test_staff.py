from app.models.staff import StaffBase
from app.schemas.staff_schema import StaffCreate, StaffUpdate
from datetime import datetime
import uuid


def test_staff_create():
    """
    Test the creation of a Staff instance.
    """

    staff_data = StaffCreate(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        position="Manager",
    )
    assert isinstance(
        staff_data, StaffCreate
    ), "staff_data should be an instance of StaffCreate"
    assert staff_data.first_name == "Alice", "First name should be 'Alice'"
    assert staff_data.last_name == "Smith", "Last name should be 'Smith'"
    assert (
        staff_data.email == "alice.smith@example.com"
    ), "Email should be 'alice.smith@example.com'"
    assert staff_data.position == "Manager", "Position should be 'Manager'"


def test_staff_update():
    """
    Test the update of a Staff instance.
    """

    staff_data = StaffUpdate(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        position="Manager",
    )
    assert isinstance(
        staff_data, StaffUpdate
    ), "staff_data should be an instance of StaffUpdate"
    assert staff_data.first_name == "Alice", "First name should be 'Alice'"
    assert staff_data.last_name == "Smith", "Last name should be 'Smith'"
    assert (
        staff_data.email == "alice.smith@example.com"
    ), "Email should be 'alice.smith@example.com'"
    assert staff_data.position == "Manager", "Position should be 'Manager'"


def test_staff_instance():
    """
    Test the creation of a Staff instance.
    """

    staff_instance = StaffBase(
        id=uuid.uuid4(),
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        position="Manager",
        hire_date=datetime.now(),
    )
    assert isinstance(
        staff_instance, StaffBase
    ), "staff_instance should be an instance of Staff"
    assert staff_instance.first_name == "Alice", "First name should be 'Alice'"
    assert staff_instance.last_name == "Smith", "Last name should be 'Smith'"
    assert (
        staff_instance.email == "alice.smith@example.com"
    ), "Email should be 'alice.smith@example.com'"
    assert staff_instance.position == "Manager", "Position should be 'Manager'"
    assert staff_instance.hire_date is not None, "Hire date should not be None"
    assert isinstance(staff_instance.id, uuid.UUID), "ID should be a UUID instance"
