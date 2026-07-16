from fastapi import APIRouter
from app.models.common import InfoResponse
from app.core.config import settings

router = APIRouter()

@router.get("/info", response_model=InfoResponse, tags=["infra"])
def info():
    return InfoResponse(name=settings.APP_NAME, version=settings.APP_VERSION, api_prefix=settings.API_V1_STR)
