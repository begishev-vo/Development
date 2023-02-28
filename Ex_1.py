# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input("Input number "))
print(" a = ", a)

first_number = a // 100
second_iter_number = a % 100
second_number = second_iter_number // 10
third_number = a % 10
sum = first_number + second_number + third_number
print(" first_number = ", first_number)
print(" second_number = ", second_number)
print(" third_number = ", third_number)

print(" Sum_number = ", sum)

