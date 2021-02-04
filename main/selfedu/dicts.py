# Словари ( dictionary )
"""
Неупорядоченная коллекция с доступом по ключу.
Называют ещё ассоциативными массивами или хэш-таблицами.
"""

# Способы создания

# 1. С помощью литерала

# d = {}
# print(type(d))  # <class 'dict'>

# product1 = {
#     'title': 'Sony',
#     'price': 100
# }
# ключи должны быть заключены в кавычки !!! Значения могут быть разных типов данных.
# print(product1)  # {'title': 'Sony', 'price': 100}

# 2. с помощью конструктора dict

# product2 = dict(title='iPhone', price=110)  # когда мы работаем с именованными аргументами,
# то заключать их в кавычки не нужно.
# print(product2)  # {'title': 'iPhone', 'price': 110}

# 3. создание словаря из списка или кортежа

# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['katy@gmail.com', 'Katy'],
#     ['john@gmail.com', 'John']
# ]
# print(users)  # [['bob@gmail.com', 'Bob'], ['katy@gmail.com', 'Katy'], ['john@gmail.com', 'John']]

# d_users = dict(users)
# print(d_users)  # {'bob@gmail.com': 'Bob', 'katy@gmail.com': 'Katy', 'john@gmail.com': 'John'}

# users_t = (
#     ('bob@gmail.com', 'Bob'),
#     ('katy@gmail.com', 'Katy'),
#     ('john@gmail.com', 'John')
# )
# t_users = dict(users_t)
# print(t_users)  # {'bob@gmail.com': 'Bob', 'katy@gmail.com': 'Katy', 'john@gmail.com': 'John'}

# 4. метод from keys

# product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
# print(product3)  # {'price1': 50, 'price2': 50, 'price3': 50}

# 5. с помощью генератора

nums = {i: i + 1 for i in range(1, 10)}
# print(nums)  # {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}


product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title='iPhone', price=110)

# получение значений

# через ключ

# print(product1['title'])  # Sony
# print(nums['1'])  # KeyError: '1' -  ключ 1 - число, а не строка !!!
# print(nums[1])  # 2

# с помощью метода dict.get('key')

# print(product1['title'])  # Sony
# print(product1.get('title'))  # Sony

# при обращении к несуществующему ключу, get вернет None,
# а обращение через ключ ошибку.
# print(product1['title2'])  # KeyError: 'title2'
# print(product1.get('title2'))  # None
# print(product1.get('title2', 'No key!'))  # No key!  - if no key


# Перебор словаря

# for key in product1:
#     print(f'{key}: {product1[key]}')
# title: Sony
# price: 100

# print(product1.items())  # dict_items([('title', 'Sony'), ('price', 100)])

# for key, value in product1.items():
#     print(key, value)
# title Sony
# price 100

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]
# print(products)
# [{'title': 'Sony', 'price': 100}, {'title': 'iPhone', 'price': 110}, {'title': 'Samsung', 'price': 90}]

# for product in products:
#     print(product['title'], product['price'])
# Sony 100
# iPhone 110
# Samsung 90


