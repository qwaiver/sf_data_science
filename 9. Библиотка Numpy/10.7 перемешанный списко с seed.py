#Напишите функцию shuffle_seed(array), которая принимает на вход массив из чисел, 
# генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает
# кортеж: перемешанный с данным seed массив (исходный массив должен оставаться без изменений),
# а также seed, с которым этот массив был получен.

import numpy as np

array = [1, 2, 3, 4, 5]
def shuffle_seed(array):
    a = np.random.randint(2**32, dtype=np.int64)
    np.random.seed(a)
    new_array = np.random.permutation(array)
    return (new_array, a)

print(shuffle_seed(array))
    