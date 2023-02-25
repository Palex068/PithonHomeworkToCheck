from os import path
from os import system

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base): # если файла с базой нет, создадим его
    with open(file_base, "w", encoding="utf-8") as f:
        f.write('0 Фамилия Имя Отчество Телефон\n')


def read_records(): # копируем содержимое файла в переменную all_data
    global all_data, id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data


def show_all(): # печать телефонного справочника
    if not all_data:
        print("Empty data")
    else:
        matrix_data = list(string.split() for string in all_data)
        for i in matrix_data:
            print(f"""{i[0]:4}{i[1]:15}{i[2]:15}{i[3]:15}{i[4]:12}""")
                

def add_new_contact(): # добавление новой записи
    
    global id
    data_content = ['Фамилию','Имя','Отчество','Телефон']
    answers = []
    
    for data in data_content:
        answers.append(input_data(data))
    
    if not exist_contact(0, " ".join(answers)):
        id += 1
        answers.insert(0, str(id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Данные контакта добавлены!\n")
    else:
        print("Такая запись уже существует!")


def input_data(num):  # проверка полученных данных
    
    answer = input(f"Введите {num}: ")
    while True:
        if num in "Фамилия Фамилию Имя Отчество":
            if answer.isalpha():
                break  #TODO: добавить возможность исправить запись
        if num in "Телефон":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Ошибка ввода данных!\n"
                       f"Для ФИО используйте только буквы!"
                       f"Для номера телефона используйте цифры!"
                       f"Длинна номера телефона 11 цифр!\n"
                       f"Введите {num}: ")
    return answer


def exist_contact(rec_id, data):
    """Проверка записи в базе

    :type data: проверка записи
    :type rec_id: проверка id
    """

    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def search_contact():
    search_data = exist_contact(0, input("Введите данные контакта: "))
    
    if search_data:
        matrix_data = list(string.split() for string in search_data)
        for i in matrix_data:
            print(f"""{i[0]:4}{i[1]:15}{i[2]:15}{i[3]:15}{i[4]:12}""")
        
    else:
        print("Такой записи нет!")


def change_contact(data_tuple):  #Изменение существующей записи

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Такая запись существует!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Запись изменена!\n")


def del_contact(): # Удаление записи

    global all_data

    symbol = "\n"
    show_all()
    
    del_record = input("Введите id записи: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Ошибка ввода данных!")


def interface():
    play = True
    while play:
        read_records()
        answer = input("""
* * * * * * * * * * * * * * *        
*   Телефонный справочник:  *
* * * * * * * * * * * * * * *
*  1. Показать все записи   *
*  2. Добавить контакт      *
*  3. Найти контакт         *
*  4. Редактировать запись  *
*  5. Удалить контакт       *
*  0. Выход                 *
* * * * * * * * * * * * * * *
""")             
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                pass
            case "0":
                play = False
            case _:
                print("Try again!\n")
    else:
        system('cls')
        print("I'll be back! 😎 ")


def edit_menu():  #Меню редактирования

    add_dict = {"1": "Фамилия", "2": "Имя", "3": "Отчество", "4": "Телефон"}

    show_all()
    record_id = input("Введите id записи: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nВыберите данные для замены:")
            change = input("1. Фамилия\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. Номер телефона\n"
                           "5. Выход\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, input_data(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Ошибка ввода данных, повторите ввод.")
    else:
        print("Ошибка ввода данных!")

interface()