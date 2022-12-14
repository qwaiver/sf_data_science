#Напишите функцию-копилку с названием saver(), которая не принимает никаких аргументов.
# Она должна возвращать внутреннюю функцию adder(val), которая принимает на вход одно число val и
# возвращает сумму в копилке после прибавления числа val.
#Изначально в новой копилке хранится 0.

def saver():
    sum = 0
    def adder(val):
        nonlocal sum
        sum += val
        return sum
    return adder




pig = saver()
print(pig(25))
# 25
print(pig(100))
# 125
print(pig(19))
# 144