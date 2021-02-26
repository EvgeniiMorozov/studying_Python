# Морозов Е.И. группа: Python026

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

from re import IGNORECASE
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


def get_time_1(string: str) -> str:

    if len(findall(r'\d{2}[:]\d{2}[:]\d{2}', string)) != 0:
        # Преобразуем и распакуем полученный список в переменные
        dd, mm, ss = findall(r'\d{2}[:]\d{2}[:]\d{2}', string)[0].split(':')

        if int(dd) < 24 and int(mm) <= 60 and int(ss) <= 60:
            return (findall(r'\d{2}[:]\d{2}[:]\d{2}', string))[0]

        # elif int(dd) == 24 and int(mm) != 0 and int(ss) != 0:
        #     return 'Время не обнаружено!'

        else:
            return 'Время не обнаружено!'


# Задача 4
def get_sign(string: str) -> str:
    res = findall(r'[ ]([А-Яа-яЁё]\d{3}[А-Яа-яЁё]{2}\d{2,3})[ ]', string)
    return res[0] if len(res) != 0 else 'Номеров нет!'


def get_sign_1(string: str) -> str:
    res = findall(r'[ ]([абвгдежзиклмнопрстуфхцчшщэюя]\d{3}[абвгдежзиклмнопрстуфхцчшщэюя]{2}\d{2,3})[ ]',
                  string, flags=IGNORECASE)
    return res[0] if len(res) != 0 else 'Номеров нет!'


def main():
    # Задача 1
    # get_days(2, 3, 4)

    # Задача 2
    # print(splice_nums(123, 456))
    # print(splice_nums(999, 111))
    # print(splice_nums(100, 500))

    # Задача 3
    # string = '1232453 2656d fgfghdfg7578 868678 12:23:41 ds fv rgh4534 23 34 23 435'
    # print(get_time(string))

    # Задача 4
    # numbers = [
    #     'grwtrth ц123ук45 321412345',
    #     '21342134 ц 123 ук 45 asdfgwehg',
    #     '213434fsdcsdfrefg ц 123 ук 456 dfsgewxbxdfs',
    #     '234вапвап234вапвапwedfsdf ц123ук456 wqe213rqwedf',
    # ]
    # for number in numbers:
    #     print(get_sign(number))

    times = [
        '12:23:59',
        '00:23:59',
        '24:00:00',
        '00:00:00',
        '24:00:02',
        '69:96:91',
    ]
    for time in times:
        print(get_time_1(time))

    print('\n==============================\n')

    numbers = [
        'grwtrth ц123ук45 321412345',
        '21342134 ц 123 ук 45 asdfgwehg',
        '213434fsdcsdfrefg ц 123 ук 456 dfsgewxbxdfs',
        '234вапвап234вапвапwedfsdf ц123ук456 wqe213rqwedf',
        'цуаукее Ъ232ЬЁ45 цукакер437768',
        'цуаукее ъ232ыЁ45 цукакер437768'
    ]
    for number in numbers:
        print(get_sign_1(number))


if __name__ == '__main__':
    main()
