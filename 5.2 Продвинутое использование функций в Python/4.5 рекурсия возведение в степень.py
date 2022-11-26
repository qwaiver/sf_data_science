#Напишите рекурсивную функцию power(val, n), которая возводит число в заданную целую натуральную степень
# (или в степень 0).
#В качестве первого аргумента функция принимает число, в качестве второго — желаемую степень.

def power(val, n):
    if n == 0 : return 1
    if n == 1 : return val
    return (val * power(val, n-1))

print(power(25,0))
print(power(-5,4))
# 1
# 625