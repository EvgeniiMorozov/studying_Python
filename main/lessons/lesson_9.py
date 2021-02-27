# Сортировка слиянием.
def merge_sort(arr):
    # определяем базовый случай
    if len(arr) == 1:
        return arr

    # указатель на середину списка
    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    # отсортированный подсписок
    sorted_list = []

    # указатели на текущую позицию сортируемого элемента подсписка
    left_index = 0
    right_index = 0

    # длины подсписков (нужны, чтобы знать в какой момент остановить сортировку подсписка)
    left_length = len(left_arr)
    right_length = len(right_arr)

    for i in range(left_length + right_length):
        # работаем в начале с элементами, которые не в конце подсписков
        if left_index < left_length and right_index < right_length:
            # сравнение первых элементов подсписков, если один меньше другого, то он добавляется в sorted_list
            if left_arr[left_index] <= right_arr[right_index]:
                sorted_list.append(left_arr[left_index])
                left_index += 1
            else:
                sorted_list.append(right_arr[right_index])
                right_index += 1
        # работаем с элементами, которые в конце подсписков
        # если дошли до конца левого списка
        elif left_index == left_length:
            sorted_list.append(right_arr[right_index])
            right_index += 1

        # если дошли до конца правого списка
        elif right_index == right_length:
            sorted_list.append((left_arr[left_index]))
            left_index += 1

    return sorted_list


# Множества.


def main():
    # Сортировка слиянием.
    # arr = [7, 5, 4, 2, 1, 0, 9]
    # print(merge_sort(arr))  # [0, 1, 2, 4, 5, 7, 9]

    # Множества.
    # nums_set = {1, 2, 3, 4, 5, 6}
    # print(nums_set)
    #
    # nums_set = {'one', 'two', 'three', 'four', 'five', 'six'}
    # print(nums_set)
    # print(type(nums_set))

    # nums_set = {'one', 'two', 'three', 'four', 'five', 'six', 1, (1, 2, 3), [1, 2, 3]}  # TypeError: unhashable type: 'list'
    # множество не может содержать изменяемые типы данных
    # nums_set = {'one', 'two', 'three', 'four', 'five', 'six', 1, (1, 2, 3)}
    # print(nums_set)

    # nums_set = {'one', 'two', 'three', 'four', 'five', 'six', 1, (1, 2, 3), 1, 2, 2, 2, 3, 3, 3, 3}
    # # множества удаляют дубликаты на моменте его создания
    # print(nums_set)  # {1, 'six', 3, 2, (1, 2, 3), 'one', 'three', 'five', 'four', 'two'}

    # nums_set = {}
    # print(type(nums_set))  # <class 'dict'>
    # # пустое множество создают так:
    # nums_set = set()

    # доступ к элементам множества
    # nums_set = {'one', 'two', 'three', 'four', 'five', 'six', 1, (1, 2, 3)}
    # for el in nums_set:
    #     print(el)
    # print('one' in nums_set)  # True
    # print('one1' in nums_set)  # False

    # Добавление элементов во множество
    # nums_set = set()
    # print(nums_set)  # set()
    # nums_set.add(1)
    # print(nums_set)  # {1}

    # удаление элементов из множества
    # nums_set = {1, 2, 3, 4, 5, 6, 7}
    # print(nums_set)
    # три варианта удаления
    # 1 - pop()
    # nums_set.pop()
    # print(nums_set)

    # 2 - remove()
    # nums_set = {'one', 'two', 'three', 'four', 'five', 'six'}
    # nums_set.remove('two')
    # print(nums_set)

    # 3 - discard()
    # nums_set.discard('two')
    # nums_set.discard('two1')
    # print(nums_set)

    # очистка множества - clear()
    # nums_set.clear()
    # print(nums_set)  # set()

    # Операции над множествами
    #
    # recipe1 = {'мука', 'масло', 'яйца', 'майонез'}
    # recipe2 = {'колбаса', 'лук', 'яйца', 'перец'}

    # объединение - union()
    # all_ingredients = recipe1.union(recipe2)
    # print(all_ingredients)
    #
    # print(recipe1 | recipe2)

    # пересечение - intersection() или & (амперсанд)
    # print(recipe1 & recipe2)  # {'яйца'}
    # print(recipe1.intersection(recipe2))  # {'яйца'}

    # разность между множествами
    # print(recipe1.difference(recipe2))  # {'мука', 'майонез', 'масло'}
    # print(recipe1 - recipe2)  # {'мука', 'майонез', 'масло'}

    # симметричная разность (все эл-ты множеств, кроме их пересечения)
    # print(recipe1.symmetric_difference(recipe2))  # {'перец', 'колбаса', 'мука', 'масло', 'майонез', 'лук'}
    # print(recipe1 ^ recipe2)

    # Сравнение множеств (c точки зрения подмножеств и надмножеств)
    # print(recipe1 > recipe2)  # False
    # nums_set1 = {1, 2, 3, 4, 5}
    # nums_set2 = {1, 2, 3}
    # print(nums_set1 > nums_set2)  # True
    # nums_set2 является подмножеством nums_set1

    # Методы множеств
    # copy() - делает копию множества (как новый объект)
    # nums_set1 = {1, 2, 3, 4, 5}
    # nums_set2 = nums_set1.copy()
    # nums_set3 = nums_set1
    # print(id(nums_set1))
    # print(id(nums_set3))
    # print(id(nums_set2))
    # print(nums_set2)

    # isdisjoint() - проверяет, содержатся ли пересечения
    nums_set1 = {1, 2, 3, 4, 5}
    nums_set2 = {1, 2}
    nums_set3 = {6, 7, 8}
    print(nums_set1.isdisjoint(nums_set2))  # False
    print(nums_set3.isdisjoint(nums_set1))  # True

    # frozenset - замороженные множества
    frz = frozenset([1, 2, 3])


if __name__ == '__main__':
    main()
