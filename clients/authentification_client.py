from api_client import APIClient
from httpx import Client, URL, QueryParams, Response, Request
from typing import Any, TypedDict
from httpx._types import RequestData, RequestFiles

# get_user_headers = {
#     "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
# }
# get_user_response = httpx.get(f"http://127.0.0.1:8000/api/v1/users/{create_response_data["user"]["id"]}",
#                               headers = get_user_headers)
# get_user_response_data = get_user_response.json()
#
# print(f"Успешность получения пользователя: {get_user_response.status_code}")
# print(f"Данные запроса на получение пользователя: {get_user_response_data}")


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

