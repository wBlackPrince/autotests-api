from typing import Any, Sized


def assert_status_code(actual: int, expected: int):
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

def assert_equal(actual: Any, expected: Any, name: str):
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

def assert_is_true(actual: Any, name: str):
    """
    Проверяет что фактическое значение истинно
    :param actual: Фактическое значение
    :param name: Название фактического значения
    :raises AssertionError: Если фактическое значение ложно
    """
    assert bool(actual), (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(actual: Sized, expected: Sized, name):
    """
    Проверяет что два объекта имеют одинаковую длину по определенному атрибуту

    :param actual: фактический объект
    :param expected: ожидаемый объект
    :param name: имя атрибута
    :raises AssertionError: Если длины атрибутов объектов не совпадают
    """
    assert len(actual) == len(expected), (
        f"Incorrect object's length {name}"
        f"Expected length {len(expected)}"
        f"Actual length {len(actual)}"
    )