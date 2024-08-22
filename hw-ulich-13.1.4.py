import threading
import random

file_path = input("Введите путь к файлу: ")

def fill_file():
    with open(file_path, "w") as file:
        for _ in range(100):
            file.write(str(random.randint(1, 100)) + "\n")
    print("Файл заполнен случайными числами.")

def find_primes():
    primes = []
    with open(file_path, "r") as file:
        for line in file:
            num = int(line.strip())
            if all(num % i != 0 for i in range(2, num)):
                primes.append(num)
    with open("primes.txt", "w") as file:
        for prime in primes:
            file.write(str(prime) + "\n")
    print("Простые числа записаны в файл 'primes.txt'.")

def calculate_factorials():
    factorials = []
    with open(file_path, "r") as file:
        for line in file:
            num = int(line.strip())
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            factorials.append(factorial)
    with open("factorials.txt", "w") as file:
        for fact in factorials:
            file.write(str(fact) + "\n")
    print("Факториалы записаны в файл 'factorials.txt'.")

# Проверка
fill_thread = threading.Thread(target=fill_file)
prime_thread = threading.Thread(target=find_primes)
factorial_thread = threading.Thread(target=calculate_factorials)

fill_thread.start()
fill_thread.join()

prime_thread.start()
factorial_thread.start()
prime_thread.join()
factorial_thread.join()

print("Статистика выполненных операций:")
print("- Файл заполнен случайными числами.")
print("- Простые числа записаны в файл 'primes.txt'.")
print("- Факториалы записаны в файл 'factorials.txt'.")