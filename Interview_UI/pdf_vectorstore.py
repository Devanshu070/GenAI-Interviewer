# pdf_vectorstore.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.docstore.document import Document
from dotenv import load_dotenv
load_dotenv()
import os
HUGGINGFACEHUB_ACCESS_TOKEN = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN") 

def create_vectorstore(docs):
    # Step 1: Split the PDF content into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    # Step 2: Generate embeddings for each chunk
    # embeddings = OpenAIEmbeddings()  # uses OpenAI API under the hood
    
    # Step 2: Generate embeddings for each chunk
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



    # Step 3: Create a FAISS vector store
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    return vectorstore

if __name__ == "__main__":
    # Sample document (mock PDF content)
    sample_text = """
    Artificial Intelligence (AI) is transforming industries by automating tasks,
    providing insights from data, and enabling new ways of interacting with technology.
    One major application of AI is in natural language processing (NLP), which powers chatbots,
    translation tools, and semantic search systems.
    """

    # Wrap the text in a LangChain Document
    docs = [Document(page_content=sample_text)]

    # Create the vector store
    vectorstore = create_vectorstore(docs)

    print("Vectorstore created successfully!")

    # Run a similarity search
    query = "What are applications of AI?"
    results = vectorstore.similarity_search(query, k=2)

    # Print results
    print("\n🔍 Top Similar Results:")
    for i, res in enumerate(results, 1):
        print(f"\nResult {i}:\n{res.page_content}")

