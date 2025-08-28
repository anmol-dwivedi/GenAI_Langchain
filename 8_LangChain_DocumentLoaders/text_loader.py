from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()


# text loader
#loader = TextLoader('/home/anmol/Desktop/GenAI_LangChain/8_LangChain_DocumentLoaders/cricket.txt', encoding='utf-8')
loader = TextLoader('8_LangChain_DocumentLoaders/cricket.txt', encoding='utf-8')
docs = loader.load()
print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)


# use the text loader in a chain
chain = prompt | model | parser
print(chain.invoke({'poem':docs[0].page_content}))