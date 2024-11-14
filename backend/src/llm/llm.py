from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from src.config import os

gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
openai_llm = ChatOpenAI(model="gpt-4o", temperature=0)
