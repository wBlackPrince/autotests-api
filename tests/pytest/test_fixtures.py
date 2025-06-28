import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def users_client(settings):
    print("[FUNCTION] создаем API на каждый автотест")

class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_can_create_course(self, settings, user, users_client):
        ...

class TestAccountFlow:
    def test_user_account(self, user, settings, users_client):
        ...

# @pytest.fixture
# def user_data():
#     print("Создаем пользователя для теста (setup)")
#     yield {"username": "test_user", "email": "test@example.com"}
#     print("Удаляем пользователя после теста (teardown)")
#
# def test_user_email(user_data: dict):
#     assert user_data["email"] == "test@example.com"
#
# def test_user_username(user_data: dict):
#     assert user_data["username"] == "test_user"