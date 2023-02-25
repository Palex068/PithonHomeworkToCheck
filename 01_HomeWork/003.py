# Задача 3: 
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 
# 385916 -> yes
# 123456 -> no

def user_input():
    while True:
        try:
            number = int(input(f"Введите шестизначное число: ")) # пока будут волшебные числа, 
            if not number in range(100000, 1000000):  # после поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print(f'\nВводите только шестизначные числа\n')

def sum_of_digits(number):
    digits_sum = 0
    while number > 0:
        digits_sum += int(number%10)
        number //=10
    return digits_sum

def checks_the_tickets_happiness(number):
    
    first_half = number//1000
    second_half = number - first_half*1000
    if sum_of_digits(first_half) == sum_of_digits(second_half):
        result = 'yes'
    else:
        result = 'no'
    return result
 
import os
os.system('cls')

number = user_input()

result = checks_the_tickets_happiness(number)

print(f"{number} -> {result}")
