from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserSchema(BaseModel):
    '''
    Структура json-данных пользователя
    '''
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    last_name: str = Field(alias="lastName")

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа (а именно json-данных этого ответа) на получения пользователя
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel):
    '''
    Структура запроса для создания нового пользователя
    '''
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    last_name: str = Field(alias="lastName")

class CreateUserResponseSchema(BaseModel):
    '''
    Структура ответа на создание пользователя
    '''
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")
    last_name: str | None = Field(alias="lastName")

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление пользователя.
    """
    user: UserSchema
