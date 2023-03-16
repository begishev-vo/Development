# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(x, y):
    x = x + 1
    y = y - 1
    if y > 0:
        return summa(x, y)
    else:
        return x

a = int(input("Input number a = "))
b = int(input("Input number b = "))

print(f'Sum equal = {summa(a, b)}')