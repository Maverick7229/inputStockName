# llm_groq.py
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="gemma2-9b-it",  # or use other available models
    temperature=0.2
)
