from pydantic import BaseModel, Field, HttpUrl

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

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