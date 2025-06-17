from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.public_httpx_builder import get_public_httpx_client


class Token(TypedDict):
    """
    Описание токена, который содержится внутри ответа на аутентификацию
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа на аутентификацию.
    """
    token: Token

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str

class AuthentificationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """


    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json = request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json = request)


    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        '''
        Метод получения токенов
        :param request: Словарь с email, password
        :return: Вложенный словарь с refreshToken, tokenType, accessToken
        '''
        response = self.login_api(request)
        return response.json()


def get_authentification_client() -> AuthentificationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthentificationClient(client = get_public_httpx_client())
