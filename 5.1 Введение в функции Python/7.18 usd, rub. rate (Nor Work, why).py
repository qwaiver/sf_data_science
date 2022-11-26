#Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd),
# сумму в рублях (rub) и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар.
#В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов,
# должна возникнуть ошибка ValueError('Not enough arguments').
# Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').

def exchange(usd=0, rub=0, rate=0):
    if usd > 0 and rub > 0 and rate > 0:
        raise ValueError('Too many arguments')
    elif usd > 0 and rub > 0:
        return rub/usd
    elif usd > 0 and rate > 0:
        return usd * rate
    elif rub > 0 and rate > 0:
        return rub/rate
    #elif (usd > 0 and rub == 0 and rate == 0) or (usd == 0 and rub > 0 and rate == 0) or (usd == 0 and rub == 0 and rate > 0) or (usd == 0 and rub == 0 and rate == 0):
    else:
        raise ValueError('Not enough arguments')



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