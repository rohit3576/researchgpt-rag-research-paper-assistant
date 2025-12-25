from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> List[str]:
    """
    Splits text into overlapping chunks.

    Args:
        text (str): Cleaned extracted text
        chunk_size (int): Number of characters per chunk
        overlap (int): Number of overlapping characters

    Returns:
        List[str]: List of text chunks
    """
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks: List[str] = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ---------------- TEST BLOCK ----------------
if __name__ == "__main__":
    from utils.pdf_loader import extract_text_from_pdf

    pdf_path = "sample.pdf"
    text = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(text)

    print(f"✅ Total chunks created: {len(chunks)}\n")
    print("🧩 Sample Chunk:\n")
    print(chunks[0])
