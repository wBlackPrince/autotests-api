from clients.excersises.excersises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    проверяет, что фактические данные упражнения совпадают с ожидаемыми данными упражнения

    :param actual: фактические данные упражнения
    :param expected: ожидаемые данные упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

def assert_get_exercise_response(
        create_exercise_response: CreateExerciseResponseSchema,
        get_exercise_response: GetExerciseResponseSchema
):
    """
    проверяет что данные ответа на создание упражнения совпадают с данными ответа на получение упражнения

    :param create_exercise_response: данные ответа на создание упражнения
    :param get_exercise_response: данные ответа на получение упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(create_exercise_response.exercise, get_exercise_response.exercise)


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Проверяет что данные ответа на создание упражнения совпадают с данными запроса на создание упражнения

    :param request:  данные ответа на создание упражнения
    :param response: данными запроса на создание упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
    проверяет что данные запроса на обновление упражнения совпадают с данными ответа на обновление упражнения
    :param request: данные запроса на обновление упражнения
    :param response: данные ответа на обновление упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")