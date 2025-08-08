from allure_commons.types import Severity
from pydantic import EmailStr
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake
import pytest
import allure
from tools.allure.tags import AllureTag

@pytest.mark.users
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
class TestUsers:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    @allure.title("Create user")
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self, email: EmailStr, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(email))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Get user me")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(
            self,
            public_users_client: PublicUsersClient,
            function_user: UserFixture,
            private_users_client: PrivateUsersClient
    ):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(function_user.response, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())