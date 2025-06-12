from fastapi import APIRouter

from app.api.routes import trainee
from app.api.routes import trainer
from app.api.routes import staff
from app.api.routes import admin
from app.api.routes import duty


router = APIRouter()
router.include_router(trainee.router, prefix="/trainees", tags=["trainees"])
router.include_router(trainer.router, prefix="/trainers", tags=["trainers"])
router.include_router(staff.router, prefix="/staff", tags=["staff"])
router.include_router(admin.router, prefix="/admin", tags=["admin"])
router.include_router(duty.router, prefix="/duty", tags=["duty"])
