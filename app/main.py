from fastapi import FastAPI
from app.settings import Settings
import uvicorn, logging


app = FastAPI()


@app.on_event("startup")
def logging_setup() -> None:
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{levelprefix} {asctime} {message}",
        style="{",
        use_colors=True)
    logger.handlers[0].setFormatter(console_formatter)


@app.get("")
async def index():
    return "Hello there"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=Settings().port, reload=Settings().dev_mode)