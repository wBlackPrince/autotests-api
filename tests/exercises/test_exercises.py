from http import HTTPStatus
import pytest
from clients.excersises.excersises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from clients.excersises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise(request, response_data)

        validate_json_schema(response.json(), CreateExerciseResponseSchema.model_json_schema())

