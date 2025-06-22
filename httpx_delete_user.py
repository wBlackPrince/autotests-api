import httpx
from tools.fakers import fake

payload = {
  "email": fake.email(),
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


delete_user_headers = {
    'Authorization': f"Bearer {login_response_data["token"]["accessToken"]}"
}

delete_user_response = httpx.delete(f"http://127.0.0.1:8000/api/v1/users/{create_response_data["user"]["id"]}",
                                    headers = delete_user_headers)
delete_user_response_data = delete_user_response.json()

print(f"Успешность удаления пользователя: {delete_user_response.status_code}")
print(f"Данные запроса на удаление: {delete_user_response_data}")