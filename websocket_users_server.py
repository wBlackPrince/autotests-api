import websockets
import asyncio
from websockets import ServerConnection

clients = set()

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