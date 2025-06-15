import httpx
from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "12345",
  "lastName": "Nikitin",
  "firstName": "Eduard",
  "middleName": " "
}


create_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=payload)
create_response_data = create_response.json()

print("Статус запроса на создание пользователя: ", create_response.status_code)
print("Данные нового пользователя: ", create_response_data)



login_payload = {
  "email": create_response_data["user"]["email"],
  "password": "12345"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json = login_payload)
login_response_data = login_response.json()

print(f"Успешность получения токена доступа: {login_response.status_code}")
print(f"Токен доступа: {login_response_data["token"]["accessToken"]}")



get_user_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}
get_user_response = httpx.get(f"http://127.0.0.1:8000/api/v1/users/{create_response_data["user"]["id"]}",
                              headers = get_user_headers)
get_user_response_data = get_user_response.json()

print(f"Успешность получения пользователя: {get_user_response.status_code}")
print(f"Данные запроса на получение пользователя: {get_user_response_data}")
