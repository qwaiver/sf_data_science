#Напишите функцию sum_min_numbers(), которая также принимает на вход три числа и возвращает сумму двух наименьших.
#Можно использовать функцию из предыдущего задания(3.4) для поиска минимального числа.

def sum_min_numbers(a, b, c):
    min = 0
    min_list = [a, b, c]
    if a < b and a < c or a < b and a == c or a < c and a == b:
        min = a
    elif b < c and b < a or b < c and b == a or b < a and b == c:
        min = b
    else:
        min = c

    min2 = sorted(min_list)
    return min + min2[1]

print(find_min_number(2, 2, -7))