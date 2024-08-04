from langchain_community.document_loaders import PyPDFLoader
from fastapi import File, UploadFile
import os


async def get_pdf_content(file: UploadFile):
    try:
        contents = await file.read()
        os.makedirs("temp", exist_ok=True)

        filepath = "temp/{}".format(file.filename)
        with open(filepath, "wb") as temp:
            temp.write(contents)
    except:
        return "Error reading file"

    try:
        loader = PyPDFLoader(filepath, extraction_mode="layout")
        documents = loader.load()
        contents = [doc.page_content for doc in documents]
        result = "\n".join(contents)
        os.remove(filepath)
    except:
        return "Error loading PDF"

    return result
