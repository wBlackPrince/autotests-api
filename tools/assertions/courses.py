from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
import allure
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")


@allure.step("Check update course response")
def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update course response")

    assert_equal(request.title, response.course.title, "title")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")


@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса совпадают с ожидаемыми данными между собой.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check course")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

@allure.step("Get courses response")
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    logger.info("Get courses response")

    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)

@allure.step("Check create course response")
def assert_create_course_response(
    request: CreateCourseRequestSchema,
    response: CreateCourseResponseSchema
):
    """
    Проверяет, что данные ответа на создание курса совпадают с данными запроса на создание курса

    :param request: Данные запроса на создание курса
    :param response: Данные Ответа на создание курса
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create course response")

    assert_equal(request.title, response.course.title, "title")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")
    assert_equal(request.preview_file_id, response.course.preview_file.id, "preview_file_id")
    assert_equal(request.created_by_user_id, response.course.created_by_user.id, "created_by_user_id")

