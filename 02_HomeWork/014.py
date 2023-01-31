"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k ), не превосходящие числа N.

10 -> 1 2 4 8
"""

import os, math
os.system('cls')

def user_input(): # безопасный ввод
    while True:
        try:
            number = int(input("Введите число от 1 до 1000: ")) # пока будут волшебные числа, после
            if not number in range(1, 1001):        # поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 1000')

n = user_input()
result = 1
result_list = []
while n >= result:
    result_list.append(result)
    result *= 2 
print(*result_list)

# решение в одну строку, от вездесущего ребенка)

print(*[2 ** x for x in range(0, int(math.log2(int(input("Введите число: ")))) + 1)])