

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()





doc1 = Document(
    page_content="Virat Kohli is one of the most successful and popular Indian cricketers.",
    metadata={
        "team": "Royal Challengers Bangalore"
    }
)

doc2 = Document(
    page_content="Rohit Sharma is one of the most successful captains in IPL history.",
    metadata={
        "team": "Mumbai Indians"
    }
)

doc3 = Document(
    page_content="MS Dhoni is one of the most famous and successful captains in IPL history.",
    metadata={
        "team": "Chennai Super Kings"
    }
)


documents = [doc1, doc2,doc3]
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)



vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="chroma_db"
)


vector_store.add_documents(documents)



results = vector_store.similarity_search(
    "Who plays for Mumbai Indians?",
    k=2
)



for doc in results:
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
    print()