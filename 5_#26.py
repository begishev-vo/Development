# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    else:
        return power(x, n - 1) * x


A = int(input("Input number A = "))
B = int(input("Input number B = "))

print(f'Power equal = {power(A, B)}')