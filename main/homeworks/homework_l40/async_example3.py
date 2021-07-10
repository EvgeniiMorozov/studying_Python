import asyncio
import time

import aiohttp
import requests


def write_image(data, name):
    """Записывает набор байт в файл картинки name в папку images"""
    with open(f'images/{name}', 'wb') as f:
        f.write(data)


async def fetch_content(url, session):
    """
    Пользуется переданной сессией session для того, чтобы сделать get запрос,
    который возвращает картинку в виде набора байт. Эти байты посылаются на запись
    в файл.
    """
    async with session.get(url) as response:  # асинхронный get запрос, возвращающий картинку
        data = await response.read()  # в response записалась картинка в виде набора байт, этот ответ сервера мы и читаем
        write_image(data, response.url.name)  # передаём эти байты в write_image, который создаёт .jpg картинку


async def main():
    url = 'https://loremflickr.com/1920/1080'  # url-адрес, на который будем обращаться
    tasks = []  # список заданий, которые будут выполняться асинхронно

    async with aiohttp.ClientSession() as session:  # Открываем пользовательскую сессию

        # В цикле 10 раз обращаемся по url, который возвращает картинки как байты, после
        # чего записывает эти байты в .jpg файл (это всё внутри fetch_content())
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))  # Создаём задание
            tasks.append(task)  # Добавляем задание в список заданий

        await asyncio.gather(*tasks)  # Запускаем все задания. Они будут исполняться асинхронно


def sync_main():
    """
    Эта функция в цикле делает 10 get запросов к url, затем полученный набор байтов
    записываем в .jpg файл.
    """
    url = 'https://loremflickr.com/1920/1080'
    for i in range(10):
        response = requests.get(url).content  # get запрос, который возвращает картинку, как набор байт
        write_image(response, f'{i}.jpg')  # передаём эти байты в write_image, который создаёт .jpg картинку


if __name__ == '__main__':
    start_time = time.time()

    # Запуск асинхронного теста (старый способ, на Windows работает без ошибок)
    loop = asyncio.get_event_loop()  # Создаётся объект цикла событий
    loop.run_until_complete(main())  # Цикл событий запускается, пока main() не закончит свою работу

    # Запуск асинхронного теста (новый способ, но на Windows могут появляться ошибки)
    # Если появляются ошибки, лучше запустить тест способом выше.
    # asyncio.run(main())

    # Запуск синхронного теста (нужен для сравнения)
    # sync_main()

    end_time = time.time()
    print(f'Время: {end_time - start_time} сек.')
