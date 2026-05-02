from fastapi import APIRouter
from app.services import downloader
import logging

logging = logging.getLogger(__name__)

router = APIRouter(prefix="/scrape", tags=["scraper"])

@router.post("/new")
def scrape():
    downloader.main("new")
    return

