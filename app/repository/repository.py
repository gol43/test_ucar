from abc import ABC, abstractmethod
from sqlalchemy import insert, select, update
from app.database.db import get_session


class AbstractRepository(ABC):
    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def update_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, model):
        self.model = model

    async def find_all(self):
        async with get_session() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def add_one(self, data: dict) -> int:
        async with get_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
            
    async def update_one(self, obj_id: int, data: dict) -> int:
        async with get_session() as session:
            exists = await session.execute(select(self.model).where(self.model.id == obj_id))
            if not exists.scalar():
                raise ValueError(f"Объект с id {obj_id} не найден")
            stmt = update(self.model).where(self.model.id == obj_id).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
        