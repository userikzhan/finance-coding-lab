from fastapi import APIRouter, UploadFile, File
import pandas as pd

from app.logger import logger

from app.metrics import increment_uploads
increment_uploads()

router = APIRouter()


@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):

    logger.info(f"Upload started: {file.filename}")

    try:

        df = pd.read_excel(file.file)

        rows = len(df)

        logger.info(f"File processed successfully. Rows: {rows}")

        return {
            "status": "success",
            "filename": file.filename,
            "rows": rows
        }

    except Exception as e:

        logger.error(f"Upload failed: {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }
