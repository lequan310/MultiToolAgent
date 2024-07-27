from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.core.llms import ChatMessage, MessageRole
from app.config import os

llm = HuggingFaceInferenceAPI(
    model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=os.getenv("HF_INFERENCE_KEY"),
    task="Text2Text Generation",  # conversational is deprecated
    max_tokens=100,
)


def get_agent_response(message: str):
    llm.system_prompt = (
        "You are a lazy assistant who gives the shortest answer possible."
    )
    response = llm.chat([ChatMessage(role=MessageRole.USER, content=message)])
    return response.message.content
