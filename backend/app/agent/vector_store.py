from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import os
from app.agent.vectordb.qdrant import QdrantDB
import asyncio

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
qdrant = QdrantDB(
    host=os.getenv("QDRANT_HOST"),
    port=int(os.getenv("QDRANT_PORT")),
    embeddings=embeddings,
)


# if qdrant.collection_exists("test_collection"):
#     qdrant.delete_collection("test_collection")
# asyncio.run(qdrant.add_pdf("test_collection", "app/data/journal.pdf"))
