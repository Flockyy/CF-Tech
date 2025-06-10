from fastapi import APIRouter

from app.api.routes import trainee

router = APIRouter()
router.include_router(trainee.router, prefix="/trainees", tags=["trainees"])
router.include_router(trainee.router, prefix="/trainers", tags=["trainers"])