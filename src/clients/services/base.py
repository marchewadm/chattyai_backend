from abc import ABC, abstractmethod

from src.dependencies import AuthDependency, RedisServiceDependency
from src.clients.schemas.common import AiModelsResponse


class BaseService(ABC):
    """
    Base abstract class for external APIs services.

    All services should inherit from this class.
    Contains some already implemented methods that can be used by child classes.
    """

    def __init__(self, ai_models: list[str]) -> None:
        """
        Initializes the service.

        Args:
            ai_models (list[str]): List of all supported Large Language Models (LLMs).

        Returns:
            None
        """

        self.ai_models = ai_models

    @classmethod
    @abstractmethod
    def _get_api_provider_name(cls) -> str:
        """
        The name of the API provider.

        Returns:
            str: The name of the API provider.
        """

        pass

    @classmethod
    async def get_api_key(
        cls,
        auth: AuthDependency,
        redis_service: RedisServiceDependency,
    ) -> str:
        """
        Retrieve an API key for a user based on the API provider name.

        Args:
            auth (AuthDependency): The authentication dependency.
            redis_service (RedisServiceDependency): The Redis service dependency.

        Raises:
            HTTPException: Raised with status code 404 if the user does not have any API keys stored in Redis.

        Returns:
            str: The decrypted API key if found.
        """

        api_key = await redis_service.get_user_specific_api_key_from_cache(
            auth.uuid, cls._get_api_provider_name()
        )

        return api_key

    def get_ai_models(self) -> AiModelsResponse:
        """
        Get all available Large Language Models (LLMs) for the user.

        Returns:
            AiModelsResponse: The response containing the list of all available LLMs.
        """

        return AiModelsResponse(ai_models=self.ai_models)