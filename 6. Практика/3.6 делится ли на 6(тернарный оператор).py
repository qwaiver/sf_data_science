#Напишите функцию is_divided_by_six(), которая проверяет, делится ли число на 6.
#При решении воспользуйтесь тернарным оператором.
#Функция должна вернуть True, если число делится на шесть, и False — в противном случае.

def is_divided_by_six(x):

    return True if x%6==0 else False

print(is_divided_by_six(13))
print(is_divided_by_six(12))



