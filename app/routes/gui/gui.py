from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def dashboard():
    with open("app/web/index.html", "r") as file:
        html_content = file.read()
    return html_content
