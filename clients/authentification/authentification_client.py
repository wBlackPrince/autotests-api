
from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient


class LoginDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class RefreshDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str

class AuthentificationClient(APIClient):
    def login_api(self, request: LoginDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("http://127.0.0.1:8000/api/v1/authentication/login", json = request)

    def refresh_api(self, request: RefreshDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("http://127.0.0.1:8000/api/v1/authentication/refresh", json = request)

