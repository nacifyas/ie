import asyncio
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.models.embarazo import Embarazos, EmbarazosDB
from app.models.pibyd import PIByD, PIByDDB


router = APIRouter()



@router.get("/", response_class=RedirectResponse)
async def dashboard():
    return "/docs"


@router.get("/pibdesempleo")
async def api() -> list[PIByD]:
    corr_array = [PIByDDB.get(pk) async for pk in await PIByDDB.all_pks()]
    return sorted(await asyncio.gather(*corr_array), key=lambda x: x.date)


@router.post("/pibdesempleo")
async def new(entrada: PIByD) -> str:
    db_pibd = await PIByDDB(**entrada.model_dump()).save()
    return db_pibd.pk


@router.get("/embarazo")
async def api() -> list[Embarazos]:
    corr_array = [EmbarazosDB.get(pk) async for pk in await EmbarazosDB.all_pks()]
    return sorted(await asyncio.gather(*corr_array), key=lambda x: x.income)


@router.post("/embarazo")
async def new(entrada: Embarazos) -> str:
    db_emb = await EmbarazosDB(**entrada.model_dump()).save()
    return db_emb.pk


