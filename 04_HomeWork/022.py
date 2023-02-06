"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств

Пример:

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
import random, os
os.system('cls')


def random_list(n, range_start = -5, range_finish = 5):  # Список случайных чисел, очень не хотелось их вбивать руками))
    N = []
    for _ in range(n):
        N.append(random.randint(range_start, range_finish + 1))
    return N


n = (int(input("Введите количество элементов первого списка: ")))
m = (int(input("Введите количество элементов второго списка: ")))

N = random_list(n, -10, 10)
M = [random.randint(-10, 10) for _ in range(m)]

print(*sorted(N), sep="\t")
print(*sorted(M), sep="\t")

result = list()
for i in N:
    for j in M:
        if i == j:
            result.append(i)

print(*sorted(set(result)), sep="\t")
