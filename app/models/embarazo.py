from pydantic import BaseModel
from app.db_connector import redis
from aredis_om import HashModel, Migrator


class EmbarazosDB(HashModel):
    age: int
    income: str
    anxiety: int
    depression: int
    mother_risk: int
    baby_risk: int
    baby_problems: int 

    async def migrate():
        await Migrator().run()

    class Config:
        extra = 'ignore'

    class Meta:
        database = redis


class Embarazos(BaseModel):
    age: int
    income: str
    depression: int
    anxiety: int
    mother_risk: int
    baby_risk: int
    baby_problems: int 

    class Config:
        extra = 'ignore'