from abc import ABC, abstractmethod

from sqlalchemy.exc import NoResultFound

from fastapi import HTTPException, status

from src.shared.repository.base import BaseRepository


class BaseService[T: BaseRepository]:
    """
    Base class for services.

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


class BaseAiService(ABC):
    """
    Base abstract class for AI services.

    All AI services should inherit from this class.

    Contains some already implemented methods that can be used by child classes.
    """

    def __init__(self) -> None:
        """
        Initialize the service.

        Returns:
            None
        """

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
