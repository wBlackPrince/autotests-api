from pydantic import BaseModel, Field, EmailStr
import uuid

class UserSchema(BaseModel):
    '''
    Структура данных пользователя
    '''
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    '''
    Структура запроса для создания нового пользователя
    '''
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    '''
    Структура ответа на создание пользователя
    '''
    user: UserSchema