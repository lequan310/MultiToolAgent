from pymupdf4llm import to_markdown
from pymupdf import open as open_pdf
from fastapi import File, UploadFile
import io
import os


async def get_pdf_content(file: UploadFile):
    try:
        content = await file.read()
        pdf_stream = io.BytesIO(content)
        doc = open_pdf(stream=pdf_stream, filetype="pdf")
        md_text = to_markdown(doc, margins=(0))
        return md_text
    except:
        return "Error reading file"
