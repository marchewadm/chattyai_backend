from typing_extensions import Annotated
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    ValidationInfo,
    StringConstraints,
    ConfigDict,
)


class ApiKeyBase(BaseModel):
    key: str


class ApiKeyCreate(ApiKeyBase):
    pass


class ApiKey(ApiKeyBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    name: Annotated[str, StringConstraints(min_length=1)]
    password: Annotated[str, StringConstraints(min_length=8)]
    password2: Annotated[str, StringConstraints(min_length=8)]

    @field_validator("password2")
    @classmethod
    def validate_password(cls, v: str, info: ValidationInfo) -> str:
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v


class UserLogin(UserBase):
    password: Annotated[str, StringConstraints(min_length=8)]


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    api_keys: list[ApiKey] = []
