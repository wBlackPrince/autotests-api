from httpx import Client
from clients.authentification.authentification_client import get_authentification_client, LoginRequestDict
from typing import TypedDict


class AuthentificationUserDict(TypedDict):
    '''
    Структура запроса на получение приватного httpx клиента
    '''
    email: str
    password: str


def get_private_httpx_client(user: AuthentificationUserDict) -> Client:
    '''
    Метод-builder для создания клиента, способного работать с приватными эндпоинтами
    :return: объект класса Client
    '''
    authentification_client = get_authentification_client()

    login_request = LoginRequestDict(email = user["email"], password = user["password"])

    login_response = authentification_client.login(login_request)

    return Client(
        timeout = 100,
        base_url = "http://localhost:8000",
        headers = {"Authorization": f"Bearer {login_response["token"]["accessToken"]}"}
    )