from fastapi import APIRouter

from src.shared.schemas import (
    AiModelsResponse,
    ChatHistoryCompletionRequest,
    ChatHistoryCompletionResponse,
)

from src.auth.dependencies import AuthDependency
from src.chat_room.dependencies import ChatRoomServiceDependency
from src.chat_history.dependencies import ChatHistoryServiceDependency
from .dependencies import OpenAiServiceDependency, OpenAiApiKeyDependency


router = APIRouter(prefix="/openai", tags=["openai"])


@router.get("/models", response_model=AiModelsResponse)
async def get_openai_models(
    auth: AuthDependency,
    openai_service: OpenAiServiceDependency,
):
    """
    Get the available OpenAI models.
    """

    return openai_service.get_ai_models()


@router.post("/chat", response_model=ChatHistoryCompletionResponse)
async def chat_with_openai(
    auth: AuthDependency,
    api_key: OpenAiApiKeyDependency,
    openai_service: OpenAiServiceDependency,
    chat_room_service: ChatRoomServiceDependency,
    chat_history_service: ChatHistoryServiceDependency,
    payload: ChatHistoryCompletionRequest,
):
    """
    Send message to OpenAI's model and get response from it.
    """

    return await openai_service.chat(
        auth.user_id, api_key, chat_room_service, chat_history_service, payload
    )
