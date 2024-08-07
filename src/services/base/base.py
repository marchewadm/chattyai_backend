from abc import ABC, abstractmethod

from sqlalchemy.exc import NoResultFound

from fastapi import HTTPException, status

from src.repositories.base import BaseRepository
from src.schemas.common import AiModelsResponse


class BaseService[T: BaseRepository](ABC):
    """
    Base abstract class for services.

    This class enforces the use of an instance of a base repository for operations.

    Contains some already implemented methods that can be used by child classes.
    """

    def __init__(self, repository: T) -> None:
        """
        Initialize the service with a repository.

        Args:
            repository (T): The repository to use for operations.

        Returns:
            None
        """

        self.repository = repository

    @abstractmethod
    def create(self, payload) -> None:
        """
        Create new entity and store it in the database.

        Args:
            payload: The data to create the entity with.

        Returns:
            None
        """

        pass

    def get_one_by_id(self, entity_id: int):
        """
        Get an entity by its ID.

        Args:
            entity_id (int): The ID of the entity to retrieve.

        Raises:
            HTTPException: Raised with status code 404 if the entity is not found.
        """

        try:
            return self.repository.get_one_by_id(entity_id)
        except NoResultFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Entity with ID {entity_id} not found",
            )

    def delete_by_id(self, entity_id: int) -> None:
        """
        Delete an entity by its ID.

        Args:
            entity_id (int): The ID of the entity to delete.

        Raises:
            HTTPException: Raised with status code 404 if the entity is not found.

        Returns:
            None
        """

        try:
            self.repository.delete_by_id(entity_id)
        except NoResultFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Could not delete entity with ID {entity_id}. Entity not found.",
            )


class BaseAiService[T: BaseRepository](BaseService[T], ABC):
    """
    Base abstract class for AI services.

    This class enforces the use of an instance of a base repository for operations.
    All AI services should inherit from this class.

    Contains some already implemented methods that can be used by child classes.
    """

    def __init__(self, repository: T, ai_models: list[str]) -> None:
        """
        Initialize the service with a repository and a list of supported AI models.

        Args:
            repository (T): The repository to use for operations.
            ai_models (list[str]): List of all supported AI models.

        Returns:
            None
        """

        super().__init__(repository)
        self.ai_models = ai_models

    @staticmethod
    @abstractmethod
    async def get_api_key(auth, redis_service, api_provider_name: str) -> str:
        """
        Retrieve an API key for a user based on the API provider name.

        Args:
            auth: The authentication dependency.
            redis_service: The Redis service dependency.
            api_provider_name (str): The name of the API provider.

        Returns:
            str: The API key for the user.
        """

        pass

    def get_ai_models(self) -> AiModelsResponse:
        """
        Get all available Large Language Models (LLMs) for the user.

        Returns:
            AiModelsResponse: The response containing the list of all available LLMs.
        """

        return AiModelsResponse(ai_models=self.ai_models)