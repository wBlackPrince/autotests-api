from allure_commons.types import Severity

from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest
import allure


@pytest.mark.authentication
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Login with correct email and password")
    def test_login(self, authentication_client: AuthentificationClient, function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
