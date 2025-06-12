from app.models.registration import RegistrationBase
from app.schemas.registration_schema import RegistrationCreate, RegistrationStatus
from datetime import date
import uuid


def test_registration_create():
    """
    Test the creation of a Registration instance.
    """

    registration_data = RegistrationCreate(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        registration_date="2025-06-06",
        registration_status=RegistrationStatus.pending,
    )
    assert isinstance(registration_data, RegistrationCreate), (
        "registration_data should be an instance of RegistrationCreate"
    )
    assert registration_data.registration_date == "2025-06-06", (
        "Registration date should be '2025-06-06'"
    )
    assert registration_data.registration_status == RegistrationStatus.pending, (
        "Status should be 'Pending'"
    )


def test_registration_instance():
    """
    Test the creation of an Registration instance.
    """

    registration_data = RegistrationCreate(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        registration_date="2025-06-06",
        registration_status=RegistrationStatus.pending,
    )
    assert isinstance(registration_data, RegistrationCreate), (
        "registration_data should be an instance of RegistrationCreate"
    )
    assert registration_data.registration_date == "2025-06-06", (
        "Registration date should be '2025-06-06'"
    )
    assert registration_data.registration_status == RegistrationStatus.pending, (
        "Status should be 'Pending'"
    )
