from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_httpx_builder import AuthentificationUserDict, get_private_httpx_client


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class File(TypedDict):
    '''
    Описание файла в структуре оответа на создание файла
    '''
    id: str
    filename: str
    directory: str
    url: str


class CreateFileResponseDict(TypedDict):
    '''
    Описание структуры ответа на создание файла
    '''
    file: File


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/files",
                                data = request,
                                files = {"upload_file": open(request["upload_file"], "rb")})

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        '''
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Json объект с filename, directory, upload_file.
        '''
        return self.create_file_api(request).json()



def get_files_client(user: AuthentificationUserDict) -> FilesClient:
    '''
    Метод возвращающий объект FilesClient
    :param user: Словарь с email, password
    :return: объект класса FilesClient
    '''
    return FilesClient(client = get_private_httpx_client(user))