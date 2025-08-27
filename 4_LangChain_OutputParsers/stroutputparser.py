from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


model = ChatHuggingFace(llm=llm)

# 1st promt -> detailed report
template_1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables= ['topic'])


# 2nd Prompt -> summary
template_2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. /n {text}',
    input_variables=['text'])


prompt1 = template_1.invoke({'topic':'Black Hole'})
result = model.invoke(prompt1)
prompt2 = template_2.invoke({'text':result.content})
result1 = model.invoke(prompt2)
print(result1.content)
