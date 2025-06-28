from pydantic import BaseModel

from clients.excersises.excersises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from clients.excersises.exercises_client import ExercisesClient, get_exercises_client
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
import pytest


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
    function_course: CourseFixture,
    exercises_client: ExercisesClient
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)
    response = exercises_client.create_exercise(request)

    return ExerciseFixture(request=request, response=response)