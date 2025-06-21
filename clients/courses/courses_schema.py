from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    '''
    Структура данных курса
    '''
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class GetCoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str

class CreateCourseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на создание курса
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str = Field(alias="description")
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    '''
    Структура ответа на создание курса
    '''
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    '''
    Описание структуры запроса на обновление курса
    '''
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateCourseResponseSchema(BaseModel):
    '''
    Структура ответа на обновление курса
    '''
    course: CourseSchema
