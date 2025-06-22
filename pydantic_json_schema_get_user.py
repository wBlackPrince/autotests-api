from clients.private_httpx_builder import AuthentificationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
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
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

print(f"Данные запроса на создание пользователя: {create_user_response}")


authentification_user = AuthentificationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentification_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

validate_json_schema(get_user_response.json(), GetUserResponseSchema.model_json_schema())
print(f"Данные запроса на создание пользователя: {get_user_response}")