from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет что поля запроса и ответа на него совпадают
    :param request: Запрос, представленный pydantic-моделью
    :param response: Ответ, представленный pydantic-моделью
    :raises AssertionError: Если хотя-бы одно из полей не совпадает
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.middle_name, request.middle_name, "first_name")

