"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7 5 15
# 5
# 15
# [1, 9, 13, 14, 19]
"""
N = list(int(i) for i in input().split())
n_min, n_max = int(input()), int(input())
# print(N)
# result = list()
# for i in range(len(N)):
#     if N[i] in range(n_min, n_max + 1):
#         result.append(i)
# print(result)
print(list(i for i in range(len(N)) if N[i] in range(n_min, n_max + 1)))