from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List


class EmbeddingModel:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Loads a Sentence Transformer embedding model.
        """
        print("🔹 Loading embedding model...")
        self.model = SentenceTransformer(model_name)
        print("✅ Embedding model loaded")

    def encode(self, texts: List[str]) -> np.ndarray:
        """
        Converts text chunks into normalized embeddings.

        Args:
            texts (List[str]): List of text chunks or queries

        Returns:
            np.ndarray: Normalized embedding vectors (float32)
        """
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,   # IMPORTANT for cosine similarity
            show_progress_bar=True
        )

        # FAISS expects float32
        return embeddings.astype("float32")


# ---------------- TEST BLOCK ----------------
if __name__ == "__main__":
    sample_texts = [
        "This paper proposes a new transformer model.",
        "The methodology uses BERT embeddings."
    ]

    embedder = EmbeddingModel()
    vectors = embedder.encode(sample_texts)

    print("\n✅ Embedding shape:", vectors.shape)
    print("🔢 Vector norm (should be ~1):", np.linalg.norm(vectors[0]))
