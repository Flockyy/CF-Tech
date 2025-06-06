from app.models.trainee import Trainee
from app.schemas.trainee_schema import TraineeCreate, TraineeUpdate
from datetime import datetime
import uuid


def test_trainee_create():
    """
    Test the creation of a Trainee instance.
    """

    trainee_data = TraineeCreate(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        date_of_birth=datetime(2009, 1, 1),
        study_level="Bac +3",
        phone_number="+33123456789",
    )
    assert isinstance(trainee_data, TraineeCreate), (
        "trainee_data should be an instance of TraineeCreate"
    )
    assert trainee_data.first_name == "Alice", "First name should be 'Alice'"
    assert trainee_data.last_name == "Smith", "Last name should be 'Smith'"
    assert trainee_data.email == "alice.smith@example.com", (
        "Email should be 'alice.smith@example.com'"
    )
    assert trainee_data.date_of_birth == datetime(2009, 1, 1), (
        "Date of birth should be a valid date"
    )
    assert trainee_data.study_level == "Bac +3", "Study level should be 'Bac +3'"
    assert trainee_data.phone_number == "+33123456789", (
        "Phone number should be '+33123456789'"
    )


def test_trainee_update():
    """
    Test the update of a Trainee instance.
    """

    trainee_data = TraineeUpdate(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        date_of_birth=datetime(2009, 1, 1),
        study_level="Bac +3",
        phone_number="+33123456789",
    )
    assert isinstance(trainee_data, TraineeUpdate), (
        "trainee_data should be an instance of TraineeUpdate"
    )
    assert trainee_data.first_name == "Alice", "First name should be 'Alice'"
    assert trainee_data.last_name == "Smith", "Last name should be 'Smith'"
    assert trainee_data.email == "alice.smith@example.com", (
        "Email should be 'alice.smith@example.com'"
    )
    assert trainee_data.date_of_birth == datetime(2009, 1, 1), (
        "Date of birth should be a valid date"
    )
    assert trainee_data.study_level == "Bac +3", "Study level should be 'Bac +3'"
    assert trainee_data.phone_number == "+33123456789", (
        "Phone number should be '+33123456789'"
    )


def test_trainee_instance():
    """
    Test the creation of a Trainee instance.
    """

    trainee_instance = Trainee(
        id=uuid.uuid4(),
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        date_of_birth=datetime(2009, 1, 1),
        study_level="Bac +3",
        phone_number="+33123456789",
    )
    assert isinstance(trainee_instance, Trainee), (
        "trainee_instance should be an instance of Trainee"
    )
    assert trainee_instance.first_name == "Alice", "First name should be 'Alice'"
    assert trainee_instance.last_name == "Smith", "Last name should be 'Smith'"
    assert trainee_instance.email == "alice.smith@example.com", (
        "Email should be 'alice.smith@example.com'"
    )
    assert trainee_instance.date_of_birth == datetime(2009, 1, 1), (
        "Date of birth should be a valid date"
    )
    assert trainee_instance.study_level == "Bac +3", "Study level should be 'Bac +3'"
    assert trainee_instance.phone_number == "+33123456789", (
        "Phone number should be '+33123456789'"
    )
