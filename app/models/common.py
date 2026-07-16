from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

class InfoResponse(BaseModel):
    name: str
    version: str
    api_prefix: str
