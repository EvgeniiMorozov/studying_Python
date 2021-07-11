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

import aiohttp


URL = "https://random-data-api.com/api/phone_number/random_phone_number"


def write_data(data: str, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data + "\n")


if __name__ == '__main__':
    ...
