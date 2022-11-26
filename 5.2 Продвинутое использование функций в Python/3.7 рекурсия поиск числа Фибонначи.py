#Числа Фибоначчи — пример последовательности, которую можно получить рекурсивно.
# Вот первые числа этой последовательности: 0, 1, 1, 2, 3, 5, 8, 13 …
#Как вы могли заметить, каждый n-ый элемент — это сумма и элементов.

#Напишите рекурсивную функцию fib(n), которая считает n-ое число Фибоначчи. Будем считать, что fib(0) = 0 и fib(1) = 1.

def fib(n):
    if n == 1: return 1
    if n == 0: return 0
    return fib(n-1) + fib(n-2)


print(fib(0))
# 0
print(fib(2))
# 1
print(fib(6))
# 8