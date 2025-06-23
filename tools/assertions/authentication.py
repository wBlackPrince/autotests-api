from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true

def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет на корректность поля ответа LoginResponseSchema
    :param response: Pydantic модель
    :raises AssertionError: Если хотя бы одно из полей ответа не соответствует критериям
    """
    assert_equal(response.token.token_type, "bearer", "token_type")
    assert_is_true(response.token.access_token, "access_token")
    assert_is_true(response.token.refresh_token, "refresh_token")