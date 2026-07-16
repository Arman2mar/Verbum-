from fastapi import APIRouter
from app.models.common import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse, tags=["infra"])
def health():
    return HealthResponse(status="ok")
