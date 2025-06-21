from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_httpx_builder import AuthentificationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import get_random_email, get_random_password

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password=get_random_password(),
    first_name='Eduard',
    middle_name='...',
    last_name='Nikitin'
)

create_user_response = public_users_client.create_user(create_user_request)

print(f"Данные запроса на создание пользователя: {create_user_response}")

authentification_user = AuthentificationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(user=authentification_user)
courses_client = get_courses_client(user=authentification_user)

create_file_request = CreateFileRequestSchema(
    filename="eto.png",
    directory="files",
    upload_file="test_data/files/eto.jpg"
)

create_file_response = files_client.create_file(request=create_file_request)
print(f"Данные запроса на создание файла", create_file_response)
print()

create_course_request = CreateCourseRequestSchema(
    title='MyCourse',
    maxScore=1000,
    minScore=0,
    description='nothing',
    estimatedTime="100",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = courses_client.create_course(request=create_course_request)
print(f"Данные запроса на создание курса", create_course_response)