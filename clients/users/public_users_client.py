from clients.api_client import APIClient
from typing import Any, TypedDict
from httpx import Response

class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        '''
        Метод создания нового пользователя

        :param request: Словарь с email, паролем, фамилией, именем и вторым именем
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.post("/api/v1/users", json = request)