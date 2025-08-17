from clients.api_client import APIClient
from httpx import Response
from clients.public_httpx_builder import get_public_httpx_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import allure
from tools.routes import ApiRoutes

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        '''
        Метод создания нового пользователя

        :param request: Словарь с email, паролем, фамилией, именем и вторым именем
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.post(ApiRoutes.USERS, json = request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        '''
        Метод для создания нового пользователя, работает поверх низкоуровневого метода для создания пользователя
        :param request: Словарь с email, паролем, фамилией, именем и вторым именем
        :return: Словарь с json-данными пользователя
        '''
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(get_public_httpx_client())