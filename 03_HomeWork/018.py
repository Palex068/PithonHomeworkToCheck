"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
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

def nearest_value(value, N):
    M = set(N)
    M.add(value)  # я решил, что ответ это число отличное от введённого 
    M = sorted(M)  # пока не разобрался как эти операции записать в одну строку)
    m = M.index(value)
    if m == 0:
        return M[1]
    elif m == len(M) - 1:
        return M[len(M) - 1]
    else:
        if (value - M[m - 1]) > (M[m + 1] - value):
            return M[m + 1]
        elif (value - M[m - 1]) < (M[m + 1] - value):
            return M[m - 1]
        else:
            return M[m - 1], M[m + 1] # решил что, если два числа одинаково близки к введённому, то отдадим оба)

n = user_input("Количество элементов списка")

N = random_list(n)

print(f"\n{N}\n")

k = user_input("Искомое число", - 100, 100)

print(f"\nДля удобства, выведем сортированный список\n\n{sorted(N)}")

result = nearest_value(k, N)

print(f"\nРешение через цикл (функцию) - обычная запись: {result}")

# List Comprehension пока не получается, пожалуй нужен другой алгоритм для решения в одну строку, я подумаю)