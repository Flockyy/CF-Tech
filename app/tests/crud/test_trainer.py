from app.models.trainer import TrainerBase
from app.schemas.trainer_schema import TrainerCreate, TrainerUpdate
import uuid


def test_trainer_create():
    """
    Test the creation of a Trainer instance.
    """

    trainer_data = TrainerCreate(
        first_name="Bob",
        last_name="Johnson",
        email="bob.johnson@example.com",
        specialty="Web Development",
        hourly_rate=50.0,
        bio="Experienced web developer specializing in frontend technologies.",
    )
    assert isinstance(
        trainer_data, TrainerCreate
    ), "trainer_data should be an instance of TrainerCreate"
    assert trainer_data.first_name == "Bob", "First name should be 'Bob'"
    assert trainer_data.last_name == "Johnson", "Last name should be 'Johnson'"
    assert (
        trainer_data.email == "bob.johnson@example.com"
    ), "Email should be 'bob.johnson@example.com'"
    assert (
        trainer_data.specialty == "Web Development"
    ), "Specialty should be 'Web Development'"
    assert trainer_data.hourly_rate == 50.0, "Hourly rate should be 50.0"
    assert (
        trainer_data.bio
        == "Experienced web developer specializing in frontend technologies."
    ), "Bio should match"


def test_trainer_update():
    """
    Test the update of a Trainer instance.
    """

    trainer_data = TrainerUpdate(
        first_name="Bob",
        last_name="Johnson",
        email="bob.johnson@example.com",
        specialty="Web Development",
        hourly_rate=50.0,
        bio="Experienced web developer specializing in frontend technologies.",
    )
    assert isinstance(
        trainer_data, TrainerUpdate
    ), "trainer_data should be an instance of TrainerUpdate"
    assert trainer_data.first_name == "Bob", "First name should be 'Bob'"
    assert trainer_data.last_name == "Johnson", "Last name should be 'Johnson'"
    assert (
        trainer_data.email == "bob.johnson@example.com"
    ), "Email should be 'bob.johnson@example.com'"
    assert (
        trainer_data.specialty == "Web Development"
    ), "Specialty should be 'Web Development'"
    assert trainer_data.hourly_rate == 50.0, "Hourly rate should be 50.0"
    assert (
        trainer_data.bio
        == "Experienced web developer specializing in frontend technologies."
    ), "Bio should match"


def test_trainer_instance():
    """
    Test the creation of a Trainer instance.
    """

    trainer_instance = TrainerBase(
        id=uuid.uuid4(),
        first_name="Bob",
        last_name="Johnson",
        email="bob.johnson@example.com",
        specialty="Web Development",
        hourly_rate=50.0,
        bio="Experienced web developer specializing in frontend technologies.",
    )
    assert isinstance(
        trainer_instance, TrainerBase
    ), "trainer_instance should be an instance of Trainer"
    assert trainer_instance.first_name == "Bob", "First name should be 'Bob'"
    assert trainer_instance.last_name == "Johnson", "Last name should be 'Johnson'"
    assert (
        trainer_instance.email == "bob.johnson@example.com"
    ), "Email should be 'bob.johnson@example.com'"
    assert (
        trainer_instance.specialty == "Web Development"
    ), "Specialty should be 'Web Development'"
    assert trainer_instance.hourly_rate == 50.0, "Hourly rate should be 50.0"
    assert (
        trainer_instance.bio
        == "Experienced web developer specializing in frontend technologies."
    ), "Bio should match"
