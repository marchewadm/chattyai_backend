from typing import Annotated

from fastapi import Depends, Security

from src.services.auth import AuthService
from src.services.user import UserService
from src.services.api_provider import ApiProviderService
from src.services.api_key import ApiKeyService

from src.schemas.auth import AuthCurrentUser


AuthServiceDependency = Annotated[AuthService, Depends(AuthService)]
UserServiceDependency = Annotated[UserService, Depends(UserService)]
ApiProviderServiceDependency = Annotated[
    ApiProviderService, Depends(ApiProviderService)
]
ApiKeyServiceDependency = Annotated[ApiKeyService, Depends(ApiKeyService)]

AuthDependency = Annotated[
    AuthCurrentUser, Security(AuthService.get_current_user)
]
