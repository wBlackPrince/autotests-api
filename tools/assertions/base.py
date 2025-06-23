from typing import Any


def assert_status_code(actual: int, expected: int) -> None:
    '''
    Проверяет, что фактический статус-код совпадает с ожидаемым статус-кодом

    :param actual: Фактический статус-код ответа
    :param expected: Ожидаемый статус-код ответа
    :raises AssertionError: Если статус-коды не совпадают
    '''
    assert actual == expected, (
        "Incorrect response status code."
        f"Expected status code: {expected}"
        f"Actual status code: {actual}"
    )

def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Проверяет что фактическое значение совпадает с ожидаемым
    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Имя проверяемого значение
    :raises AssertionError: Если значения не совпадают
    """
    assert actual == expected, (
        f"Incorrect value {name}."
        f"Expected value: {expected}"
        f"Actual value: {actual}"
    )