from langchain_huggingface import HuggingFaceEndpointEmbeddings
from app.config import os
from app.agent.vectordb.qdrant import QdrantDB
import asyncio

embeddings = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
    repo_id="BAAI/bge-small-en-v1.5",  # Equivalent of default Qdrant FastEmbed text embeddings
)
qdrant = QdrantDB(
    host=os.getenv("QDRANT_HOST"),
    port=int(os.getenv("QDRANT_PORT")),
    embeddings=embeddings,
)


# if qdrant.collection_exists("test_collection"):
#     qdrant.delete_collection("test_collection")
# asyncio.run(qdrant.add_pdf("test_collection", "app/data/journal.pdf"))
