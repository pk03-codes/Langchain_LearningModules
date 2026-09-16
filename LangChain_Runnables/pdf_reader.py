from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Load the document
loader = TextLoader("docs.txt")
documents = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Convert text into embeddings and store in FAISS
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# Create a retriever
retriever = vectorstore.as_retriever()

# Manually retrieve relevant documents
query = "What are the key takeaways from the document?"

retrieved_docs = retriever.invoke(query)

# Combine retrieved text into a single string
retrieved_text = "\n".join(
    doc.page_content for doc in retrieved_docs
)

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Manually pass retrieved text to LLM
prompt = f"""
Based on the following text, answer the question.

Question:
{query}

Context:
{retrieved_text}
"""

answer = llm.invoke(prompt)

# Print the answer
print("Answer:", answer.content)