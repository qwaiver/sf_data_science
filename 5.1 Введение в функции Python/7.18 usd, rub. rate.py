#Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd),
# сумму в рублях (rub) и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар.
#В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов,
# должна возникнуть ошибка ValueError('Not enough arguments').
# Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').

def exchange(usd = None, rub = None, rate = None):
    sum = [usd, rub, rate].count(None)
    errors = ['Too many arguments', None, 'Not enough arguments', 'Not enough arguments']
    if sum != 1: raise ValueError(errors[sum])

    if usd == None:
        return rub/rate
    elif rub == None:
        return usd*rate
    elif rate == None:
        return rub/usd

print(exchange(usd=100, rub=8500))
print(exchange(usd=100, rate=85))
print(exchange(rub=1000, rate=85))
# 85.0
# 8500
# 11.764705882352942
print(exchange(rub=1000, rate=85, usd=90))
# ValueError: Too many arguments
print(exchange(rub=1000))
# ValueError: Not enough arguments