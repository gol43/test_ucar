from fastapi import HTTPException

from app.repository.repository import SQLAlchemyRepository
from app.schemas.incedent_shemas import IncedentCreate, IncedentUpdate

class IncedentService:
    def __init__(self, model):
        self.incedents_repository = SQLAlchemyRepository(model)
    
    async def find_incedents(self):
        incedents_all = await self.incedents_repository.find_all()
        return incedents_all
    
    async def add_incedent(self, incedent: IncedentCreate) -> int:
        incedent_dict = incedent.model_dump()
        incedent_id = await self.incedents_repository.add_one(incedent_dict)
        return incedent_id

    async def update_incedent(self, incedent_id: int, incedent: IncedentUpdate) -> int:
        try:
            return await self.incedents_repository.update_one(incedent_id, incedent.model_dump())
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))