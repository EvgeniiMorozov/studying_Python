import random


# Task_1

# Дан список, состоящий из произвольного числа направлений
# поворотов («left» и/или «right»). Напишите функцию, которая
# будет принимать этот список и определять, сколько полных оборотов сделано.

# Сделаем допущение, что для полного оборота надо совершить 4 поворота в одну сторону.

def random_turns(n):
    """
    Функция-генератор списка случайных перемещений "left" и "right".

    :param n: количество перемещений.
    :return: список перемещений.
    """
    lst = []
    for i in range(n):
        lst.append('left') if random.randint(0, 1) == 0 else lst.append('right')
    return lst


def counting_rotates(lst):
    count_left = 0
    count_right = 0
    for turn in lst:
        # count_left += 1 if turn == 'left' else count_right += 1
        if turn == 'left':
            count_left += 1
        else:
            count_right += 1
    print(f'Список направлений: {lst}')
    print(f'{count_left=}\t\t{count_right=}')
    print(f'Полных оборотов влево: {count_left // 4}\nПолных оборотов вправо: {count_right // 4}')


def main():
    # Task_1
    lst = random_turns(23)
    counting_rotates(lst)


if __name__ == '__main__':
    main()
