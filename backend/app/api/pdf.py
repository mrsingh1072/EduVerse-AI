from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.services.pdf_service import create_pdf

router = APIRouter()


class PDFRequest(BaseModel):
    content: str


@router.post("/notes")
async def export_notes_pdf(
    data: PDFRequest
):

    filename = create_pdf(
        data.content,
        "notes.pdf"
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename="notes.pdf"
    )


@router.post("/exam")
async def export_exam_pdf(
    data: PDFRequest
):

    filename = create_pdf(
        data.content,
        "exam.pdf"
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename="exam.pdf"
    )