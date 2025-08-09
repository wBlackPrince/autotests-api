import allure


@allure.step("Building API client")
def build_api_client():
    with allure.step("Getting user authentification"):
        ...

    with allure.step("Creating api client"):
        ...

@allure.step("Creating course with {title}")
def create_course(title: str):
    ...

@allure.step("Deleting course")
def delete_course():
    ...

def test_feature():
    build_api_client()
    create_course(title="Pytest")
    create_course(title="Pydantic")
    delete_course()