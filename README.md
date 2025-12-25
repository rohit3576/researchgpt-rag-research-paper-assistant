📄 ResearchGPT — RAG Research Paper Assistant

ResearchGPT is a fully featured, explainable Retrieval-Augmented Generation (RAG) system that allows users to ask natural-language questions on research papers and receive grounded, citation-aware answers.

The system combines semantic retrieval (FAISS + embeddings) with LLM-based answer generation, wrapped in a modern, premium UI designed for real-world research workflows.

🚀 Live Demo

👉 Hugging Face Spaces
https://huggingface.co/spaces/rohit3576/researchgpt-rag

📌 What ResearchGPT Does

✅ Upload research papers in PDF format

✅ Extract and clean academic text

✅ Split content into semantic chunks

✅ Generate dense embeddings using Sentence-Transformers

✅ Perform similarity search using FAISS

✅ Generate answers using a lightweight LLM (FLAN-T5)

✅ Highlight citations inside answers

✅ Display collapsible source sections

✅ Preview uploaded PDFs

✅ Light / Dark mode toggle

✅ Premium liquid-glass modern UI

🧠 How It Works (RAG Pipeline)

ResearchGPT follows a standard Retrieval-Augmented Generation (RAG) architecture:

PDF ingestion – extract raw text from research papers

Text chunking – split long documents into overlapping semantic chunks

Embedding generation – convert chunks into vector representations

Vector indexing – store embeddings in a FAISS index

Semantic retrieval – fetch the most relevant chunks for a query

Answer generation – pass retrieved context to an LLM

Explainability – return answers with cited source sections

This approach reduces hallucinations and ensures that answers are grounded in the original document.

🧱 Project Structure
ResearchGPT/
│
├── app.py                     # Gradio UI and application logic
├── requirements.txt           # Python dependencies
├── README.md
│
├── assets/
│   └── styles.css             # Premium liquid-glass UI styling
│
├── utils/
│   ├── __init__.py
│   ├── pdf_loader.py          # PDF text extraction
│   ├── text_chunker.py        # Text chunking logic
│   ├── embeddings.py          # Embedding model loader
│   ├── vector_store.py        # FAISS vector index
│   └── rag_pipeline.py        # Retrieval + generation pipeline
│
└── sample.pdf                 # Example PDF (optional)

🛠 Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/rohit3576/researchgpt-rag-research-paper-assistant.git
cd researchgpt-rag-research-paper-assistant
2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py


Open the app in your browser:

http://127.0.0.1:7860


📌 Usage

Upload a research paper (PDF)

Click Process Paper to build embeddings

Ask questions such as:

What methodology does the paper propose?

What are the main contributions?

What results were achieved?

View:

Answer with highlighted citations

Expandable source text

Embedded PDF preview

🧪 Example

Question:

What methodology does the paper propose?


Answer (example):

The paper evaluates models using head-to-head statistical t-tests across multiple runs.
It defines review helpfulness based on user voting behavior and explores the impact of auxiliary features such as star ratings.
These methods are applied consistently across different product categories.
[Source 1] [Source 2]

🎨 Feature Summary
Feature	Status
PDF Upload	✅
Text Extraction	✅
Chunking	✅
FAISS Similarity Search	✅
Embedding Model	✅
LLM Answer Generation	✅
Citation Highlighting	✅
Collapsible Sources	✅
PDF Preview	✅
Light / Dark Mode	✅
UI	

🧠 Tech Stack

Gradio — Interactive UI

PyPDF2 — PDF parsing

Sentence-Transformers — Text embeddings

FAISS (CPU) — Vector similarity search

Transformers (FLAN-T5) — Answer generation

Python — Backend logic

Hugging Face Spaces — Deployment

🧑‍💻 Why This Project Matters

Retrieval-Augmented Generation (RAG) systems are becoming essential for building trustworthy AI applications.
By grounding LLM outputs in retrieved source documents, ResearchGPT demonstrates how to:

Reduce hallucinations

Improve factual accuracy

Provide explainable AI outputs

This project is portfolio-ready, interview-ready, and mirrors real-world AI system design.

🧪 Future Enhancements

Multi-PDF support

Conversational (chat) memory

Highlight exact quoted sentences inside PDFs

Improved handling of tables and figures

Persistent vector storage

📜 License

This project is open-source and free to use for educational and personal purposes.

👤 Author

Rohit Pawar
AI / ML Engineer
