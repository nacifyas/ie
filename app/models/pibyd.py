from app.redis import redis
from aredis_om import HashModel, Migrator
from datetime import date
import asyncio

class PIByD(HashModel):
    date: date
    pib: float
    tasa_desempleo: float

    class Config:
        extra = 'ignore'

    class Meta:
        database = redis

asyncio.run(Migrator().run())
