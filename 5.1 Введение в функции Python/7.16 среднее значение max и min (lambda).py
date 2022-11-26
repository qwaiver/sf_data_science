#Перепишите функцию between_min_max из задания 7.12 в lambda-функцию. Функция принимает на вход
# числа через запятую и возвращает одно число — среднее между максимумом и минимумом этих чисел.

between_min_max = lambda *nums : (max(nums) + min(nums))/2

#def between_min_max(*nums):
#    return (max(nums) + min(nums))/2

print(between_min_max(10))
print(between_min_max(1, 2, 3, 4, 5))
# 10.0
# 3.0