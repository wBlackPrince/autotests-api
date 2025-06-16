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

create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

create_file_data = {
    "filename": "_BIOMES_map.png",
    "directory": "maps"
}

create_file_files = {
    "upload_file": open(f"test_data/files/{create_file_data["filename"]}", "rb")
}

create_file_response = httpx.post("http://127.0.0.1:8000/api/v1/files",
                                  data = create_file_data,
                                  files = create_file_files,
                                  headers = create_file_headers
                                  )
create_file_response_data = create_file_response.json()

print(f"Успешность запроса на передачу файла: {create_file_response.status_code}")
print(f"Данные запроса на передечу файла: {create_file_response_data}")

