from app.models.course import CourseBase
from app.schemas.course_schema import CourseCreate, CourseStatus
from datetime import date
import uuid


def test_course_create():
    """
    Test the creation of a Course instance.
    """

    course_data = CourseCreate(
        title="Data Engineer",
        description="First data eng course",
        date_start="2025-06-30",
        date_end="2025-08-29",
        room_id=uuid.uuid4(),
        trainer_id=uuid.uuid4(),
        max_capacity=13,
        prerequisite="sql, python",
    )
    assert isinstance(course_data, CourseCreate), (
        "course_data should be an instance of CourseCreate"
    )
    assert course_data.title == "Data Engineer", "Title should be 'Data Engineer'"
    assert course_data.description == "First data eng course", (
        "Description should be 'First data eng course'"
    )
    assert course_data.date_start == "2025-06-30", (
        "Starting date should be '2025-06-30'"
    )
    assert course_data.date_end == "2025-08-29", "Ending date should be '2025-08-29'"
    assert course_data.max_capacity == 13, "Max capacity should be 13"
    assert course_data.prerequisite == "sql, python", (
        "Prerequisite should be 'sql, python'"
    )


def test_course_instance():
    """
    Test the creation of an Course instance.
    """

    course_instance = CourseBase(
        title="Data Engineer",
        description="First data eng course",
        date_start="2025-06-30",
        date_end="2025-08-29",
        room_id=uuid.uuid4(),
        trainer_id=uuid.uuid4(),
        max_capacity=13,
        prerequisite="sql, python",
    )
    assert isinstance(course_instance, CourseCreate), (
        "course_data should be an instance of CourseCreate"
    )
    assert course_instance.title == "Data Engineer", "Title should be 'Data Engineer'"
    assert course_instance.description == "First data eng course", (
        "Description should be 'First data eng course'"
    )
    assert course_instance.date_start == "2025-06-30", (
        "Starting date should be '2025-06-30'"
    )
    assert course_instance.date_end == "2025-08-29", (
        "Ending date should be '2025-08-29'"
    )
    assert course_instance.max_capacity == 13, "Max capacity should be 13"
    assert course_instance.prerequisite == "sql, python", (
        "Prerequisite should be 'sql, python'"
    )
