from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from clients.users.users_schema import CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password=fake.password(),
    first_name='Eduard',
    middle_name='...',
    last_name='Nikitin'
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


validate_json_schema(create_user_response_json, create_user_response_schema)


print(f"Данные запроса на создание пользователя: {create_user_response}")