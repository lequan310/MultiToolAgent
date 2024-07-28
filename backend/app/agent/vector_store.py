from langchain_huggingface import HuggingFaceEndpointEmbeddings
from app.config import os
from app.agent.vectordb.qdrant import QdrantDB
import asyncio

if os.getenv("DOCKER_ENV"):
    HOST = os.getenv("QDRANT_HOST")
    PORT = os.getenv("QDRANT_PORT")
else:
    HOST = "localhost"
    PORT = 6333

embeddings = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
    repo_id="BAAI/bge-small-en-v1.5",  # Equivalent of Qdrant FastText embeddings
)
qdrant = QdrantDB(host=HOST, port=PORT, embeddings=embeddings)


# if qdrant.collection_exists("test_collection"):
#     qdrant.delete_collection("test_collection")
# asyncio.run(qdrant.add_pdf("test_collection", "app/data/journal.pdf"))
