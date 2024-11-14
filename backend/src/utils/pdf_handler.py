from pymupdf4llm import to_markdown
from pymupdf import open as open_pdf
from fastapi import File, UploadFile


async def get_pdf_content(file: UploadFile):
    """Open PDF from UploadFile and return markdown text"""

    try:
        pdf_stream = await file.read()
        doc = open_pdf(stream=pdf_stream, filetype="pdf")
        md_text = to_markdown(doc, margins=(0))
        return md_text
    except:
        return "Error reading file"
