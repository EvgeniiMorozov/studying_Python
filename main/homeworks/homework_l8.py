# Полезная статья про функциональный подход (в нескольких частях):
# https://medium.com/devschacht/charles-scalfani-so-you-want-to-be-a-functional-programmer-part-1-6ef98e90d58d


# Задача 1. Решить функциональным подходом
# Пользователь вводит количество недель, месяцев, лет и
# получает количество дней за это время. Считать, что в месяце 30 дней.


# Задача 2. Решить функциональным подходом
# Даны два трехзначных числа. Получите новое число присоединением второго
# числа справа к первому без последних цифр у каждого. Например, 123 и 456 Ответ: 1245


# Задача 3. Реализуйте функцию get_time, которая извлекает из переданного текста
# строку времени в формате ЧЧ:ММ:СС (время там написано именно таким образом).


# Задача 4. Реализуйте функцию get_sign, которая извлекает из переданного текста строку
# номерного знака автомобиля (РФ).
from re import findall


# Задача 1
def get_days(weeks: int, months: int, years: int) -> None:

    def _get_days_from_weeks(week: int) -> int:
        return week * 7

    def _get_days_from_months(month: int) -> int:
        return month * 30

    def _get_months_from_years(year: int) -> int:
        return year * 12

    result = (_get_days_from_weeks(weeks) + _get_days_from_months(months) +
              _get_days_from_months(_get_months_from_years(years)))

    return print(f'Недель: {weeks} | Месяцев: {months} | Лет: {years}\nДней: {result}')


# Задача 2
def splice_nums(number_1: int, number_2: int) -> int:
    def _del_last_digit(num: int) -> int:
        return num // 10
    return int(str(_del_last_digit(number_1)) + str(_del_last_digit(number_2)))


# Задача 3
def get_time(string: str) -> str:
    # Результат будем отдавать в виде строки
    return (findall(r'\d{2}[:]\d{2}[:]\d{2}', string))[0]


# Задача 4
def get_sign(string: str) -> str:
    res = findall(r'[ ]?[\w\D]{1}[ ]?\d{3}[ ]?[\w\D]{2}[ ]?\d{2,3}[ ]?', string)
    return str(res)


def main():
    # Задача 1
    # get_days(2, 3, 4)

    # Задача 2
    # print(splice_nums(123, 456))
    # print(splice_nums(999, 111))
    # print(splice_nums(100, 500))

    # Задача 3
    string = '1232453 2656d fgfghdfg7578 868678 12:23:41 ds fv rgh4534 23 34 23 435'
    print(get_time(string))

    # Задача 4
    numbers = [
        'ц123ук45',
        'ц 123 ук 45',
        'ц 123 ук 456',
        'ц123ук456',
    ]
    for number in numbers:
        print(get_sign(number))


if __name__ == '__main__':
    main()
