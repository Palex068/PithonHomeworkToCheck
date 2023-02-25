"""
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.

Ввод:
ноутбук
Вывод:
12
"""
import os
os.system('cls')


def letter_cost(ch):
    
    ch = ch.upper()
    if ch in " ":
        n = 0
    elif ch in "AEIOULNSTRАВЕИНОРСТ":
        n = 1
    elif ch in "DGДКЛМПУ":
        n = 2
    elif ch in "BCMPБГЁЬЯ":
        n = 3
    elif ch in "FHVWYЙЫ":
        n = 4
    elif ch in "KЖЗХЦЧ":
        n = 5
    elif ch in "JXШЭЮ":
        n = 8
    elif ch in "QZФЩЪ":
        n = 10
    return n

def word_counter(word):
    word_count = 0
    word = word.upper()
    for i in word:
        l_c = letter_cost(i)
        word_count += l_c
        print(f"{i} = {l_c}")
    return word_count

word = input(f"Введите слово: ")
print()

print(f"\n{word_counter(word)}")
