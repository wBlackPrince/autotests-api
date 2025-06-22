from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake

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

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)

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

    email: EmailStr | None = Field(default_factory=fake.email)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление пользователя.
    """
    user: UserSchema