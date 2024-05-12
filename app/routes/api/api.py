import asyncio
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
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
