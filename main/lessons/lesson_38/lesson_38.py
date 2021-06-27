# Занятие 38. Параллельное программирование. Многопроцессность
import threading
import concurrent.futures
import multiprocessing
import time


# def factorial(start, end):
#     fact = 1
#     for n in range(start, end+1):
#         fact *= n
#     return fact


# def f():
#     print('f done!')


X = 0


# def increment(n, q):
#     # global X
#     num = q.get()
#     print(f'Процесс {multiprocessing.current_process().name} начал работу! {num=}')
#     for _ in range(n):
#         num += 1
#         if _ == 5_000_000:
#             q.put(1)
#     q.put(num)
#     print(f'Процесс {multiprocessing.current_process().name} закончил работу! {num=}')

# def pipe(data, shared_memory):
#     shared_memory.send(data)
#     shared_memory.close()
#
#
# def read_pipe(shared_memory):
#     print(f'Процесс {multiprocessing.current_process().name} получил {shared_memory.recv()}')


def shared_memory(arr, val, data_value, data_arr):
    print(f'Процесс {multiprocessing.current_process().name} увидел {val.value} {arr[:]}')
    val.value = data_value
    arr[0] = data_arr


def shared_manager(dct, lst, data):
    lst[0] = data
    dct[0] = data


def main():

    # t1 = threading.Thread(target=factorial, args=(1, 100000))
    # t2 = threading.Thread(target=factorial, args=(100001, 200000))

    # t1 = threading.Thread(target=factorial, args=(1, 50000))
    # t2 = threading.Thread(target=factorial, args=(50001, 100000))
    # t3 = threading.Thread(target=factorial, args=(100001, 150000))
    # t4 = threading.Thread(target=factorial, args=(150001, 200000))

    # p1 = multiprocessing.Process(target=factorial, args=(1, 100000))
    # p2 = multiprocessing.Process(target=factorial, args=(100001, 200000))

    # p1 = multiprocessing.Process(target=f)
    # p2 = multiprocessing.Process(target=f)

    # q = multiprocessing.Queue()
    # q.put(0)
    # p1 = multiprocessing.Process(target=increment, args=(100_000_000, q), name='Процесс 1')
    # p2 = multiprocessing.Process(target=increment, args=(100_000_000, q), name='Процесс 2')

    # parent, child = multiprocessing.Pipe()
    # p1 = multiprocessing.Process(target=pipe, args=([1, '1', None, ()], parent), name='Процесс 1')
    # p2 = multiprocessing.Process(target=read_pipe, args=({1: 1, 2: 2, 3: 3}, child), name='Процесс 2')
    # p3 = multiprocessing.Process(target=read_pipe, args=({1: 1, 2: 2, 3: 3}, child), name='Процесс 3')

    # num = multiprocessing.Value('i')
    # arr = multiprocessing.Array('i', range(10))
    # print(f'Главный процесс увидел {num.value} {arr[:]}')
    # p1 = multiprocessing.Process(target=shared_memory, args=(arr, num, 101, 1001), name='Процесс 1')
    # p2 = multiprocessing.Process(target=shared_memory, args=(arr, num, 102, 1002), name='Процесс 2')

    with multiprocessing.Manager() as manager:
        lst = manager.list(range(10))
        dct = manager.dict()

        p1 = multiprocessing.Process(target=shared_manager, args=(dct, lst, 10001), name='Процесс 1')
        p2 = multiprocessing.Process(target=shared_manager, args=(dct, lst, 20002), name='Процесс 2')

        print(f'Результат: {dct}, {lst}')

    start_time = time.time()

    # result = factorial(1, 200000)  # ~ 21 сек
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()  # 2 потока - 9 sec

    # 4 потока - 4.4 сек
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    #
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()

    # 5.9 sec
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # запуск без join()
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()

    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    end_time = time.time()
    print(f'Время исполнения: {end_time - start_time} сек')
    # print(f'Результат: {result}')
    # print(f'Результат: {parent.recv()}, {child.recv()}')
    # print(f'Результат: {dct.items()}, {lst[:]}')


if __name__ == '__main__':
    main()
