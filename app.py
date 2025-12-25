import gradio as gr
import re

from utils.pdf_loader import extract_text_from_pdf
from utils.text_chunker import chunk_text
from utils.embeddings import EmbeddingModel
from utils.vector_store import FAISSVectorStore
from utils.rag_pipeline import RAGPipeline


# ---------------- LOAD CUSTOM CSS ----------------
with open("assets/styles.css", "r", encoding="utf-8") as f:
    custom_css = f.read()


# ---------------- GLOBAL OBJECTS ----------------
embedder = EmbeddingModel()
vector_store = None
rag_pipeline = None
current_pdf_path = None


# ---------------- HELPERS ----------------
def highlight_citations(text: str) -> str:
    """
    Wrap [Source X] with citation highlight span
    """
    return re.sub(
        r"\[(Source \d+)\]",
        r'<span class="citation">[\1]</span>',
        text
    )


# ---------------- CORE LOGIC ----------------
def process_pdf(pdf_file):
    global vector_store, rag_pipeline, current_pdf_path

    if pdf_file is None:
        return "❌ Please upload a PDF first.", None

    # Gradio provides temp file path
    current_pdf_path = pdf_file.name

    # 1️⃣ Extract & chunk
    text = extract_text_from_pdf(current_pdf_path)
    chunks = chunk_text(text)

    if not chunks:
        return "❌ No readable text found in the PDF.", None

    # 2️⃣ Embed
    embeddings = embedder.encode(chunks)

    # 3️⃣ FAISS store
    vector_store = FAISSVectorStore(embedding_dim=embeddings.shape[1])
    vector_store.add_embeddings(embeddings, chunks)

    # 4️⃣ RAG pipeline
    rag_pipeline = RAGPipeline(
        vector_store=vector_store,
        embedder=embedder
    )

    # PDF preview iframe
    pdf_preview = f"""
    <div class="pdf-preview">
        <iframe src="{current_pdf_path}"></iframe>
    </div>
    """

    return f"✅ Paper indexed successfully ({len(chunks)} sections).", pdf_preview


def ask_question(question):
    if rag_pipeline is None:
        return "❌ Upload and process a paper first.", ""

    if not question.strip():
        return "❌ Please enter a question.", ""

    result = rag_pipeline.answer(question)

    answer = highlight_citations(result["answer"])
    sources = result["sources"]

    # Collapsible animated sources
    sources_md = ""
    for src, text in sources.items():
        sources_md += f"""
<details>
<summary>{src}</summary>
{text}
</details>
"""

    return (
        "🧠 Analyzing research paper…\n"
        "Extracting relevant sections and validating context.\n\n"
        + answer,
        sources_md
    )


# ---------------- THEME TOGGLE ----------------
def toggle_theme(is_light):
    return "light" if is_light else ""


# ---------------- GRADIO UI ----------------
with gr.Blocks(css=custom_css, title="📄 ResearchGPT") as demo:

    theme_toggle = gr.Checkbox(label="🌗 Light Mode")

    gr.Markdown(
        """
        <div class="glass">
        <h1>📄 ResearchGPT</h1>
        <p>
        <b>Explainable RAG-based Research Assistant</b><br>
        Ask questions on research papers with grounded answers and citations.
        </p>
        </div>
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group(elem_classes="glass"):
                pdf_input = gr.File(
                    label="📑 Upload Research Paper (PDF)",
                    file_types=[".pdf"]
                )
                upload_btn = gr.Button("⚡ Process Paper")
                status_output = gr.Textbox(
                    label="Status",
                    interactive=False,
                    placeholder="Waiting for PDF..."
                )

        with gr.Column(scale=2):
            with gr.Group(elem_classes="glass"):
                question_input = gr.Textbox(
                    label="Ask a Question",
                    placeholder="e.g. What methodology does the paper propose?",
                    lines=2
                )
                ask_btn = gr.Button("🧠 Generate Answer")

    with gr.Row():
        with gr.Column():
            with gr.Group(elem_classes="glass"):
                answer_output = gr.Markdown(
                    label="Answer"
                )

        with gr.Column():
            with gr.Group(elem_classes="glass"):
                sources_output = gr.Markdown(
                    label="📚 Sources (click to expand)"
                )

    with gr.Row():
        with gr.Group(elem_classes="glass"):
            pdf_preview_output = gr.HTML()

    upload_btn.click(
        fn=process_pdf,
        inputs=pdf_input,
        outputs=[status_output, pdf_preview_output]
    )

    ask_btn.click(
        fn=ask_question,
        inputs=question_input,
        outputs=[answer_output, sources_output]
    )

    theme_toggle.change(
        fn=toggle_theme,
        inputs=theme_toggle,
        outputs=gr.HTML()
    )

    gr.Markdown(
        """
        <div class="glass">
        <small>
        🔍 RAG-based answers • 📚 Expandable citations • 🧠 Explainable AI • 📄 PDF preview
        </small>
        </div>
        """
    )


if __name__ == "__main__":
    demo.launch()
