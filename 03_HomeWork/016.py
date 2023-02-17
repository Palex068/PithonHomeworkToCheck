"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""

import os, random
os.system('cls')

def user_input(msg, range_start = 1, range_finish = 100):  # безопасный ввод
    while True:
        try:
            # пока будут волшебные числа, после
            number = int(input(f"Введите {msg} (число от {range_start} до {range_finish}): "))
            # поправлю на передаваемый в функцию элемент
            if not number in range(range_start, range_finish + 1):
                raise ValueError
            return number

        except ValueError:
            print(f'Вводите только числа от {range_start} до {range_finish}')

def random_list(n, range_start = -5, range_finish = 5):  # Список случайных чисел, очень не хотелось их вбивать руками))
    N = []
    for _ in range(n):
        N.append(random.randint(range_start, range_finish + 1))
    return N

def value_count(value, N):
    result_count = 0
    for i in N:
        if i == value:
            result_count += 1
    return result_count


n = user_input("Количество элементов списка")

N = random_list(n)

print(f"\n{sorted(N)}\n")

k = user_input("Искомое число", - 100, 100)

result = value_count(k, N)

print(f"\nРешение через цикл (функцию) - обычная запись: {result}")

# List Comprehension

print(f"\nРешение в одну строку (List Comprehension):    {sum(1 for i in N if i == k)}")