from qdrant_client import QdrantClient
from typing import List


class QdrantDB:
    def __init__(self, host: str, port: int):
        self.client = QdrantClient(host, port)
