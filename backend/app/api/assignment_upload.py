from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter()


@router.post("/")
async def upload_assignment(
    file: UploadFile = File(...)
):

    return {
        "filename": file.filename
    }