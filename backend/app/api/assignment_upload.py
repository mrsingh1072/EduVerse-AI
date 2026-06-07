from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
import shutil
import os

router = APIRouter()


@router.post("/")
async def upload_assignment(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "filename": file.filename,
        "saved_path": file_path
    }