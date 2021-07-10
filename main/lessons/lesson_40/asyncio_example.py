import asyncio
import time

import aiohttp
import requests


def write_image(data, name):
    with open(f"images/{name}.jpg", "wb") as f:
        f.write(data)


async def fetch_content(url, session):
    async with session.get(url) as response:
        data = await response.read()
        write_image(data, response.url.name)


async def main():
    url = "https://loremflickr.com/1920/1080"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


def sync_main():
    url = "https://loremflickr.com/1920/1080"

    for i in range(10):
        print(f"Картинка {i} качается")
        data = requests.get(url).content
        write_image(data, i)


if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # sync_main()

    end_time = time.time()

    print(f"{end_time - start_time}")
