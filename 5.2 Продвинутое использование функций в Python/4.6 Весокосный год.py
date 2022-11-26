#Напишите функцию is_leap(year), которая принимает на вход год и возвращает True, если год високосный,
# иначе — False

def is_leap(year):
    if year%400 == 0: return True
    elif year%4 == 0 and year%100 != 0: return True
    else: return False


print(is_leap(2021))

# True
# False
# True