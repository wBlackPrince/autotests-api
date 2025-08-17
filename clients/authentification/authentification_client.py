from httpx import Response
from clients.api_client import APIClient
from clients.authentification.authentification_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_httpx_builder import get_public_httpx_client
import allure
from tools.routes import ApiRoutes

class AuthentificationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    @allure.step("Authentificate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{str(ApiRoutes.AUTHENTIFICATION)}/login", json = request.model_dump(by_alias=True))

    @allure.step("Refresh authentification token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{str(ApiRoutes.AUTHENTIFICATION)}/refresh", json = request.model_dump(by_alias=True))


    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        '''
        Метод получения токенов
        :param request: Словарь с email, password
        :return: Вложенный словарь с refreshToken, tokenType, accessToken
        '''
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentification_client() -> AuthentificationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthentificationClient(client = get_public_httpx_client())
