import websockets
import asyncio
from websockets import ServerConnection

async def echo(webSocket: ServerConnection):
    async for message in webSocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"

        for i in range(5):
            await webSocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен по адресу ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())