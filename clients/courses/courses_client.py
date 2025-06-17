from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.files.files_client import File
from clients.private_httpx_builder import AuthentificationUserDict, get_private_httpx_client
from clients.users.public_users_client import User


class GetCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str

class UpdateCourseRequestDict(TypedDict):
    '''
    Описание структуры запроса на обновление курса
    '''
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CreateCourseRequestDict(TypedDict):
    '''
    Описание структуры запроса на создание курса
    '''
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str




class Course(TypedDict):
    '''
    Структура данных курса
    '''
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class CreateCourseResponseDict(TypedDict):
    '''
    Структура ответа на создание курса
    '''
    course: Course


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query:GetCoursesRequestDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(
            "/api/v1/courses",
                params = query
        )

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/courses/{course_id}",
                                json = request)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/courses",
                json=request
        )

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        return self.create_course_api(request).json()

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")



def get_courses_client(user: AuthentificationUserDict) -> CoursesClient:
    '''
    Метод возвращающий объект CoursesClient
    :param user: Словарь с email, password
    :return: объект класса CoursesClient
    '''
    return CoursesClient(client = get_private_httpx_client(user))