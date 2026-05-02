from fastapi import APIRouter
from app.services import storage
import logging


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/storage", tags=["storage"])

@router.get("/get-files")
async def get_files():
    logger.info('Routing to get-files')
    files = storage.fetch_files()
    return files

@router.post("/upload-today")
async def put_today():
    result = storage.place_file()
    return result

@router.post("/upload-file/{filename}")
async def put_files(filename: str | None = None):
    result = storage.place_file(filename)
    return result

