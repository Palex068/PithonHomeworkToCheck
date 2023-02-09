# Задача 4: 
# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 
# 3 2 4 -> yes
# 3 2 1 -> no

def user_input(msg):
    while True:
        try:
            number = int(input(f"Введите {msg}, число от 1 до 100: ")) # пока будут волшебные числа, после
            if not number in range(1, 101):                 # поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 100')

def breaking_chocolate(n, m, k):
    if k%n == 0 or k%m == 0:
        result = "yes"
    else:
        result = "no"
    return result

import os
os.system('cls')

n = user_input("первую сторону шоколадки")
m = user_input("вторую сторону шоколадки")
k = user_input("количество долек")

result = breaking_chocolate(n, m, k)

print(f"\n{n} {m} {k} -> {result}")