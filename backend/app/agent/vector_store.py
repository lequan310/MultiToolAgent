from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_qdrant import QdrantVectorStore, RetrievalMode
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFMinerLoader
from qdrant_client import QdrantClient
from app.config import os
import re


loader = PDFMinerLoader("app/data/journal.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

documents = text_splitter.split_documents(documents)

embeddings = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
)

qdrant = QdrantVectorStore.from_documents(
    documents,
    embeddings,
    path=":memory:",
    collection_name="my_documents",
    retrieval_mode=RetrievalMode.DENSE,
)

query = "When is Week 12?"
found_docs = qdrant.similarity_search_with_relevance_scores(
    query, k=1, score_threshold=0.5
)

if found_docs:
    found, score = found_docs[0]
    print(found.dict()["page_content"])
    print(score)
