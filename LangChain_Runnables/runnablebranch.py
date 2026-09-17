from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel,RunnableLambda,RunnableBranch

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt1=PromptTemplate(
    template='Write a detailed topic on {topic}',
    input_variables=['topic']

)

prompt2=PromptTemplate(
    template='Summarise the following \n {text}',
    input_variables=['text']

)
parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)
print(final_chain.invoke({'topic':"Unemployment in India"}))
