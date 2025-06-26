import pytest
from clients.private_httpx_builder import AuthentificationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from pydantic import BaseModel, EmailStr


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthentificationUserSchema:
        return AuthentificationUserSchema(
            email = self.request.email,
            password = self.request.password
        )

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)

@pytest.fixture
def private_users_client(function_user) -> PrivateUsersClient:
    private_user_client = get_private_users_client(function_user.authentication_user)
    return private_user_client