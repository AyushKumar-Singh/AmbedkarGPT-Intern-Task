# 🎓 AmbedkarGPT – RAG-Based Q&A System

A lightweight, fully-local Retrieval-Augmented Generation (RAG) prototype that answers questions from a short speech by Dr. B. R. Ambedkar. Built for the Internshala Phase 1 Core Skills Evaluation using LangChain, ChromaDB, HuggingFace embeddings and Ollama (Mistral 7B).

---

## Project goal (Intern task)
Implement a CLI Q&A system that:
1. Loads `speech.txt`.  
2. Splits the speech into chunks.  
3. Creates HF embeddings (sentence-transformers/all-MiniLM-L6-v2).  
4. Persists embeddings in ChromaDB.  
5. Retrieves context for a user question.  
6. Generates answers with Ollama (Mistral 7B).  
All components must run locally with no API keys.

---

## Quick features
- Fully offline and local.  
- Persistent Chroma vector store.  
- Embeddings: sentence-transformers/all-MiniLM-L6-v2.  
- Local LLM: Ollama (Mistral 7B).  
- Simple interactive CLI.

---

## Repo layout
```
AmbedkarGPT-Intern-Task/
├── main.py             # CLI entrypoint and RAG pipeline
├── requirements.txt    # Python deps
├── README.md           # This file
└── speech.txt          # Provided Ambedkar excerpt
```

---

## Prerequisites and notes

- Python 3.8+ (recommended 3.10 or 3.11).  
- Ollama + Mistral 7B installed locally.

Important for Windows users:
- Ollama runs in WSL2 (recommended). Install WSL2 and run Ollama inside the Linux distro:
  - In Windows PowerShell: `wsl --install`
  - Inside WSL shell:
    - `curl -fsSL https://ollama.ai/install.sh | sh`
    - `ollama pull mistral`

---

## Setup (Windows / WSL-friendly)

1. Clone the repo:
   git clone <your-repo-url>
   cd AmbedkarGPT-Intern-Task

2. Create and activate a venv:
   - Windows (PowerShell):
     python -m venv venv
     .\venv\Scripts\Activate.ps1
   - WSL / macOS / Linux:
     python -m venv venv
     source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Ensure Ollama is installed and `mistral` is pulled (in the environment where `ollama` runs).

---

## Run

Start the CLI:

python main.py

On first run the script should build the Chroma DB (persist directory like `chroma_db`); subsequent runs reuse it.

Type a question when prompted. Type `exit` or `quit` to stop.

---

## Implementation notes (what main.py should do)
- Load speech.txt with a TextLoader.  
- Split text (e.g., chunk_size=500, overlap=50).  
- Use HuggingFaceEmbeddings (all-MiniLM-L6-v2).  
- Persist Chroma vectorstore to `./chroma_db`.  
- Create a RetrievalQA chain using Ollama LLM configured to use `mistral`.  
- Prompt LLM to answer only from retrieved context to reduce hallucinations.

---

## Troubleshooting

- "ollama: command not found": Run Ollama inside WSL or the OS where Ollama is installed.  
- Embeddings fail to download: ensure network access during first run.  
- Chroma dimension mismatch after swapping embedding model: delete `chroma_db/` and rebuild.

Useful commands:
- Rebuild DB: delete `chroma_db/` then re-run main.py.
- Check ollama models: `ollama list`

---

## Sample questions
- What is the real remedy according to Ambedkar?  
- What analogy does Ambedkar use for social reform?  
- Why can’t caste and belief in the shastras coexist?

---

## Deliverables checklist
- main.py — working, documented code.  
- requirements.txt — pinned dependencies.  
- README.md — this file.  
- speech.txt — provided speech excerpt.

---

## License
MIT

---

Thank you — this README focuses on clarity, local-first setup, and Windows/WSL specifics required for Ollama.

