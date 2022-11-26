#Напишите функцию get_total, которая принимает на вход число единиц товара и стоимость каждой единицы.
# Функция возвращает одно число — общую стоимость данного числа товаров.

def get_total(units, price):
    result = units * price
    return result

print(get_total(15, 50))