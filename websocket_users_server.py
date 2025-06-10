import websockets
import asyncio
from websockets import ServerConnection

<<<<<<< HEAD
clients = set()
=======
async def echo(webSocket: ServerConnection):
    async for message in webSocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"
>>>>>>> fb9f9cddc5033ff90a3a1886e7031ed0ba43c132

async def echo(webSocket: ServerConnection):
    clients.add(webSocket)

    async for message in webSocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"#: {message}"

        for client in clients:
            if client != webSocket:
                await client.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен по адресу ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())