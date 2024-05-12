from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.models.pibyd import PIByDDB
from routes.api import api
from app.settings import Settings
import uvicorn, logging, platform, sys, asyncio


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/web"), name="static")
app.include_router(api.router, prefix="/api")


@app.on_event("startup")
async def setup() -> None:
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{levelprefix} {asctime} {message}",
        style="{",
        use_colors=True)
    logger.handlers[0].setFormatter(console_formatter)
    await PIByDDB.migrate()
    if sys.platform == 'win32' or  platform.system()=='Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)



@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    with open("app/web/index.html", "r") as file:
        html_content = file.read()
    return html_content



@app.get("/", response_class=RedirectResponse)
async def redirect_to_dashboard():
    return "/dashboard"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080 if Settings().dev_mode else 80, reload=Settings().dev_mode)
