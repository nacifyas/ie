from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.settings import Settings
import uvicorn, logging


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/web"), name="static")

@app.on_event("startup")
def logging_setup() -> None:
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{levelprefix} {asctime} {message}",
        style="{",
        use_colors=True)
    logger.handlers[0].setFormatter(console_formatter)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("app/web/index.html", "r") as file:
        html_content = file.read()
    return html_content


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080 if Settings().dev_mode else 80, reload=Settings().dev_mode)
