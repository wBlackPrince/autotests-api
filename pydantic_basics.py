'''
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}

{
  "course": {
	  "id": "string",
	  "title": "string",
	  "maxScore": 0,
	  "minScore": 0,
	  "description": "string",
	  "estimatedTime": "string",
	}
}
'''

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr
from pydantic.alias_generators import to_camel
import uuid

class FileSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def user_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    description: str = "Playwright course"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime",default="two weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")



# инициализация модели по умолчанию

course_default_model = CourseSchema(
    previewFile = FileSchema(
        filename="preview.png",
        directory="images",
        url="http://localhost:8000"
    ),
    createdByUser = UserSchema(
        email = "mast@gmail.com",
        lastName = "Nikitin",
        firstName = "Eduard",
        middleName = " "
    )
)

print(course_default_model.model_dump_json())
print()

# инициализация модели с помощью словаря

course_dict = {
    "previewFile": {
        "filename": "preview.png",
        "directory": "images",
        "url": "http://localhost:8000"
    },
    "createdByUser": {
        "email": "mast@gmail.com",
        "lastName": "Nikitin",
        "firstName": "Eduard",
        "middleName": " "
    }
}

course_model_dict = CourseSchema(**course_dict)

print(course_model_dict.model_dump())
print()


course_json = '''
{
    "id": "11111",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "filename": "preview.png", 
        "directory": "images",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "2 week",
    "createdByUser": {
        "email": "mast@gmail.com",
        "lastName": "Nikitin",
        "firstName": "Eduard",
        "middleName": " "
    }
}
'''

course_json_model = CourseSchema.model_validate_json(course_json)
print(course_json_model.model_dump(by_alias=True))
print()

print(course_default_model.created_by_user.user_name)