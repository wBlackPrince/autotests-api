import httpx


login_payload = {
  "email": "myrt@example.com",
  "password": "12345"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json = login_payload)
login_response_data = login_response.json()

print(f"Успешность получения токена доступа: {login_response.status_code}")
print(f"Токен доступа: {login_response_data["token"]["accessToken"]}")

client = httpx.Client(base_url = "http://127.0.0.1:8000",
                      timeout = 100,
                      headers = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"})

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()

print(f"Успешность выполнения GET-запроса: {get_user_me_response.status_code}")
print(f"Данные ответа на GET-запрос: {get_user_me_response_data}")
