from timeit import default_timer
import asyncio
import aiohttp

async def load_data(session,delay):
    print(f'Starting {delay} second timer')
    async with session.get (f'https:// httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed{delay}second timer ')
        return text

async def main():
    start_time = default_timer()

    async with aiohttp.ClientSession() as session:
        two_data = asyncio.create_task(load_data(2))
        three_data = asyncio.create_task(load_data(3))

        await asyncio.sleep(1)
        print('Doing other work')

        two_result = await two_task
        three_result = await three_task


