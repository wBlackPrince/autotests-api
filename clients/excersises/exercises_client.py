from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response
from clients.private_httpx_builder import AuthentificationUserDict, get_private_httpx_client



class Exercise(TypedDict):
    '''
    Описание структуры урока
    '''
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExerciseResponseDict(TypedDict):
    '''
    Описание структуры запроса на получение урока
    '''
    exercise: Exercise


class GetExercisesRequestDict(TypedDict):
    '''
    Описание структуры запроса для получения списка уроков у курса
    '''
    courseId: str


class GetExercisesResponseDict(TypedDict):
    '''
    Описание структуры запроса на получение списка уроков
    '''
    exercises: list[Exercise]


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


class CreateExerciseResponseDict(TypedDict):
    '''
    Описание структуры запроса на создание урока
    '''
    exercise: Exercise


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

class UpdateExerciseResponseDict(TypedDict):
    '''
    Описание структуры запроса на обновление урока
    '''
    exercise: Exercise




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
        return self.get("api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод получения урока у курса

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.get(f"api/v1/exercises/{exercise_id}")


    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        '''
        Метод создания нового урока

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.post("api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        '''
        Метод обновления урока

        :param exercise_id: Идентификатор урока
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.patch(f"api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод удаления урока

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.delete(f"api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesRequestDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthentificationUserDict) -> ExercisesClient:
    '''
    Метод возвращающий объект ExercisesClient
    :param user: Словарь с email, password
    :return: объект класса ExercisesClient
    '''
    return ExercisesClient(client=get_private_httpx_client(user))