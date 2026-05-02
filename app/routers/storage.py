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





