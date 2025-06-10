from app.models.attendance import AttendanceBase
from app.schemas.attendance_schema import AttendanceCreate
from datetime import date
import uuid


def test_attendance_create():
    """
    Test the creation of an Attendance instance.
    """

    attendance_data = AttendanceCreate(
        trainee_id=uuid.uuid4(), course_id=uuid.uuid4(), date_course=date.today()
    )
    assert isinstance(
        attendance_data, AttendanceCreate
    ), "attendance_data should be an instance of AttendanceCreate"
    assert (
        attendance_data.date_course == date.today()
    ), f"Date of attendance should be {date.today()}"
    assert attendance_data.am == False, "A.M attendance should be False"
    assert attendance_data.pm == False, "P.M attendance should be False"


def test_attendance_instance():
    """
    Test the creation of an Attendance instance.
    """

    attendance_instance = AttendanceBase(
        trainee_id=uuid.uuid4(),
        course_id=uuid.uuid4(),
        date_course=date.today(),
    )
    assert isinstance(
        attendance_instance, AttendanceBase
    ), "attendance_instance should be an instance of AttendanceBase"
    assert (
        attendance_instance.date_course == date.today()
    ), f"Date of attendance should be {date.today()}"
    assert attendance_instance.am == False, "A.M attendance should be False"
    assert attendance_instance.pm == False, "P.M attendance should be False"
