from fastapi import FastAPI
from app.routers import scrape

app = FastAPI(title="Correspondence")

app.include_router(scrape.router)

