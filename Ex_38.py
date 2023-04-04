# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def menu():
    dict_phonebook = {}
    while True:
        anc = int(input("Введите запрос: 1. Сохранить файл телефонной книги, "
                        "2. Показать все контакты, 3. Найти контакт, 4. Добавить контакт, 5. Изменить контакт,"
                        "6. Удалить контакт, 7. Выход: "))

        if anc == 1:
            save_dir(dict_phonebook)
            print('save')
        elif anc == 2:
            if len(dict_phonebook) == 0:
                dict_phonebook = open_read_dir()
            if len(dict_phonebook) == 0:
                print('Справочник пуст')
            else:
                print(dict_phonebook)
        elif anc == 3:
            cnct_find(dict_phonebook)
        elif anc == 4:
            value_new_cnt = add_cnct(dict_phonebook)
            print(value_new_cnt)
            dict_phonebook.update(value_new_cnt)
            print('Сохранись')
        elif anc == 5:
            new_cnct = cnct_find(dict_phonebook)
            add_cnct(dict_phonebook, new_cnct)
        elif anc == 6:
            pass
        elif anc == 7:
            print("End")
            break
        else:
            print("Введите корректные данные")



def open_read_dir(dict_phonebook):
    dict_phonebook = {}
    print(dict_phonebook)
    with open('phonebook.txt', 'r') as f:
        for line_cnct in f.readlines():
            key, value = line_cnct.split(':')
            dict_phonebook[key] = value
        print(dict_phonebook)
        return dict_phonebook

def save_dir(dict_phonebook):
    str_phonebook = ' '
    for key, value in dict_phonebook.items():
        str_phonebook += f'{key}:{value} \n'
    with open('phonebook.txt', 'w') as f:
        f.write(str_phonebook)

def add_cnct(dict_phonebook, new_cnct_in = [0]):
    if len(new_cnct_in) < 2:
        name_cnct = input('Введите ИФ')
        phone_cnct = input('Введите телефон')
        comment_cnct = input('Введите комментарий')
        cnct_list = [phone_cnct, comment_cnct]
    else:
        name_cnct, cntc_list = tuple(new_cnct_in)
    # dict_phonebook[name_cnct] = dict_phonebook.setdefault(name_cnct, cnct_list)
    dict_phonebook.setdefault(name_cnct, cnct_list)
    print(f'{name_cnct}, {dict_phonebook[name_cnct]}')
    return dict_phonebook


def cnct_find(dict_phonebook):
    name_cnct = input('Введите ИФ')
    if name_cnct in dict_phonebook:
        print(f'{name_cnct}: {dict_phonebook[name_cnct]}')
        return [name_cnct, dict_phonebook[name_cnct]]
    else:
        print(f'Не найдено')


menu()