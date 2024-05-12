from pydantic import BaseModel
from app.db_connector import redis
from aredis_om import HashModel, Migrator
from datetime import date


class PIByDDB(HashModel):
    date: date
    pib: float
    tasa_desempleo: float

    async def migrate():
        await Migrator().run()

    class Config:
        extra = 'ignore'

    class Meta:
        database = redis

class PIByD(BaseModel):
    date: date
    pib: float
    tasa_desempleo: float
    
    class Config:
        extra = 'ignore'

# if Settings().dev_mode: asyncio.run(Migrator().run())