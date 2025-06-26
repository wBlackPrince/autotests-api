import pytest
from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient

@pytest.fixture
def authentication_client() -> AuthentificationClient:
    return get_authentification_client()

