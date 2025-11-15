from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM  # ✅ NEW IMPORT
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

SPEECH_PATH = "speech.txt"
PERSIST_DIR = "chroma_db"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
HF_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL_NAME = "mistral"

def build_vectorstore(speech_path: str, persist_directory: str):
    persist_path = Path(persist_directory)
    
    print("[INFO] Initializing embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name=HF_MODEL_NAME,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    if persist_path.exists() and any(persist_path.iterdir()):
        print(f"[INFO] Loading existing Chroma DB at '{persist_directory}'")
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )
    
    print("[INFO] Loading speech text file...")
    loader = TextLoader(speech_path, encoding="utf-8")
    docs = loader.load()
    
    print("[INFO] Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    split_docs = splitter.split_documents(docs)
    
    print(f"[INFO] Creating vector store with {len(split_docs)} chunks...")
    vectordb = Chroma.from_documents(
        split_docs,
        embeddings,
        persist_directory=persist_directory
    )
    
    print("[INFO] Vector store created successfully.")
    return vectordb

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def create_qa_chain(vectordb: Chroma):
    print("[INFO] Loading Ollama model...")
    
    llm = OllamaLLM(
        model=OLLAMA_MODEL_NAME,
        temperature=0.0
    )
    
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    
    template = """Answer the question based only on the following context:

{context}

Question: {question}

Answer: """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    print("[INFO] Creating RAG chain with LCEL...")
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain

def main():
    print("=" * 60)
    print("AmbedkarGPT – Latest LangChain RAG System")
    print("=" * 60)
    
    vectordb = build_vectorstore(SPEECH_PATH, PERSIST_DIR)
    qa_chain = create_qa_chain(vectordb)
    
    print("\n✓ System ready!")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Your question > ").strip()
        
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        if not query:
            continue
        
        print("\n[Thinking...]\n")
        answer = qa_chain.invoke(query)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()