"""
AmbedkarGPT - Simple Q&A system using RAG
"""

from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitters import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

# Configuration
SPEECH_PATH = "speech.txt"
PERSIST_DIR = "chroma_db"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
HF_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL_NAME = "mistral"

def build_vectorstore(speech_path: str, persist_directory: str):
    """Load speech, split, embed, and store in Chroma"""
    
    persist_path = Path(persist_directory)
    embeddings = HuggingFaceEmbeddings(model_name=HF_MODEL_NAME)
    
    # Load existing DB if available
    if persist_path.exists() and any(persist_path.iterdir()):
        print(f"[INFO] Loading existing Chroma DB from '{persist_directory}'")
        return Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    
    # Create new DB
    print("[INFO] Loading speech...")
    loader = TextLoader(speech_path, encoding="utf-8")
    docs = loader.load()
    
    print(f"[INFO] Splitting text into chunks...")
    splitter = CharacterTextSplitter(
        separator="\n", 
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    split_docs = splitter.split_documents(docs)
    
    print(f"[INFO] Creating embeddings and vector store...")
    vectordb = Chroma.from_documents(
        split_docs, 
        embeddings, 
        persist_directory=persist_directory
    )
    vectordb.persist()
    print("[INFO] Vector store created successfully!")
    return vectordb

def create_qa_chain(vectordb: Chroma):
    """Create RetrievalQA chain with Ollama LLM"""
    
    print("[INFO] Initializing Ollama LLM...")
    llm = Ollama(model=OLLAMA_MODEL_NAME, temperature=0.0)
    
    retriever = vectordb.as_retriever(
        search_type="similarity", 
        search_kwargs={"k": 4}
    )
    
    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever
    )
    return qa

def main():
    print("=" * 60)
    print("AmbedkarGPT - Q&A System")
    print("=" * 60)
    print("Type 'exit' or 'quit' to stop\n")
    
    # Build vectorstore and QA chain
    vectordb = build_vectorstore(SPEECH_PATH, PERSIST_DIR)
    qa_chain = create_qa_chain(vectordb)
    
    # Interactive Q&A loop
    try:
        while True:
            query = input("\nYour question > ").strip()
            
            if query.lower() in ("exit", "quit"):
                print("Goodbye!")
                break
                
            if not query:
                continue
            
            print("\n[INFO] Generating answer...")
            answer = qa_chain.run(query)
            
            print("\n" + "=" * 60)
            print("ANSWER:")
            print("=" * 60)
            print(answer.strip())
            print("=" * 60)
            
    except KeyboardInterrupt:
        print("\n\nGoodbye!")

if __name__ == "__main__":
    main()