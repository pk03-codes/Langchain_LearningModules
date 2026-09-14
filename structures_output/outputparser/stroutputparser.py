from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



# result=model.invoke("what is the capital of USA?")
# print(result.content)
#1st prompt -> detailed report
template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt->summary
template2=PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain= template1 | model |parser | template2 | model | parser

result=chain.invoke({'topic':'black hole'})

print(result)
