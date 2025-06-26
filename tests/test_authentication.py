from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest


@pytest.mark.authentication
@pytest.mark.regression
def test_login(authentication_client: AuthentificationClient, function_user: UserFixture):
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


