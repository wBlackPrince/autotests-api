from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class UpdateDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get("/api/v1/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/users/{id}")

    def update_user_api(self, user_id: str, request: UpdateDict) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.patch(f"/api/v1/users/{id}", json = request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.delete(f"/api/v1/users/{id}")