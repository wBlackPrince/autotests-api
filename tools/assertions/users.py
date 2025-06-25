from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
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


def assert_user(
    actual: UserSchema,
    expected: UserSchema
):
    """
    Проверяет что поля данных ожидаемого пользователя совпадают с данными фактического пользователя

    :param actual: фактический пользователь
    :param expected: ожидаемый пользователь
    :raises AssertionError: Если хотя-бы одно из полей пользователей не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

def assert_get_user_response(
    create_user_response: CreateUserResponseSchema,
    get_user_response: GetUserResponseSchema
):
    """
    Проверяет что ответ на создание пользователя совпадает с ответом на получение пользователя
    :param create_user_response: Ответ на создание пользователя, внутри вложенный UserSchema
    :param get_user_response: Ответ на получение пользователя, внутри вложенный UserSchema
    :raises AssertionError: Если ответы не совпадают по данным
    """
    assert_user(create_user_response.user, get_user_response.user)
