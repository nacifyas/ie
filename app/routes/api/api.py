from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def api():
    return "api api api"
