from fastapi import FastAPI
from app.routers import scrape, storage
import logging
import sys

app = FastAPI(title="Correspondence")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)

log_formatter = logging.Formatter(
        "%(asctime)s [%(processName)s: %(process)d] [%(levelname)s] %(name)s: %(message)s"
    )
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)


app.include_router(scrape.router)
app.include_router(storage.router)

