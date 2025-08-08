import httpx
from tools.fakers import fake

# payload = {
#   "email": fake.email(),
#   "password": "12345",
#   "lastName": "Nikitin",
#   "firstName": "Eduard",
#   "middleName": " "
# }
#
#
# response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=payload)
# print(response.status_code)
# print(response.json())




user_id = "f178390o4"

create_request = {
    "name": "Eduard",
    "lastName": "Nikitin",
    "middleName": "Anatolyevich"
}

create_response = httpx.post(f"https://localhost:7222/user/{user_id}", json=create_request, verify=False)
print(create_response.status_code)
print(create_response.json())


get_response = httpx.get(f"https://localhost:7222/user/{user_id}", verify=False)
print(get_response.status_code)
print(get_response.json())

# update_request = {
#     "name": "Eduard",
#     "lastName": "Nikitin",
#     "middleName": "Anatolievich"
# }
#
# update_response = httpx.put(f"https://localhost:7222/user/{user_id}", json=update_request, verify=False)
# print(update_response.status_code)
#
#
# delete_response = httpx.delete(f"https://localhost:7222/user/{user_id}", verify=False)
# print(delete_response.status_code)