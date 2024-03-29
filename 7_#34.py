# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их
# придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def ritm(stroka):
    stroka = stroka.split()
    list = []
    for word in stroka:
        res = 0
        for i in word:
            if i in 'аеиоуыэюя':
                res = res + 1
        list.append(res)
    print(list.count(list[0]))
    print(len(list))
    print(list[0])
    return len(list) == list.count(list[0])

print('Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да')
stroka = input()
if ritm(stroka):
    print('Парам пам-пам')
else:
    print('Пам парам')
