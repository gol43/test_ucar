from pydantic import BaseModel
from app.database.enums import IncedentStatus, IncedentSource
from datetime import datetime


class IncedentCreate(BaseModel):
    text: str
    source: IncedentSource = IncedentSource.MONITORING
    status: IncedentStatus = IncedentStatus.PENDING


class IncedentUpdate(BaseModel):
    status: IncedentStatus


class IncedentOut(BaseModel):
    id: int
    text: str
    source: IncedentSource
    status: IncedentStatus
    created_at: datetime

    class Config:
        from_attributes = True

