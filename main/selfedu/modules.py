# import os
# import random as rnd
# задали псевдоним для модуля random через ключевое слово as

# from random import randint, shuffle
# импорт только определённых методов из модуля

# from random import *
# импорт всех методов из модуля random (* - все)

# import os
# import os as my

import libs


# print(os.getcwd())  # C:\apps\Python3\studying_Python\main\selfedu
# print(rnd.randint(1, 100))

# print(randint(1, 100))  # 49

# lst = [1, 2, 3, 4, 5]
# shuffle(lst)
# print(lst)  # [3, 4, 2, 1, 5]

print(libs.get_count('hello', 'l'))  # 2
print(libs.get_length('hello'))  # 5



