"""
Дан следующий url:

https://random-data-api.com/api/phone_number/random_phone_number

По этой ссылке генерируется json со случайным номером телефона.
Пример JSON:
{
    "id":3134,
    "uid":"db8ed088-1b70-4a50-a225-476420102c63",
    "phone_number":"506-831-6070 x739",
    "cell_phone":"291.972.8814",
    "cell_phone_in_e164":"+19394790155003"
}

Написать программу, которая асинхронно 500 раз выполняет get запрос
к указанному выше url, извлекает из json данные по ключу "cell_phone",
и записывает его в файл data.txt. Для наглядности, можно сделать так, чтобы
в файл ещё записывался номер задачи. В итоге содержимое файла может выглядеть
как-то так:

Task 0. 768-992-3435
Task 12. 1-365-690-2821
Task 4. 881.569.5793
Task 8. 1-861-958-4949
...

Для этого вам понадобятся следующие библиотеки: asyncio, aiohttp.

Для того, чтобы было проще писать код, дан пример программы (async_example3.py),
которая асинхронно качает несколько картинок. Нужно разобраться, что он делает и
переделать его под данную задачу. Код прокомментирован.
"""

import asyncio
import json
import time

import aiohttp


def write_data(data: str, filename: str):
    """Записывает данные в файл"""
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(data + "\n")


async def fetch_content(url: str, filename: str, session, index: int):
    """
    Пользуясь переданной сессией session делает get-запрос, получает данные в формате
    json, дессериализует их, извлекает из них нужные нам данные и записывает их в файл.
    """
    async with session.get(url) as response:
        data = await response.read()
        data = json.loads(data)
        write_data(f"Task{index}. {data['cell_phone']}", filename)


async def collect_data():
    url = "https://random-data-api.com/api/phone_number/random_phone_number"
    filename = "data.txt"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for index in range(500):
            task = asyncio.create_task(fetch_content(url, filename, session, index))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(collect_data())

    end_time = time.time()
    print(f'Время: {end_time - start_time} сек.')
