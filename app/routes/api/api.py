import asyncio
from fastapi import APIRouter
from app.models.pibyd import PIByD


router = APIRouter()


@router.get("/pibdesempleo", response_model=PIByD)
async def api() -> list[PIByD]:
    corr_array = [PIByD.get(pk) for pk in await PIByD.all_pks()]
    return list(asyncio.gather(corr_array))
