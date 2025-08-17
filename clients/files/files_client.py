from httpx import Response
from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_httpx_builder import AuthentificationUserSchema, get_private_httpx_client
import allure
from tools.routes import ApiRoutes

class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Get file by {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{ApiRoutes.FILES}/{file_id}")

    @allure.step("Delete file by {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{ApiRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            ApiRoutes.FILES,
            data = request.model_dump(by_alias=True, exclude={"upload_file"}),
            files = {"upload_file": request.upload_file.read_bytes()}
        )

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        '''
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Json объект с filename, directory, upload_file.
        '''
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)



def get_files_client(user: AuthentificationUserSchema) -> FilesClient:
    '''
    Метод возвращающий объект FilesClient
    :param user: Словарь с email, password
    :return: объект класса FilesClient
    '''
    return FilesClient(client = get_private_httpx_client(user))