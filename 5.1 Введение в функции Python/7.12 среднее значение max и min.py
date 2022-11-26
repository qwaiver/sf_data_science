#Напишите функцию between_min_max(...), которая принимает на вход числа через запятую.
#Функция возвращает среднее арифметическое между максимальным и минимальным значением этих чисел, то есть (max + min)/2.


def between_min_max(*nums):
    return (max(nums) + min(nums))/2




print(between_min_max(10))
print(between_min_max(1, 2, 3, 4, 5))
# 10.0
# 3.0