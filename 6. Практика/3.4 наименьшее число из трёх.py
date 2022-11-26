#Напишите функцию find_min_number(a, b, c), которая принимает три числа на вход и возвращает наименьшее из них.
# Используйте условия для решения задачи.

def find_min_number(a, b, c):
    min = 0
    if a < b and a < c or a < b and a == c or a < c and a == b:
        min = a
    elif b < c and b < a or b < c and b == a or b < a and b == c:
        min = b
    else:
        min = c
    return min

print(find_min_number(2, 2, -7))