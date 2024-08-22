from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.models.chat_request import ChatRequest
from app.agent.agent import get_agent_response

# from app.agent.llm import get_llm_response

router = APIRouter()


# @router.post(
#     "/response", response_description="Send a message to the chat and get chat response"
# )
# async def get_chat_response(chat_request: ChatRequest):
#     # TODO: Get chat response from AI agent
#     response = get_agent_response(chat_request.message)
#     return JSONResponse(content={"message": response})
