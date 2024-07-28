from qdrant_client import QdrantClient, models
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFMinerLoader
from typing import List


class QdrantDB:
    def __init__(
        self,
        host: str = None,
        port: int = None,
        vector_size: int = 384,
        embeddings: HuggingFaceEndpointEmbeddings = None,
    ):
        self.client = QdrantClient(host=host, port=port)
        self.vector_size: int = vector_size
        self.metric = models.Distance.COSINE
        self.embeddings = embeddings

    def collection_exists(self, collection_name: str) -> bool:
        return self.client.collection_exists(collection_name=collection_name)

    def init_collection(self, collection_name: str):
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=self.vector_size,
                distance=self.metric,
            ),
        )

    def delete_collection(self, collection_name: str):
        self.client.delete_collection(collection_name=collection_name)

    async def add_documents(self, collection_name: str, documents: List[Document]):
        if not self.collection_exists(collection_name):
            self.init_collection(collection_name)

        store = QdrantVectorStore(
            client=self.client,
            collection_name=collection_name,
            embedding=self.embeddings,
        )
        await store.aadd_documents(documents)

    async def add_pdf(self, collection_name: str, pdf_path: str):
        loader = PDFMinerLoader(pdf_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        documents = text_splitter.split_documents(documents)
        await self.add_documents(collection_name, documents)

    async def similarity_search_with_relevance_scores(
        self, collection_name: str, query: str, k: int = 1, score_threshold: float = 0.5
    ):
        store = QdrantVectorStore(
            client=self.client,
            collection_name=collection_name,
            embedding=self.embeddings,
        )
        result = await store.asimilarity_search_with_relevance_scores(
            query=query, k=k, score_threshold=score_threshold
        )
        return result
