from httpx import Client

def get_public_httpx_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout = 100,
        base_url = "http://localhost:8000"
    )