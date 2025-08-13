from pydantic import BaseModel, Field, HttpUrl
from pydantic import FilePath
from tools.fakers import fake


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath

class FileSchema(BaseModel):
    '''
    Описание файла в структуре оответа на создание файла
    '''
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileResponseSchema(BaseModel):
    '''
    Описание структуры ответа на создание файла
    '''
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    file: FileSchema