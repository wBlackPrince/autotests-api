from httpx import Response
from clients.api_client import APIClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, \
    CreateCourseRequestSchema, CreateCourseResponseSchema, GetCoursesQuerySchema
from clients.private_httpx_builder import AuthentificationUserSchema, get_private_httpx_client
import allure
from tools.routes import ApiRoutes

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    @allure.step("Get courses")
    def get_courses_api(self, query:GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(
            f"{ApiRoutes.COURSES}",
                params = query.model_dump(by_alias=True)
        )

    @allure.step("Get course by {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{ApiRoutes.COURSES}/{course_id}")

    @allure.step("Update course by {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"{ApiRoutes.COURSES}/{course_id}",
            json = request.model_dump(by_alias=True)
        )

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            f"{ApiRoutes.COURSES}",
                json=request.model_dump(by_alias=True)
        )


    @allure.step("Delete course by {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{ApiRoutes.COURSES}/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)



def get_courses_client(user: AuthentificationUserSchema) -> CoursesClient:
    '''
    Метод возвращающий объект CoursesClient

    :param user: Словарь с email, password
    :return: объект класса CoursesClient
    '''
    return CoursesClient(client = get_private_httpx_client(user))