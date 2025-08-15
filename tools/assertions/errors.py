from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет что поля полученной ошибки совпадают с полями ожидаемой ошибки
    :param actual: полученная ошибка
    :param expected: ожидаемая ошибка
    :raises AssertionError: Если хотя бы значения одного поля не совпадают
    """

    logger.info("Check validation error")

    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")

@allure.step("Check validation error response")
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    Проверяет, что количество ожидаемых и фактических ошибок совпадают, а
    также проверяет, что все поля полученных и фактических ошибок совпадают между собой

    :param actual:
    :param expected:
    :return:
    """

    logger.info("Check validation error response")

    assert_length(actual.details, expected.details, "details")

    assert actual.details == expected.details

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """

    logger.info("Check internal error response")

    assert_equal(actual.details, expected.details, "details")

