import httpx
from tools.fakers import get_random_email, get_random_password


payload = {
  "email": get_random_email(),
  "password": get_random_password(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json = payload)
create_user_response_data = create_user_response.json()

print(f"Код запроса на создание пользователя: {create_user_response.status_code}")
print(f"Информация о запросе на создание пользователя: {create_user_response_data}")
print()




login_payload = {
  "email": create_user_response_data['user']['email'],
  "password": payload["password"]
}

login_user_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json = login_payload)
login_user_response_data = login_user_response.json()

print(f"Код запроса на аутентификацию пользователя: {login_user_response.status_code}")
print(f"Полученный токен доступа: {login_user_response_data["token"]["accessToken"]}")
print()




update_payload = {
  "email": payload["email"],
  "lastName": payload["lastName"],
  "firstName": payload["firstName"],
  "middleName": "something"
}

update_headers = {
    'Authorization': f"Bearer {login_user_response_data["token"]["accessToken"]}"
}
update_user_response = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
                                   json = update_payload,
                                   headers = update_headers)
update_user_response_data = update_user_response.json()

print(f"Код запроса на обновление пользователя: {login_user_response.status_code}")
print(f"Данные запроса на обновление: {update_user_response_data}")
print()





# get_user_headers = {
#     "Authorization": f"Bearer {login_user_response_data["token"]["accessToken"]}"
# }
# get_user_response = httpx.get(f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
#                               headers = get_user_headers)
# get_user_response_data = get_user_response.json()
#
# print(f"Успешность получения пользователя: {get_user_response.status_code}")
# print(f"Данные запроса на получение пользователя: {get_user_response_data}")