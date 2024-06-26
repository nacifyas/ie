from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from db_connector import redis
from app.models.pibyd import PIByDDB
from app.models.embarazo import EmbarazosDB
from routes.api import api
from app.settings import Settings
import uvicorn, logging, platform, sys, asyncio


app = FastAPI()
app.mount("/assets", StaticFiles(directory="app/web/assets"), name="assets")
app.include_router(api.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def setup() -> None:
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{levelprefix} {asctime} {message}",
        style="{",
        use_colors=True)
    logger.handlers[0].setFormatter(console_formatter)
    print(f"Connected to Redis: {Settings().redis_db}")
    await PIByDDB.migrate()
    await EmbarazosDB.migrate()
    if sys.platform == 'win32' or  platform.system()=='Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)



@app.get("/")
async def index():
    return FileResponse("app/web/index.html")


@app.get("/", response_class=RedirectResponse)
async def redirect_to_dashboard():
    return "/dashboard"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080 if Settings().dev_mode else 80, reload=Settings().dev_mode)
