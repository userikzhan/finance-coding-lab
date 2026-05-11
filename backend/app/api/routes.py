from fastapi import APIRouter, UploadFile
from app.services.reconcile import reconcile

router = APIRouter()

@router.post("/reconcile")
async def reconcile_api(file: UploadFile):
    result = reconcile(file.file)
    return result
