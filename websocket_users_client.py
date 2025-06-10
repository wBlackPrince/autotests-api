import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Привет, сервер!")

        for i in range(5):
            response = await websocket.recv()
            print(response)

asyncio.run(client())