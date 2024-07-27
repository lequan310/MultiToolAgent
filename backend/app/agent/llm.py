from app.config import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = HuggingFaceEndpoint(
    # endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
    # inference_server_url="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
    cache=False,
    seed=0,
)

messages = [
    SystemMessage(
        content="You're a lazy assistant. You give the shortest answer possible."
    ),
]


def get_llm_response(message: str):
    messages.append(HumanMessage(content=message))
    response = llm.invoke(messages)
    response_content = response.split("System:", 1)[-1].strip()
    messages.append(AIMessage(content=response_content))

    return response_content
