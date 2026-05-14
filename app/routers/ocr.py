from fastapi import APIRouter
from app.services import extractor
import logging

logging = logging.getLogger(__name__)

router = APIRouter(prefix="/scrape", tags=["scraper"])

@router.post("/new")
def extract(filename):
    extractor.main("new")
    return
