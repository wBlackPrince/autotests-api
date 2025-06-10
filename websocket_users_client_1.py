import asyncio
import websockets

async def async_input():
    return await asyncio.get_event_loop().run_in_executor(None, input)

async def receive_message(websocket):
    try:
        response = await websocket.recv()
        print(response)
    except:
        print('Что-то не так')

async def send_message(websocket):
    try:
        my_message = await async_input()
        await websocket.send(my_message)
    except:
        print('Что-то не так')


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

        while True:
            await asyncio.gather(send_message(websocket), receive_message(websocket))

asyncio.run(client())