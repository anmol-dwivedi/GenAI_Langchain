from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os

# Use a lightweight, reliable model
model_id = "openai-community/gpt2"  # ~500MB

# Optional: set custom HF cache dir
os.environ['HF_HOME'] = os.path.expanduser('~/huggingface_cache')

# Load tokenizer and model manually
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, use_safetensors=True)

# Build pipeline manually (on CPU)
pipe = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1,  # -1 = CPU
)

# Wrap in LangChain LLM wrapper
llm = HuggingFacePipeline(pipeline=pipe)

# Run the prompt
prompt = "What is the capital of India?"
response = llm.invoke(prompt)
print(response)
