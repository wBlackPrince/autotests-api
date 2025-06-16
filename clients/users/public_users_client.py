from clients.api_client import APIClient
from typing import Any, TypedDict
from httpx import Response

class CreateDict:
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateDict) -> Response:
        '''
        Метод создания нового пользователя

        :param request: Словарь с email, паролем, фамилией, именем и вторым именем
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.post("http://127.0.0.1:8000/api/v1/users", json = request)