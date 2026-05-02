from fastapi import APIRouter
from app.services import file_uploader

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("")

def upload(delete=True):    
    file_uploader.main()
    return



