from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.public_httpx_builder import get_public_httpx_client


class User(TypedDict):
    '''
    Структура json-данных пользователя
    '''
    id: str
    email: str
    firstName: str
    middleName: str
    lastName: str

class CreateUserResponseDict(TypedDict):
    '''
    Структура ответа на создание пользователя
    '''
    user: User

class CreateUserRequestDict(TypedDict):
    '''
    Структура запроса для создания нового пользователя
    '''
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

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(get_public_httpx_client())