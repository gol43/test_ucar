from fastapi import APIRouter, Depends
from typing import Annotated

from app.schemas.incedent_shemas import IncedentCreate, IncedentOut, IncedentUpdate
from app.services.incedent_service import IncedentService
from app.api.dependencies import incedents_services

incedent_router = APIRouter()


@incedent_router.post('/create_incedent/')
async def create_incedent(incedent_in: IncedentCreate,
                          incedent_service: Annotated[IncedentService, Depends(incedents_services)]):
    incedent_id = await incedent_service.add_incedent(incedent_in)
    return {'ok': True, 'created_id': incedent_id}


@incedent_router.get('/get_all_incedents/', response_model=list[IncedentOut])
async def get_all_incedents(incedent_service: Annotated[IncedentService, Depends(incedents_services)]):
    return await incedent_service.find_incedents()


@incedent_router.patch('/update_status/{incedent_id}')
async def update_status_incedent(incedent_id: int,
                                 incedent_in: IncedentUpdate,
                                 incedent_service: Annotated[IncedentService, Depends(incedents_services)]):
    updated_id = await incedent_service.update_incedent(incedent_id, incedent_in)
    return {"ok": True, "updated_id": updated_id}
