# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

my_list = [random.randint(1, 101) for _ in range(30)]

print(my_list)
print(*my_list)
print(set(my_list))

x = int(input("input number = "))
print(x)
k = 0
new_list = []
for i in my_list:
    if (x == i):
        k = k + 1
    else:
        if (i == (x - 1)) or (i == (x + 1)):
            print("Near number: ", i)

print("Meet number = ", k)

