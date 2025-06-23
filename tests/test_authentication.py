from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from http import HTTPStatus
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    public_users_client = get_public_users_client()
    authentification_users_client = get_authentification_client()

    create_request = CreateUserRequestSchema()
    create_response = public_users_client.create_user(create_request)
    login_request = LoginRequestSchema(
        email=create_request.email,
        password=create_request.password
    )
    login_response = authentification_users_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(instance=login_response.json(), schema=login_response_data.model_json_schema())


