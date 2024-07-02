from typing import Optional

from pydantic import BaseModel, SecretStr, ConfigDict


class ApiKey(BaseModel):
    key: SecretStr
    api_provider_name: str
    api_provider_lowercase_name: str


class ApiKeysResponse(BaseModel):
    api_keys: Optional[list[ApiKey]] = None
