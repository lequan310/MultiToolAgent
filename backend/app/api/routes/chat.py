from fastapi import APIRouter
from app.api.models.chat_request import ChatRequest

router = APIRouter()


@router.post(
    "/response", response_description="Send a message to the chat and get chat response"
)
def get_chat_response(chat_request: ChatRequest):
    # TODO: Get chat response from AI agent
    return {"message": chat_request.message}
