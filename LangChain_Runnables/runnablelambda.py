from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel,RunnableLambda

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt=PromptTemplate(
    template='Write a joke about a {topic}',
    input_variables=['topic']

)
parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({

    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x:len(x.split()))
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'AI'}))


