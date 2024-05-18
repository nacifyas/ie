import asyncio
from db_connector import redis
from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from app.models.embarazo import Embarazos, EmbarazosDB
from app.models.pibyd import PIByD, PIByDDB


router = APIRouter()



@router.get("/", response_class=RedirectResponse)
async def dashboard():
    return "/docs"


@router.get("/pibdesempleo")
async def datos_pib() -> list[PIByD]:
    corr_array = [PIByDDB.get(pk) async for pk in await PIByDDB.all_pks()]
    return sorted(await asyncio.gather(*corr_array), key=lambda x: x.date)


@router.post("/pibdesempleo")
async def nuevo_dato_pib(entrada: PIByD) -> str:
    db_pibd = await PIByDDB(**entrada.model_dump()).save()
    return db_pibd.pk


@router.delete("/pibdesempleo")
async def vaciar_datos_pib() -> int:
    corr_array = [PIByDDB.delete(pk) async for pk in await PIByDDB.all_pks()]
    return sum(await asyncio.gather(*corr_array))


@router.get("/embarazo")
async def datos_embarazo(limit: int = Query(100, ge=0, le=100), offset: int = Query(0, ge=0)) -> list[Embarazos]:
    keys = await redis.lrange("pregnancy", offset, offset+limit-1)
    corr_array = [EmbarazosDB.get(pk) for pk in keys]
    return list(await asyncio.gather(*corr_array))


@router.post("/embarazo")
async def nuevo_dato_embarazo(entrada: Embarazos) -> str:
    db_emb = await EmbarazosDB(**entrada.model_dump()).save()
    await redis.rpush("pregnancy",db_emb.pk)
    return db_emb.pk


@router.delete("/embarazo")
async def vaciar_datos_embarazos() -> int:
    keys_len = await redis.llen("pregnancy")
    corr_array = [EmbarazosDB.delete(redis.lpop("pregnancy")) for _ in range(keys_len)]
    return sum(await asyncio.gather(*corr_array))
