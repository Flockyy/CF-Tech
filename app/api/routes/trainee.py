from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.trainee_schema import TraineeCreate, TraineePublic
from app.crud import trainee_crud

router = APIRouter(prefix="/trainees", tags=["trainees"])


@router.post("/", response_model=TraineePublic)
def create_trainee(*, session: SessionDep, trainee_in: TraineeCreate):
    """
    Create new trainee.
    """
    trainee = trainee_crud.get_trainee_by_email(session=session, email=trainee_in.email)
    if trainee:
        raise HTTPException(
            status_code=400,
            detail="The trainee with this email already exists in the system.",
        )

    trainee = trainee_crud.create_trainee(session=session, trainee_create=trainee_in)

    return trainee


@router.get("/{trainee_id}", response_model=TraineePublic)
def get_trainee(*, session: SessionDep, trainee_id: str):
    """
    Get a trainee by ID.
    """
    trainee = trainee_crud.get_trainee(session=session, trainee_id=trainee_id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Trainee not found")

    return trainee


@router.put("/{trainee_id}", response_model=TraineePublic)
def update_trainee(*, session: SessionDep, trainee_id: str, trainee_in: TraineeCreate):
    """
    Update a trainee by ID.
    """
    trainee = trainee_crud.get_trainee(session=session, trainee_id=trainee_id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Trainee not found")

    updated_trainee = trainee_crud.update_trainee(
        session=session, trainee_id=trainee_id, trainee_update=trainee_in
    )

    return updated_trainee


@router.delete("/{trainee_id}", response_model=dict)
def delete_trainee(*, session: SessionDep, trainee_id: str):
    """
    Delete a trainee by ID.
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
    """
    trainees = trainee_crud.get_all_trainees(session=session)
    return trainees
