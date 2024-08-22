import threading
import time

def find_max(numbers):
    for _ in range(5):
        max_num = max(numbers)
        print(f"Максимальное значение: {max_num}")
        time.sleep(1)

def find_min(numbers):
    for _ in range(5):
        min_num = min(numbers)
        print(f"Минимальное значение: {min_num}")
        time.sleep(1)

numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

max_thread = threading.Thread(target=find_max, args=(numbers,))
min_thread = threading.Thread(target=find_min, args=(numbers,))
max_thread.start()
min_thread.start()
max_thread.join()
min_thread.join()


