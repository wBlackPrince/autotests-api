from pydantic import BaseModel, Field

class TokenSchema(BaseModel):
    """
    Описание токена, который содержится внутри ответа на аутентификацию
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа на аутентификацию.
    """
    token: TokenSchema

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")