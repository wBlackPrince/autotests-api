from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response



class UpdateExerciseRequestDict(TypedDict):
    '''
    Описание структуры запроса на обновление урока
    '''
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class CreateExerciseRequestDict(TypedDict):
    '''
    Описание структуры запроса на создание урока
    '''
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesRequestDict(TypedDict):
    '''
    Описание структуры запроса для получения списка уроков у курса
    '''
    course_id: str


class ExercisesClient(APIClient):
    '''
    Клиент для работы с api/v1/exercises
    '''

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        '''
        Метод получения списка уроков у курса

        :param query: Словарь с course_id
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.get(
            f"api/v1/exercises",
                params = query
        )

    def get_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод получения урока у курса

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.get(f"api/v1/exercises/{exercise_id}")


    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        '''
        Метод создания нового урока

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.post(
            f"api/v1/exercises",
                json = request
        )


    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        '''
        Метод обновления урока

        :param exercise_id: Идентификатор урока
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.patch(
            f"api/v1/exercises/{exercise_id}",
                json = request
        )


    def delete_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод удаления урока

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.client.delete(f"api/v1/exercises/{exercise_id}")