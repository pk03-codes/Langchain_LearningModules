from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    PyPDFLoader
)

# Load TXT files
txt_loader = DirectoryLoader(
    "Info",
    glob="*.txt",
    loader_cls=TextLoader
)

# txt_docs = txt_loader.load()


# Load PDF files
pdf_loader = DirectoryLoader(
    "Info",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# pdf_docs = pdf_loader.load()


# Combine them
# docs = txt_docs + pdf_docs

# # for document in docs:
#     print(document.metadata)

txt_docs = list(txt_loader.lazy_load())

pdf_docs = list(pdf_loader.lazy_load())

docs = txt_docs + pdf_docs

for document in docs:
    print(document.metadata)