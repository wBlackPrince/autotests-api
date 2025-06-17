from clients.courses.courses_client import get_courses_client, CreateCourseResponseDict, CreateCourseRequestDict
from clients.excersises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_httpx_builder import AuthentificationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email, get_random_password


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email = get_random_email(),
    password = get_random_password(),
    firstName = 'Eduard',
    middleName = '...',
    lastName = 'Nikitin'
)


create_user_response = public_users_client.create_user(create_user_request)

print(f"Данные запроса на создание пользователя: {create_user_response}")


authentification_user = AuthentificationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"]
)

files_client = get_files_client(user = authentification_user)
courses_client = get_courses_client(user = authentification_user)
exercises_client = get_exercises_client(user = authentification_user)



create_file_request = CreateFileRequestDict(
    filename = "world_map.png",
    directory = "files",
    upload_file = "test_data/files/_BIOMES_map.png"
)

create_file_response = files_client.create_file(request = create_file_request)
print(f"Данные запроса на создание файла", create_file_response)



create_course_request = CreateCourseRequestDict(
    title = 'MyThirdCourse',
    maxScore = 1000,
    minScore = 0,
    description = 'nothing',
    estimatedTime = "100",
    previewFileId = create_file_response["file"]["id"],
    createdByUserId = create_user_response["user"]["id"]
)

create_course_response = courses_client.create_course(request = create_course_request)
print(f"Данные запроса на создание курса", create_course_response)



create_exercise_request = CreateExerciseRequestDict(
    title = 'Увлекательная география',
    courseId = create_course_response["course"]["id"],
    maxScore = 10,
    minScore = 0,
    orderIndex = 0,
    description = '...',
    estimatedTime = '10'
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f"Данные запроса на создание урока", create_exercise_response)





