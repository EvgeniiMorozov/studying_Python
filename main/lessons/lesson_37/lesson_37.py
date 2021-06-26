# Занятие 37. Параллельное программирование. Многопоточность
# _thread, threading
# concurrent.futures
import concurrent.futures
import threading
import time


X = 0


def sleeper(sec):
    print(f'Засыпаю на {sec} сек.')
    time.sleep(sec)
    print(f'Проснулись через {sec} сек.')


# def increment(n, lock: threading.Lock):
#     lock.acquire()
#     global X
#     print(f'Поток {threading.current_thread()} увеличит {X=} на {n}')
#     # lock.acquire()
#     for _ in range(n):
#         X += 1
#     lock.release()
#     print(f'Поток {threading.current_thread()} закончил инкриминирование')

# def increment(n, lock):
#     global X
#     print(f'Поток {threading.current_thread()} увеличит {X=} на {n}')
#     for _ in range(n):
#         with lock:
#             with lock:  # Possible DEADLOCK
#                 X += 1
#             # print(f'Увеличил Х. {X=}')
#
#     print(f'Поток {threading.current_thread()} закончил инкриминирование')

def increment(n, lock):
    global X
    print(f'Поток {threading.current_thread()} увеличит {X=} на {n}')
    with lock:
        for _ in range(n):
            X += 1

    print(f'Поток {threading.current_thread()} закончил инкриминирование')
    return '120'


def main():
    # t1 = threading.Thread(target=sleeper, args=(1,))
    # t2 = threading.Thread(target=sleeper, args=(1,))
    #
    # start_time = time.time()
    # # sleeper(1)
    # # sleeper(1)
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()
    #
    # end_time = time.time()
    # print(f'Программа исполнялась {end_time - start_time} сек.')

    # N = 1000000
    # # lock = threading.Lock()
    # # lock = threading.RLock()
    # lock = threading.BoundedSemaphore(value=1)
    # t1 = threading.Thread(target=increment, args=(N, lock))
    # t2 = threading.Thread(target=increment, args=(N, lock))
    # start_time = time.time()
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()
    #
    # end_time = time.time()
    # print(f'Итоговый Х {X}')
    # print(f'Программа исполнялась {end_time - start_time} сек.')

    N = 1000000
    # lock = threading.Lock()
    # lock = threading.RLock()
    lock = threading.BoundedSemaphore(value=1)
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(increment, n=N, lock=lock)
        future2 = executor.submit(increment, n=N, lock=lock)
    print(future1.result(), future2.result())
    end_time = time.time()
    print(f'Итоговый Х {X}')
    print(f'Программа исполнялась {end_time - start_time} сек.')


if __name__ == '__main__':
    main()
