# Сортировки, venv, git.

# Быстрая сортировка (сортировка/метод Хоара).
# Сложность: - в среднем N*logN операций, в худщем случае N^2

def quick_sort(arr):
    # базовый случай выхода из рекурсии
    if len(arr) <= 1:
        return arr

    # точка опоры, центральный элемент массива
    pivot = arr[len(arr) // 2]
    less_arr = []  # список элементов, меньше опорного
    equal_arr = []  # список элементов, которые равны опорному
    greater_arr = []  # список элементов, больше опорного

    # сравниваем элементы и вставляем их в соответсвующий список
    for el in arr:
        if el < pivot:
            less_arr.append(el)
        elif el > pivot:
            greater_arr.append(el)
        else:
            equal_arr.append(el)

    return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

# Virtual Environment (виртуальное окружение) / venv / env.


def main():
    arr = [1, 6, 3, 8, 3, 9, 4, 2, 6, 7]  # pivot - точка опоры
    print(arr)
    print(quick_sort(arr))


if __name__ == '__main__':
    main()
