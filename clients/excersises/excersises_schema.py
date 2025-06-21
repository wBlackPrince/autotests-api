from pydantic import BaseModel, Field, ConfigDict

class ExerciseSchema(BaseModel):
    '''
    Описание структуры урока
    '''
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExerciseResponseSchema(BaseModel):
    '''
    Описание структуры запроса на получение урока
    '''
    exercise: ExerciseSchema

class GetExercisesRequestSchema(BaseModel):
    '''
    Описание структуры запроса для получения списка уроков у курса
    '''
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="course_id")

class GetExercisesResponseSchema(BaseModel):
    '''
    Описание структуры запроса на получение списка уроков
    '''
    exercises: list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на создание урока
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    '''
    Описание структуры запроса на создание урока
    '''
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на обновление урока
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    maxScore: int | None = Field(alias="maxScore")
    minScore: int | None = Field(alias="minScore")
    orderIndex: int | None = Field(alias="orderIndex")
    description: str | None
    estimatedTime: str | None = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    '''
    Описание структуры запроса на обновление урока
    '''
    exercise: ExerciseSchema