import httpx

def print_twice():
    print()
    print()

'''
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())
print_twice()

data = {
    "title": "new_task",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json = data)
print(response.status_code)
print(response.headers)
print(response.json())
print_twice()

data = {"data": "test_user", "password": "12345"}
response = httpx.post("https://httpbin.org/post", data = data)
print(response.status_code)
print(response.headers)
print(response.json())
print_twice()

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers = headers)
print(response.request.headers)
print(response.json())
print_twice()


params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1", params = params)
print(response.url)
print(response.json())
print_twice()


files = {"file":  ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files = files)

print(response.json())
print_twice()


with httpx.Client() as client:
    response_1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response_1.json())
print(response_2.json())
print_twice()
'''

client = httpx.Client(headers = {"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())
print_twice()

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
    print(response.status_code)
except Exception as exc:
    print(f"Тип ошибки: {type(exc).__name__}")


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.TimeoutException as exc:
    print(f"Запрос выполнялся слишком долго")


