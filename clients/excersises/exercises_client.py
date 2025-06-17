from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response
from clients.private_httpx_builder import AuthentificationUserDict, get_private_httpx_client


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

class Exercise(TypedDict):
    '''
    Описание структуры урока
    '''
    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class GetExercisesResponseDict:
    '''
    Описание структуры запроса на получение списка уроков
    '''
    exercises: list[Exercise]


class CreateExerciseResponseDict:
    '''
    Описание структуры запроса на создание урока
    '''
    exercise: Exercise

class UpdateExerciseResponseDict:
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
        return self.get(
            "api/v1/exercises",
                params = query
        )

    def get_exercises(self, query: GetExercisesRequestDict) -> GetExercisesResponseDict:
        '''
        Метод получения списка уроков у курса, использует низкоуровневый метод получения списка уроков

        :param query: Словарь с course_id
        :return: Словарь со списком exercises
        '''
        return self.get_exercises_api(query= query).json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод получения урока у курса

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.get(f"api/v1/exercises/{exercise_id}")


    def get_exercise(self, exercise_id: str) -> Exercise:
        '''
        Метод получения данных об уроке, использует низкоуровневый метод получения урока

        :param exercise_id: Идентификатор урока
        :return: Словарь с данными об уроке
        '''
        return self.get_exercise_api(exercise_id = exercise_id).json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        '''
        Метод создания нового урока

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.post(
            "api/v1/exercises",
                json = request
        )

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        '''
        Метод создания урока, использует низкоуровневый метод создания урока

        :param request:
        :return: Словарь с данными об уроке
        '''
        return self.create_exercise_api(request = request).json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        '''
        Метод обновления урока

        :param exercise_id: Идентификатор урока
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.patch(
            f"api/v1/exercises/{exercise_id}",
                json = request
        )

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        '''
         Метод обновления урока, использует низкоуровневый метод обновления урока

        :param exercise_id: идентификатор урока
        :param request: словарь с новыми данными об уроке
        :return: Словарь с данными об уроке
        '''
        return self.update_exercise_api(
            exercise_id = exercise_id,
            request = request
        ).json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        '''
        Метод удаления урока

        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        '''
        return self.delete(f"api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthentificationUserDict) -> ExercisesClient:
    '''
    Метод возвращающий объект ExercisesClient
    :param user: Словарь с email, password
    :return: объект класса ExercisesClient
    '''
    return ExercisesClient(client = get_private_httpx_client(user))