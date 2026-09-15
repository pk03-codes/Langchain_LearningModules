from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt1=PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Generate a five pointer summary from the following text \n {text}",
    input=['text']
)
parser=StrOutputParser()

chain=prompt1|model|parser|prompt2|model|parser
result=chain.invoke({'topic':'Unemployment in Age of AI'})

print(result)

chain.get_graph().print_ascii()