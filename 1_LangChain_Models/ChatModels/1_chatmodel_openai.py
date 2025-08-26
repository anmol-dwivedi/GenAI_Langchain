from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4',
                    temperature = 1.5, 
                    max_completion_tokens=10) # restricts the number of output tokens from the model (helps save money)


result = model.invoke("What is the capital of Chattisgarh?",)

#  print(result)  # here we will get output with metadata
# print(result.content) # exclude the metadata info


result2 = model.invoke("Write a 5 line poem on cricket")
print(result2.content) # exclude the metadata info