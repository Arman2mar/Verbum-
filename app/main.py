from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import health, info

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

# Include API routers
app.include_router(health.router, prefix=settings.API_V1_STR)
app.include_router(info.router, prefix=settings.API_V1_STR)

@app.get("/", include_in_schema=False)
def root():
    return {"message": f"{settings.APP_NAME} - see {settings.API_V1_STR}/docs"}
