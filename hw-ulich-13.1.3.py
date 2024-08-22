import random
import threading

my_list = []
Volume=int(input("Введите количество чисел"))

def fill_list():
    for i in range(Volume):
        my_list.append(random.randint(1, 100))
    print("Список заполнен!")
    print(my_list)
    return my_list

def calculate_sum():
    while len(my_list) == 0:
        continue
    total_sum = sum(my_list)
    print(f"Сумма элементов списка: {total_sum}")

def calculate_average():
    while len(my_list) == 0:
        continue
    average = sum(my_list) / len(my_list)
    print(f"Среднее арифметическое: {average}")

thread1 = threading.Thread(target=fill_list)
thread2 = threading.Thread(target=calculate_sum)
thread3 = threading.Thread(target=calculate_average)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
