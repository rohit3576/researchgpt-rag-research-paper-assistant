# 📄 ResearchGPT — RAG Research Paper Assistant

**ResearchGPT** is a fully featured, explainable **Retrieval-Augmented Generation (RAG)** system designed to help users ask natural language questions on research papers and get **grounded, sourced answers**.  
It supports PDF uploads, semantic retrieval, citation highlighting, and a modern premium UI.

---

## 🚀 Live Demo

👉 **Hugging Face Spaces** (deployed version):  
https://huggingface.co/spaces/YOUR_USERNAME/ResearchGPT

*(Replace `YOUR_USERNAME` with your own account name)*

---

## 📌 What ResearchGPT Does

✔ Upload research papers (PDF)  
✔ Extract and clean text from the document  
✔ Split text into semantic chunks  
✔ Create embeddings using Sentence-Transformers  
✔ Perform similarity search with FAISS  
✔ Use a lightweight LLM (FLAN-T5) for answer generation  
✔ Display answers with **highlighted citations**  
✔ Show **collapsible source sections**  
✔ Preview the uploaded PDF  
✔ Light / Dark mode toggle  
✔ Premium modern UI with liquid-glass styling

---

## 🧠 How It Works

ResearchGPT uses the core idea of **Retrieval-Augmented Generation (RAG)**, where the system:

1. **Extracts and chunks** the input document  
2. **Embeds text into vector representations**  
3. **Stores vectors in a FAISS index**  
4. **Retrieves relevant text chunks** based on user queries  
5. **Generates answers** using an LLM with retrieved context  
6. **Displays answers with source citations**

This approach helps reduce hallucination and makes answers explainable. :contentReference[oaicite:1]{index=1}

---

## 🧱 Project Structure

ResearchGPT/
│
├── app.py # Gradio UI
├── requirements.txt # Dependencies
├── README.md
│
├── assets/
│ └── styles.css # Custom UI styling (liquid glass)
│
├── utils/
│ ├── init.py
│ ├── pdf_loader.py # PDF text extraction
│ ├── text_chunker.py # Text chunking
│ ├── embeddings.py # Embedding model
│ ├── vector_store.py # FAISS integration
│ └── rag_pipeline.py # RAG logic (retrieval + generation)
│
└── sample.pdf # Example/test PDF (optional)

yaml
Copy code

---

## 🛠 Installation (Local)

1. **Clone the repository**

```bash
git clone https://github.com/rohit3576/researchgpt-rag-research-paper-assistant.git
cd researchgpt-rag-research-paper-assistant
Create a virtual environment

bash
Copy code
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS / Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the app

bash
Copy code
python app.py
Open the local Gradio UI:

cpp
Copy code
http://127.0.0.1:7860
📌 Usage
Upload a PDF research paper

Process the paper (building embeddings)

Ask a question like:

What methodology does the paper propose?

Summarize the main contributions

What are the results and conclusions?

View the answer with:

Highlighted citation references

Expandable source text

PDF preview

🧪 Example
After uploading a PDF, asking:

nginx
Copy code
What methodology does the paper propose?
will produce a sourced answer such as:

Answer:
The paper uses head-to-head t-tests between different models to assess significance.
It defines review helpfulness based on user votes and explores additional feature effects.

with citation spans like:

css
Copy code
[Source 1] [Source 2] …
🎨 Features Summary
Feature	Included
PDF Upload	✅
Text Extraction	✅
Chunking	✅
FAISS Similarity Search	✅
Embedding Model	✅
Answer Generation	✅
Citation Highlighting	✅
Collapsible Sources	✅
PDF Preview	✅
Light / Dark Mode	✅
Premium UI	🔥

🧠 Tech Stack
Gradio — Interactive UI

PyPDF2 — PDF parsing

Sentence-Transformers — Embeddings

FAISS (CPU) — Vector search

Transformers (FLAN-T5) — Answer generation

Python — Backend

Hugging Face Spaces — Deployment

🧑‍💻 Why This Matters
RAG systems are increasingly important because they ground generated answers in actual source text, improving accuracy and reliability — unlike vanilla LLM responses which may hallucinate facts. 
OpenAI Help Center

This project demonstrates a full real-world RAG pipeline, ideal for portfolios, interviews, and research tooling.

🧪 Future Enhancements
Support for multiple PDFs at once

Chat history / multi-turn conversations

Highlight exact quoted sentences in PDF

Better document layout handling (tables, figures)

📜 License
This project is open-source and free to use.

👤 Author

Rohit Pawar, AI/ML Engineer
