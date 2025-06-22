from clients.private_httpx_builder import AuthentificationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(create_user_request)

print(f"Данные запроса на создание пользователя: {create_user_response}")

authentification_user = AuthentificationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentification_user)

get_user_response = private_users_client.get_user(create_user_response.user.id)

print(f"Данные запроса на получение пользователя: {get_user_response}")