from datetime import date
from datetime import datetime
from datetime import timedelta
import locale

# --- Class date ---
# Возвращает дату.

# today = date.today()
# print(today)  # 2021-02-11
# print(today.day)  # 11
# print(today.month)  # 2
# print(today.year)  # 2021
# print(today.weekday())  # 3 (день недели начинается с нуля - понедельник, сейчас четверг)

# --- Class datetime ---
# Возвращает дату и время.

# now = datetime.now()
# now_2 = datetime.today()

# print(now)  # 2021-02-11 11:09:49.406103
# print(now_2)  # 2021-02-11 11:09:49.406104

# print(now.day)
# print(now.month)
# print(now.year)
# print(now.weekday())
# print(now.hour)
# print(now.minute)
# print(now.second)

# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()])  # чт

# --- strftime() ---
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# now = datetime.now()

# print(now.strftime('%a'))  # Чт
# print(now.strftime('%A'))  # четверг

# print(f'Дата: {now.strftime("%A %d %b %Y")}')  # Дата: четверг 11 фев 2021
# print(f'Время: {now.strftime("%H:%M:%S")}')  # Время: 12:02:14

# print(now.strftime('%c'))  # 11.02.2021 12:03:43
# print(now.strftime('%x'))  # 11.02.2021
# print(now.strftime('%X'))  # 12:03:43

# --- Class timedelta ---

now = datetime.now()
print(now.strftime('%c'))  # Thu Feb 11 12:10:53 2021

d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1)  # 2021-02-12 14:20:53.617463
print(d1.strftime('%c'))  # Fri Feb 12 14:20:53 2021



