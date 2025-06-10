from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.schemas.trainer_schema import TrainerCreate, TrainerPublic
from app.crud import trainer_crud

router = APIRouter(prefix="/trainers", tags=["trainers"])


@router.post("/", response_model=TrainerPublic)
def create_trainer(*, session: SessionDep, trainer_in: TrainerCreate):
    """
    Create new trainer.
    """
    trainer = trainer_crud.get_trainer_by_email(session=session, email=trainer_in.email)
    if trainer:
        raise HTTPException(
            status_code=400,
            detail="The trainer with this email already exists in the system.",
        )

    trainer = trainer_crud.create_trainer(session=session, trainer_create=trainer_in)

    return trainer

@router.get("/{trainer_id}", response_model=TrainerPublic)
def get_trainer(*, session: SessionDep, trainer_id: str):
    """
    Get a trainer by ID.
    """
    trainer = trainer_crud.get_trainer(session=session, trainer_id=trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")

    return trainer

@router.put("/{trainer_id}", response_model=TrainerPublic)
def update_trainer(*, session: SessionDep, trainer_id: str, trainer_in: TrainerCreate):
    """
    Update a trainer by ID.
    """
    trainer = trainer_crud.get_trainer(session=session, trainer_id=trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")

    updated_trainer = trainer_crud.update_trainer(
        session=session, trainer_id=trainer_id, trainer_update=trainer_in
    )

    return updated_trainer  

@router.delete("/{trainer_id}", response_model=dict)
def delete_trainer(*, session: SessionDep, trainer_id: str):
    """
    Delete a trainer by ID.
    """
    trainer = trainer_crud.get_trainer(session=session, trainer_id=trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")

    trainer_crud.delete_trainer(session=session, trainer_id=trainer_id)

    return {"detail": "Trainer deleted successfully"}