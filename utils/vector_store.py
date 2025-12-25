import faiss
import numpy as np
from typing import List


class FAISSVectorStore:
    def __init__(self, embedding_dim: int):
        """
        Initialize FAISS vector store using cosine similarity.
        """
        # Inner Product = Cosine similarity when vectors are normalized
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.text_chunks: List[str] = []

    def add_embeddings(self, embeddings: np.ndarray, chunks: List[str]):
        """
        Add embeddings and their corresponding text chunks.

        Args:
            embeddings (np.ndarray): Shape (n, embedding_dim)
            chunks (List[str]): Corresponding text chunks
        """
        if embeddings.shape[0] != len(chunks):
            raise ValueError("Embeddings and chunks count mismatch")

        self.index.add(embeddings)
        self.text_chunks.extend(chunks)

    def similarity_search(self, query_embedding: np.ndarray, top_k: int = 3) -> List[str]:
        """
        Retrieve top-k most similar chunks for a query.

        Args:
            query_embedding (np.ndarray): Shape (1, embedding_dim)
            top_k (int): Number of results

        Returns:
            List[str]: Retrieved text chunks
        """
        scores, indices = self.index.search(query_embedding, top_k)
        return [self.text_chunks[i] for i in indices[0]]


# ---------------- TEST BLOCK ----------------
if __name__ == "__main__":
    print("🔹 Testing FAISS Vector Store")

    # Dummy normalized embeddings
    dummy_embeddings = np.random.rand(5, 384).astype("float32")
    dummy_embeddings /= np.linalg.norm(dummy_embeddings, axis=1, keepdims=True)

    dummy_chunks = [f"Chunk {i}" for i in range(5)]

    store = FAISSVectorStore(embedding_dim=384)
    store.add_embeddings(dummy_embeddings, dummy_chunks)

    query = np.random.rand(1, 384).astype("float32")
    query /= np.linalg.norm(query)

    results = store.similarity_search(query)

    print("✅ Retrieved Chunks:", results)
