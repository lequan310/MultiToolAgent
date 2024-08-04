from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils.pdf_parser import get_pdf_content

router = APIRouter()


@router.post(
    "/upload", response_description="Upload a pdf file and get the text content"
)
async def get_file_content(file: UploadFile = File(...)):
    result = await get_pdf_content(file)
    print(result)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "content": result,
    }
