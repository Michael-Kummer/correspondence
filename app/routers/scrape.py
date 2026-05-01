from fastapi import APIRouter
from app.services import downloader

router = APIRouter(prefix="/scrape-new", tags=["scraper"])

@router.post("")

def scrape(mode: str="new"):
    downloader.main(mode)
    return

