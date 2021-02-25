import re

# def f(x):
#     return x**2
#
#
# def sum_n_nums(n):
# #     итеративный вариант решения
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum
#
#     # рекурсивный вариант решения (не хвостовой)
#     if n == 0:
#         return 0
#     return n + sum_n_nums(n-1)

# рекурсивный вариант решения (хвостовой)
# def tail_sum_n_nums(n, sum=0):
#     if n == 0:
#         return sum
#     return tail_sum_n_nums(n-1, sum+n)


# def iter_sum_n_nums(n, sum=0):
#     while True:
#         if n == 0:
#             return sum
#         inner_sum = sum + n
#         n -= 1
#         sum = inner_sum

# Регулярные выражения


def main():
    # Моржовый оператор
    # arr = [1, 2, 3, 4, 5]
    # len_a = len(arr)
    # if len_a > 3:
    #     print(f'Список содержит больше 3х элементов: {len_a}')
    # if (len_a := len(arr)) > 3:
    #     print(f'Список содержит больше 3х элементов: {len_a}')

    # while (len_a := len(arr)) < 10:
    #     print(f"Список содержит меньше десяти элементов: {len_a}")
    #     arr.append(1)

    # без моржа
    # len_a = len(arr)
    # while len_a < 10:
    #     print(f"Список содержит меньше десяти элементов: {len_a}")
    #     arr.append(1)
    #     len_a = len(arr)
    # print(len_a)
    #
    # arr = [y := f(5), y**2, y**3]
    # print(arr)

    # Регулярные выражения
    # string = 'Петя позвонил Саше на номер +(123)456-78-90'

    # match - ищет в начале строки
    # result = re.match('Петя', string)
    # print(result)
    # print(result.group())
    # print(result.start())
    # print(result.end())

    # search - ищет шаблон по всей строке
    # result = re.search('Петя', string)
    # print(result)
    # result = re.search('позвонил', string)
    # print(result)

    # string = 'Петя позвонил позвонил Саше на номер +(123)456-78-90'

    # findall - ищет все вхождения в строке
    # result = re.findall('позвонил', string)
    # print(result)

    # split
    # result = re.split(' ', string)
    # print(result)

    # sub - замена шаблона на новый
    # result = re.sub('позвонил', 'укоротил', string)
    # print(result)

    # compile
    # pattern = re.compile('позвонил')
    # result = pattern.sub('укоротил', string)
    # print(result)

    """
    Операторы регулярных выражений:

    . - один любой символ, кроме новой строки (\n)
    ? - ищем 0 или 1 вхождение шаблона слева
    + - 1 или более вхождений шаблона слева
    * - ищет 0 и более вхождений шаблона слева
    \w - любая цифра или буква (\W - ищем всё, кроме цифры или буквы)
    \d - Любая цифра [0-9] (\D - всё кроме цифры)
    \s - любой пробельный символ (\S - всё кроме пробельного символа)
    \b - граница слова (ищем что-любо с начала строки)
    [...] - ищем один из символов в скобках ([^..] - ищем любой символ, кроме тех, что в скобках)
    \ - экранирование (например: \. - вернёт символ точки)
    ^ и $ - начало и конец строки соответственно
    {n, m} - от n до m вхождений шаблона слева ({, m} - не более m вхождений, {n} - строго n вхождений)
    a | b - оператор ИЛИ, соответсвует a или b
    () - группируют выражение и возвращает найденный текст
    \t, \n, \r - символы табуляции, новой строки и возврата каретки соответственно
    """

    # вернуть первое слово из строки
    string = 'Петя позвонил позвонил Саше на номер +7(123)456-78-90'
    # result = re.findall(r'.', string)
    # print(result)
    # result = re.findall(r'\w', string)
    # print(result)
    # result = re.findall(r'\w+', string)
    # print(result)
    # result = re.findall(r'\w*', string)
    # print(result)
    # result = re.findall(r'^\w+', string)  # эквивалент re.match(r'^\w+', string)
    # print(result)

    # Вернуть домены из списка email-адресов
    # emails = [
    #     'abc@mail1ru',
    #     'ivanov1@yandex.ru',
    #     'anon.im1337@protonmail.com',
    #     'ilya123.ru@gmail.com'
    # ]
    # for mail in emails:
    #     result = re.findall(r'@(\w+\.\w+)', mail)
    #     print(result)

    # извлечь дату из строки
    # string = r'Петя позвал Сашу погулять 21-01-2007, а затем 27.05.2010, а затем 12 08 2011, а затем 20/10/2012, а затем 21\12\2013'
    # result = re.findall(r'\d{2}\W\d{2}\W\d{4}', string)
    # print(result)

    # Извлечь слова, начинающиеся на гласную букву
    # string = 'Забрела Саша в лес, съела яблоко, а потом как закричала: "АУ!"'
    # result = re.findall(r'\w+', string)
    # print(result)
    # result = re.findall(r'[АУЕЁЫЮЭЯИОауеёыюэяио]\w+', string)
    # print(result)
    # glass = "АУЕЁЫЮЭЯИОауеёыюэяио"
    # result = re.findall(r'\b[АУЕЁЫЮЭЯИОауеёыюэяио]\w+', string)
    # result = re.findall(fr'\b[{glass}]\w+', string)
    # print(result)

    # проверить формат телефонного номера
    data = [
        'dfsdfsdfsdf',
        'sdfsdfert3345345',
        '345456456241364567456456',
        '+7(123)456-78-90',
        '81234567890',
        '+71234567890'
    ]
    # for chunk in data:
    #     result = re.findall(r'\+?[78]\(?\d{3}\)?\d{3}-?\d{2}-?\d{2}', chunk)
    #     print(result)

    # презентабельный вид
    # for chunk in data:
    #     number = re.findall(r'\+?[78]\(?\d{3}\)?\d{3}-?\d{2}-?\d{2}', chunk)
    #     if len(number) == 0:
    #         continue
    #     country_code = re.findall(r'\+?([78])\(?\d{3}\)?\d{3}-?\d{2}-?\d{2}', chunk)[0]
    #     city_code = re.findall(r'\+?[78]\(?(\d{3})\)?\d{3}-?\d{2}-?\d{2}', chunk)[0]
    #     num1 = re.findall(r'\+?[78]\(?\d{3}\)?(\d{3})-?\d{2}-?\d{2}', chunk)[0]
    #     num2 = re.findall(r'\+?[78]\(?\d{3}\)?\d{3}-?(\d{2})-?\d{2}', chunk)[0]
    #     num3 = re.findall(r'\+?[78]\(?\d{3}\)?\d{3}-?\d{2}-?(\d{2})', chunk)[0]
    #     print(f'Было: {chunk} | Стало: +{country_code}({city_code}){num1}+{num2}-{num3}')

    # замена с помощью sub
    # Убрать из списка логинов лишние символы
    data = [
        'login',
        'iv\'anov',
        'pe+t+r+ov',
        'va<p style="font-weight: 100px">ХАХА Я ТЕБЯ СЗЛОМАЛ</p>sya'
    ]
    for login in data:
        result = re.sub(r'<.*>|\W', '', login)
        print(result)


if __name__ == '__main__':
    main()
