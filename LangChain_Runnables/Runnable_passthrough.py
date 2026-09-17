from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

passthrough=RunnablePassthrough()

print(passthrough.invoke({'name':'Priyam'}))