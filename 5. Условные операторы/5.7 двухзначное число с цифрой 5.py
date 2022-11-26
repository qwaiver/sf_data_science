#Дано двузначное число. Определите, входит ли в него цифра 5.
#Попробуйте решить задачу с использованием целочисленного деления
#и деления с остатком.

A = int(input('Введите двухзначное число: '))
result= ''

if A % 5 == 0 and A % 10 != 0:
    result = True
else:
    result = False
print(result)

#n = 15
#first_digit = n // 10
#second_digit = n % 10
#
#print((first_digit == 5) or (second_digit == 5))