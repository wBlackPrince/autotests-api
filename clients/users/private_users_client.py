from clients.api_client import APIClient
from httpx import Response
from clients.private_httpx_builder import get_private_httpx_client, AuthentificationUserSchema
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema
import allure
from tools.routes import ApiRoutes


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Get user me")
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{ApiRoutes.USERS}/me")

    @allure.step("Get user by {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{ApiRoutes.USERS}/{user_id}")

    @allure.step("Update user by {user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{ApiRoutes.USERS}/{user_id}", json = request.model_dump(by_alias=True))

    @allure.step("Delete user by {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{ApiRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        '''
        Метод получения данных запроса в виде json для эндпоинта /api/v1/users/{user_id}
        :param user_id: Идентификатор пользователя
        :return: ответ от сервера в виде объекта Response
        '''
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthentificationUserSchema) -> PrivateUsersClient:
    '''
    Метод возвращающий объект PrivateUsersClient
    :param user: Словарь с email, password
    :return: объект класса PrivateUsersClient
    '''
    return PrivateUsersClient(client = get_private_httpx_client(user))