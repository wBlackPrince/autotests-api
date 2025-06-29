from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что данные ответа на создание файла совпадают с данными запроса на создание файла

    :param request: Исходный запрос на создание файла
    :param response:  Ответ API с данными файла
    :raises AssertionError: Если хотя бы одно из полей ответа не совпадает с полем из запроса
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет что фактические данные файла совпадают с данными ожидаемого файла

    :param actual: Фактический файл
    :param expected: Ожидаемый файл
    :raises AssertionError: Если хотя бы одно из полей ожидаемого файла не совпадает с полем фактического файла
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")

def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Проверяет, что данные ответа на создание файла совпадают с данными ответа на получение файла

    :param get_file_response: Файл полученный GET-запросов
    :param create_file_response: Файл полученный в результате POST-запроса на создание
    :raises AssertionError: Если хотя бы одно из полей ответа на создание файла не совпадает с полями ответа на получение файла
    """
    assert_file(get_file_response.file, create_file_response.file)

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(details="File not found")

    assert_internal_error_response(actual, expected)