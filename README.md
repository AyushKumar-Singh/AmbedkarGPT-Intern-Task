# **AmbedkarGPT – RAG-Based Q&A System (Intern Task)**

A lightweight **Retrieval-Augmented Generation (RAG)** project built as part of the **Internshala Internship – Phase 1 Core Skills Evaluation**.  
This prototype demonstrates the ability to build an end-to-end AI pipeline using **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **Ollama (Mistral 7B)** — all running fully **offline and locally**.

---

## 🚀 **Project Overview**

AmbedkarGPT is a simple command-line Q&A system that:

1. Loads a provided speech by **Dr. B. R. Ambedkar** (`speech.txt`)
2. Splits the text into meaningful chunks  
3. Converts each chunk into vector embeddings using  
   **sentence-transformers/all-MiniLM-L6-v2**
4. Stores these embeddings in a local **ChromaDB** vector store
5. Uses a **RAG pipeline** to retrieve relevant context when a user asks a question
6. Generates the final answer using **Ollama’s Mistral 7B** model

This system ensures that **all answers come strictly from the speech**, not from external data.

---

## 🧠 **Tech Stack Used**

| Component | Technology |
|----------|------------|
| Programming Language | Python 3.8+ |
| Core Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Embeddings (MiniLM-L6-v2) |
| Local LLM | Ollama – Mistral 7B |
| Text Loader & Splitter | LangChain utilities |
| Retrieval Pipeline | LangChain RetrievalQA |

---

## 📂 **Repository Structure**

```
AmbedkarGPT-Intern-Task/
│
├── main.py               # The main CLI Q&A application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── speech.txt            # Provided Ambedkar speech excerpt
```

## 📥 **Setup & Installation**

To set up the AmbedkarGPT system, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ayushkumar-singh/ambedkargpt.git
    cd AmbedkarGPT-Intern-Task
    ```

2. **Install the required dependencies**:
    It is recommended to use a virtual environment. First, create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    Then, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the speech file**:
    Obtain the `speech.txt` file containing the speech by Dr. B. R. Ambedkar and place it in the root directory of the project.

4. **Run the application**:
    To start the application, run:
    ```bash
    python app.py
    ```
    Follow the on-screen instructions to interact with the system.

---

## 🧑‍💻 **How to Use**

1. **Ask a Question**:
    Once the application is running, you can type in any question related to the speech by Dr. B. R. Ambedkar.

2. **Receive Answer**:
    The system will process your question, retrieve relevant context from the speech, and generate an answer using the Mistral 7B model.

3. **Continue the Conversation**:
    You can ask follow-up questions or new questions at any time. The system is designed to handle multi-turn conversations.

---

## ⚙️ **Customization & Development**

- To customize the behavior or improve the system, you can modify the underlying scripts:
  - `embeddings.py`: Change embedding models or parameters.
  - `retrieve.py`: Alter retrieval methods or context length.
  - `answer.py`: Tweak answer generation settings or switch models.

- For development, you can add new features or improve existing ones by editing the respective Python files. Use clear, descriptive names for new functions or classes, and ensure to update this documentation if you add significant new features.

---

## 🐞 **Troubleshooting & FAQs**

**Q1: What to do if I encounter an error while running the application?**  
A1: Please check the following:
  - Ensure you have installed all the required dependencies listed in `requirements.txt`.
  - Make sure you are using Python 3.8 or higher.
  - If the error persists, please raise an issue on the [GitHub repository](https://github.com/yourusername/ambedkargpt/issues) with details of the error.

**Q2: Can I use my own text files?**  
A2: Yes, you can use any text file as a knowledge base. Just replace `speech.txt` with your file and ensure it is properly formatted.

**Q3: How can I improve the answer quality?**  
A3: The answer quality depends on the underlying models and the quality of the embeddings. You can experiment with different models or fine-tune the existing models on a similar domain corpus.

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Thank you for using AmbedkarGPT! 🙌**  
**Let's keep the legacy of Dr. B. R. Ambedkar alive through his words.**

