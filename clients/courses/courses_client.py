from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, \
    CreateCourseRequestSchema, CreateCourseResponseSchema, GetCoursesQuerySchema
from clients.private_httpx_builder import AuthentificationUserSchema, get_private_httpx_client


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query:GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(
            "/api/v1/courses",
                params = query.model_dump(by_alias=True)
        )

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"/api/v1/courses/{course_id}",
            json = request.model_dump(by_alias=True)
        )

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/courses",
                json=request.model_dump(by_alias=True)
        )

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")



def get_courses_client(user: AuthentificationUserSchema) -> CoursesClient:
    '''
    Метод возвращающий объект CoursesClient

    :param user: Словарь с email, password
    :return: объект класса CoursesClient
    '''
    return CoursesClient(client = get_private_httpx_client(user))