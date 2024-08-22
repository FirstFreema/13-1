import threading
import time

def sum_list(lst):
    for _ in range(5):
        total = sum(lst)
        print(f"Сумма элементов в списке: {total}")
        time.sleep(1)

def average_list(lst):
    for _ in range(5):
        avg = sum(lst) / len(lst)
        print(f"Среднеарифметическое в списке: {avg}")
        time.sleep(1)


user_input = input("Введите значения через пробел: ").split()
numbers = [int(x) for x in user_input]


sum_thread = threading.Thread(target=sum_list, args=(numbers,))
avg_thread = threading.Thread(target=average_list, args=(numbers,))
sum_thread.start()
avg_thread.start()
sum_thread.join()
avg_thread.join()