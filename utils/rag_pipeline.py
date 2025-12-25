from typing import List, Dict
from transformers import pipeline

from utils.embeddings import EmbeddingModel
from utils.vector_store import FAISSVectorStore


class RAGPipeline:
    def __init__(
        self,
        vector_store: FAISSVectorStore,
        embedder: EmbeddingModel,
        model_name: str = "google/flan-t5-base",
        device: int = -1
    ):
        """
        RAG Pipeline with source citations.
        """
        print("🔹 Loading LLM...")
        self.generator = pipeline(
            task="text2text-generation",
            model=model_name,
            device=device
        )
        print("✅ LLM loaded")

        self.vector_store = vector_store
        self.embedder = embedder

    def build_prompt(self, context_chunks: List[str], question: str) -> str:
        """
        Builds a concise, hallucination-safe prompt.
        """
        context = "\n\n".join(
            [f"[Source {i+1}]\n{chunk}" for i, chunk in enumerate(context_chunks)]
        )

        prompt = f"""
You are an expert research assistant.

Answer the question using ONLY the information from the sources below.
Cite sources in your answer like [Source 1], [Source 2].
Do NOT copy text verbatim.
If the answer is not present, say:
"I don't know based on the provided document."

Sources:
{context}

Question:
{question}

Answer (concise, 3–5 sentences or bullet points):
"""
        return prompt.strip()

    def answer(self, question: str, top_k: int = 3) -> Dict:
        """
        Generate an answer with cited sources.

        Returns:
            Dict with answer + source chunks
        """
        # 1️⃣ Embed query
        query_embedding = self.embedder.encode([question])

        # 2️⃣ Retrieve chunks
        retrieved_chunks = self.vector_store.similarity_search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        # 3️⃣ Build prompt
        prompt = self.build_prompt(retrieved_chunks, question)

        # 4️⃣ Generate answer
        output = self.generator(
            prompt,
            max_new_tokens=150,
            do_sample=False
        )

        return {
            "answer": output[0]["generated_text"],
            "sources": {
                f"Source {i+1}": chunk
                for i, chunk in enumerate(retrieved_chunks)
            }
        }


# ---------------- TEST BLOCK ----------------
if __name__ == "__main__":
    from utils.pdf_loader import extract_text_from_pdf
    from utils.text_chunker import chunk_text

    print("🔹 Testing RAG Pipeline with Citations")

    # 1️⃣ Load & chunk document
    text = extract_text_from_pdf("sample.pdf")
    chunks = chunk_text(text)

    # 2️⃣ Initialize embedding + vector store
    embedder = EmbeddingModel()
    embeddings = embedder.encode(chunks)

    store = FAISSVectorStore(embedding_dim=embeddings.shape[1])
    store.add_embeddings(embeddings, chunks)

    # 3️⃣ Initialize RAG
    rag = RAGPipeline(
        vector_store=store,
        embedder=embedder
    )

    # 4️⃣ Ask question
    question = "What methodology does the paper propose?"
    result = rag.answer(question)

    print("\n🧠 Question:", question)
    print("\n📌 Answer:\n", result["answer"])

    print("\n📚 Sources Used:")
    for k, v in result["sources"].items():
        print(f"\n{k}:\n{v[:300]}...")
