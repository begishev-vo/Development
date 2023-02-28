# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

a = int(input("Input number "))
print(" a = ", a)

first_three = a // 1000
last_three = a % 1000

print(" first_three = ", first_three)
print(" last_three = ", last_three)

first_number_1 = first_three // 100
second_iter_number_1 = first_three % 100
second_number_1 = second_iter_number_1 // 10
third_number_1 = first_three % 10
sum_first_three = first_number_1 + second_number_1 + third_number_1
print(" Sum_number_1 = ", sum_first_three)

first_number_2 = last_three // 100
second_iter_number_2 = last_three % 100
second_number_2 = second_iter_number_2 // 10
third_number_2 = last_three % 10
sum_last_three = first_number_2 + second_number_2 + third_number_2
print(" Sum_number_2 = ", sum_last_three)

if sum_first_three == sum_last_three:
    print("Yes")
else:
    print("No")
