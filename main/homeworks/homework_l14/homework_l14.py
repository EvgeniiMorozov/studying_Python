from collections import Counter
from re import IGNORECASE
from re import findall
from typing import Any


# Решить задачи, выложить .py файл с решениями на github. В личный кабинет прикрепить .txt файл с ссылкой на профиль.


# Задача 1. Найти количество различных элементов массива. Пример: для [1 4 5 1 1 3] ответ 4.
def count_unique_elems(arr: list[Any]) -> int:
    return len(set(arr))


# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
def get_10_popular_password(file: str) -> Any:
    passwords = []  # в этот список будем "складывать" пароли
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            if len(line.strip("\n")) != 0:
                passwords.append(''.join(findall(r'[@]\w+[.]\w{2,3}[;](.+)$', line, flags=IGNORECASE)))

    return print(f'Десятка часто встречающихся паролей:\n{Counter(passwords).most_common(10)}')


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
def censor_link(string: str) -> str:
    pass


# Здесь писать тесты для функций с решениями
def main():
    # Задача 1.
    arrays = [
        [1, 4, 5, 1, 1, 3],
        [1, 3, 'aaa', 5, 'gg', 1, 3, 2, 2]
    ]
    for arr in arrays:
        print(count_unique_elems(arr))

    # Задача 2.
    get_10_popular_password('pwd.txt')


if __name__ == '__main__':
    main()
