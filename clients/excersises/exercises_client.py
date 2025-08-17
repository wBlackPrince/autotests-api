from clients.api_client import APIClient
from httpx import Response
from clients.excersises.excersises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseResponseSchema, \
    UpdateExerciseResponseSchema, CreateExerciseResponseSchema
from clients.private_httpx_builder import AuthentificationUserSchema, get_private_httpx_client
import allure
from tools.routes import ApiRoutes

class ExercisesClient(APIClient):
    '''
    Клиент для работы с api/v1/exercises
    '''

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        '''
        Метод получения списка уроков у курса

        :param query: Словарь с course_id
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.get(f"{ApiRoutes.EXERCISES}", params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод получения урока у курса

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.get(f"{ApiRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        '''
        Метод создания нового урока

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.post(f"{ApiRoutes.EXERCISES}", json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        '''
        Метод обновления урока

        :param exercise_id: Идентификатор урока
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.patch(f"{ApiRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод удаления урока

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.delete(f"{ApiRoutes.EXERCISES}/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthentificationUserSchema) -> ExercisesClient:
    '''
    Метод возвращающий объект ExercisesClient
    :param user: Словарь с email, password
    :return: объект класса ExercisesClient
    '''
    return ExercisesClient(client=get_private_httpx_client(user))