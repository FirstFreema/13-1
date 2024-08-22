import threading

def sum_elements(data_list):
    total = 0
    for i in range(5):
        total += sum(data_list)
    print(f"Сумма элементов: {total}")
    lock.release()

def average_elements(data_list):
    total = 0
    for i in range(5):
        total += sum(data_list) / len(data_list)
    print(f"Среднее арифметическое: {total / 5}")
    lock.release()

data_list = [int(x) for x in input("Введите элементы списка через пробел: ").split()]

lock = threading.Lock()
thread1 = threading.Thread(target=sum_elements, args=(data_list,))
thread2 = threading.Thread(target=average_elements, args=(data_list,))
lock.acquire()
thread1.start()
lock.acquire()
thread2.start()
thread1.join()
thread2.join()