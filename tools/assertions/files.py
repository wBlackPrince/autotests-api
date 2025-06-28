from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal


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
    :return:
    """
    assert_file(get_file_response.file, create_file_response.file)
