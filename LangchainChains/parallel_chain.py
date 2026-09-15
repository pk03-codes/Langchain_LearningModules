from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following \n {text}",
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'notes': prompt1 | model | parser,
        'quiz':prompt2 | model | parser
    }
)

merge_chain=prompt3 | model | parser

chain= parallel_chain | merge_chain

text="""Linear Regression

Linear regression is a supervised machine learning algorithm used to model the relationship between a dependent variable and one or more independent variables. In simple linear regression, the model assumes that the dependent variable can be predicted using a straight-line relationship with the independent variable. The general equation is y = b0 + b1x, where b0 is the intercept and b1 represents the change in y for a one-unit change in x.

The main objective of linear regression is to find the line that best fits the observed data. This is commonly done using the least squares method, which minimizes the sum of the squared differences between the actual values and the values predicted by the model. These differences are called residuals or errors.

Linear regression can be used for tasks such as predicting house prices from their features, estimating salary based on years of experience, or forecasting sales based on advertising expenditure. The quality of a regression model can be evaluated using metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R²).

A major assumption of linear regression is that the relationship between the predictors and the target is approximately linear. Other assumptions include independent observations, constant variance of errors, and, in some statistical applications, normally distributed residuals. While linear regression is relatively simple and interpretable, it may perform poorly when the underlying relationship between variables is highly nonlinear."""

result=chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()