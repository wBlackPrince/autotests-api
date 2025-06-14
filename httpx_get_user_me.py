import httpx

login_payload = {
  "email": "orototo@example.com",
  "password": "12345"
}

answer_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json = login_payload)
answer_response_data = answer_response.json()

print(f"Данные ответа: {answer_response_data}")
print(f"Код запроса: {answer_response.status_code}")



access_token = answer_response_data["token"]["accessToken"]
get_headers = {"Authorization": f"Bearer {access_token}"}

get_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers = get_headers)
get_response_data = get_response.json()

print(f"Данные ответа: {get_response_data}")
print(f"Код запроса: {get_response.status_code}")