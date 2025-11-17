# 🎓 AmbedkarGPT — Local RAG-Based Question Answering System  
**Fully Offline • ChromaDB • HuggingFace Embeddings • Ollama (Mistral 7B)**

AmbedkarGPT is a lightweight Retrieval-Augmented Generation (RAG) prototype designed for the **Internshala Phase-1 Core Skills Evaluation**.  
It processes an excerpt of Dr. B. R. Ambedkar’s speech and answers questions **locally** using vector search + a local LLM (Mistral 7B via Ollama).

No cloud APIs. No external dependencies. 100% offline.

---

## 🎯 Project Goal (Intern Task Requirements)

The system must:

1. Load `speech.txt`  
2. Split text into chunks  
3. Generate embeddings using **sentence-transformers/all-MiniLM-L6-v2**  
4. Store embeddings in **ChromaDB (persistent)**  
5. Retrieve relevant chunks based on user questions  
6. Generate answers using **Ollama (Mistral 7B)**  
7. Run fully offline — *strictly local execution*

This repository contains a clean, minimal solution that satisfies all requirements.

---

## ⚡ Features

- 🧠 **Local NLP embeddings** (HuggingFace MiniLM-L6)  
- 📦 **ChromaDB persistent vector store**  
- 🤖 **Local LLM inference** using **Ollama + Mistral 7B**  
- 🧩 **LangChain-based RAG pipeline**  
- 💻 **Simple interactive CLI**  
- 🔒 **Runs fully offline** after initial embedding download  
- ⚙️ **Clear and modular implementation**

---

## 📁 Repository Structure

```
AmbedkarGPT-Intern-Task/
├── main.py             # CLI entry point + RAG pipeline
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── speech.txt          # Provided Ambedkar speech excerpt
```

---

## 🛠️ Prerequisites

### **1. Python**
- Python **3.8+** recommended (3.10 / 3.11 preferred)

### **2. Ollama + Mistral 7B**
Ollama does not run natively on Windows — use **WSL2**.

**Windows Setup:**
```bash
wsl --install
```

Inside WSL terminal:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull mistral
```

---

## 🚀 Setup Instructions (Windows / WSL Compatible)

### **Clone the repository**
```bash
git clone <your-repo-url>
cd AmbedkarGPT-Intern-Task
```

### **Create a Python virtual environment**
**Windows PowerShell:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**WSL / Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### **Install dependencies**
```bash
pip install -r requirements.txt
```

### **Verify Ollama installation**
Inside WSL:
```bash
ollama list
```

Make sure `mistral` appears in the list.

---

## ▶️ Run the Application

```bash
python main.py
```

### On first run:
- Creates `chroma_db/` directory  
- Generates embeddings  
- Persists vector store  

### On subsequent runs:
- Immediately loads vector DB  
- Fast retrieval + answer generation  

### Exit:
Type `exit` or `quit`.

---

## 🧠 Implementation Details (Summary of main.py Logic)

- Load speech with `TextLoader`  
- Split into chunks (`chunk_size=500`, `chunk_overlap=50`)  
- Create embeddings via:

```python
HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

- Persist vector store to:

```
./chroma_db
```

- Use `Ollama` LLM with `"mistral"` model  
- Build LangChain `RetrievalQA` pipeline  
- Enforce grounded answers (no hallucinations)  
- Interactive CLI loop for Q&A  

---

## 🧹 Troubleshooting

### ❌ `ollama: command not found`
- You must run Ollama **inside WSL**, not PowerShell.

### ❌ Embedding metadata mismatch / Chroma errors
Delete the DB and rebuild:
```bash
rm -rf chroma_db/
python main.py
```

### ❌ Mistral model not found
Inside WSL:
```bash
ollama pull mistral
```

### ❌ Very slow startup (first run only)
Embeddings + vector DB creation takes time.  
Subsequent runs are fast.

---

## ❓ Example Questions

Try:
- *“What remedy does Ambedkar propose?”*  
- *“What analogy does Ambedkar use for social reform?”*  
- *“Why can’t caste and belief in shastras coexist?”*

---

## 📦 Deliverables Checklist (Internshala)

- ✔ `main.py` — Working CLI RAG pipeline  
- ✔ `requirements.txt` — Dependencies included  
- ✔ `speech.txt` — Provided text  
- ✔ `README.md` — Complete documentation  
- ✔ Local embeddings + local LLM (no external API)

---

## 📜 License
MIT License

---

## 🙏 Acknowledgement
Built as part of the **Internshala Core Skills Evaluation (Phase 1)**.

