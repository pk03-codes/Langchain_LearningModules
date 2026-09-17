from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt=PromptTemplate(
    template='Write the summary of the following: {text}',
    input_variables=['text']
)

parser=StrOutputParser()



loader=TextLoader(
    'sample.txt',encoding='utf-8'
)

chain=prompt|model|parser

docs=loader.load()

print(chain.invoke({'text':docs[0].page_content}))