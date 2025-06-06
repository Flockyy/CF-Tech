from app.models.duty import Duty
from app.schemas.duties_schema import DutyCreate, DutyUpdate
from datetime import datetime
import uuid


def test_duty_create():
    """
    Test the creation of a Duty instance.
    """

    duty_data = DutyCreate(staff_id=uuid.uuid4(), description="Test Duty")
    assert isinstance(duty_data, DutyCreate), (
        "duty_data should be an instance of DutyCreate"
    )
    assert duty_data.description == "Test Duty", "Description should be 'Test Duty'"


def test_duty_update():
    """
    Test the update of a Duty instance.
    """

    duty_data = DutyUpdate(description="Updated Duty")
    assert isinstance(duty_data, DutyUpdate), (
        "duty_data should be an instance of DutyUpdate"
    )
    assert duty_data.description == "Updated Duty", (
        "Description should be 'Updated Duty'"
    )


def test_duty_instance():
    """
    Test the creation of a Duty instance.
    """

    duty_instance = Duty(
        id=uuid.uuid4(),
        staff_id=uuid.uuid4(),
        description="Test Duty Instance",
        created_at=datetime.now(),
    )
    assert isinstance(duty_instance, Duty), (
        "duty_instance should be an instance of Duty"
    )
    assert duty_instance.description == "Test Duty Instance", (
        "Description should be 'Test Duty Instance'"
    )
    assert duty_instance.created_at is not None, "Created at should not be None"
    assert isinstance(duty_instance.id, uuid.UUID), "ID should be a UUID instance"
