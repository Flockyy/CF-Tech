from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.trainee_schema import TraineeCreate, TraineePublic
from app.crud import trainee_crud
import uuid

router = APIRouter(prefix="/trainees", tags=["trainees"])


@router.post("/", response_model=TraineePublic)
def create_trainee(*, session: SessionDep, trainee_in: TraineeCreate):
    """
    Create a new trainee.

    Args:
        session (SessionDep): The database session dependency.
        trainee_in (TraineeCreate): The trainee creation data.

    Raises:
        HTTPException: If the trainee with this email already exists.
        HTTPException: If the trainee creation fails.

    Returns:
        TraineePublic: The created trainee data.
    """
    trainee = trainee_crud.get_trainee_by_email(session=session, email=trainee_in.email)
    if trainee:
        raise HTTPException(
            status_code=400,
            detail="The trainee with this email already exists in the system.",
        )

    trainee = trainee_crud.create_trainee(session=session, trainee=trainee_in)

    return trainee


@router.get("/{trainee_id}", response_model=TraineePublic)
def get_trainee(*, session: SessionDep, trainee_id: uuid.UUID):
    """
    Get a trainee by ID.

    Args:
        session (SessionDep): The database session dependency.
        trainee_id (uuid.UUID): The ID of the trainee to retrieve.

    Raises:
        HTTPException: If the trainee is not found.
        HTTPException: If the trainee retrieval fails.
        HTTPException: If the trainee is inactive.

    Returns:
        TraineePublic: The retrieved trainee data.
    """

    trainee = trainee_crud.get_trainee(session=session, trainee_id=trainee_id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Trainee not found")

    return trainee


@router.put("/{trainee_id}", response_model=TraineePublic)
def update_trainee(
    *, session: SessionDep, trainee_id: uuid.UUID, trainee_in: TraineeCreate
):
    """
    Update a trainee by ID.

    Args:
        session (SessionDep): The database session dependency.
        trainee_id (uuid.UUID): The ID of the trainee to update.
        trainee_in (TraineeCreate): The trainee update data.

    Raises:
        HTTPException: If the trainee is not found.
        HTTPException: If the trainee update fails.

    Returns:
        TraineePublic: The updated trainee data.
    """

    trainee = trainee_crud.get_trainee(session=session, trainee_id=trainee_id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Trainee not found")

    updated_trainee = trainee_crud.update_trainee(
        session=session, trainee_id=trainee_id, trainee_update=trainee_in
    )

    return updated_trainee


@router.delete("/{trainee_id}", response_model=dict)
def delete_trainee(*, session: SessionDep, trainee_id: uuid.UUID):
    """
    Delete a trainee by ID.

    Args:
        session (SessionDep): The database session dependency.
        trainee_id (uuid.UUID): The ID of the trainee to delete.

    Raises:
        HTTPException: If the trainee is not found.

    Returns:
        dict: A success message.
    """
    trainee = trainee_crud.get_trainee(session=session, trainee_id=trainee_id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Trainee not found")

    trainee_crud.delete_trainee(session=session, trainee_id=trainee_id)

    return {"message": "Trainee deleted successfully."}


@router.get("/", response_model=list[TraineePublic])
def list_trainees(*, session: SessionDep):
    """
    List all trainees.

    Args:
        session (SessionDep): The database session dependency.

    Returns:
        list[TraineePublic]: The list of all trainees.
    """

    trainees = trainee_crud.get_all_trainees(session=session)
    return trainees
