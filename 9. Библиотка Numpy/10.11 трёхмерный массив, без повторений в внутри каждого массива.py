#Напишите функцию get_unique_loto(num). Она так же, как и функция в задании 10.10, 
# генерирует num полей для игры в лото, однако теперь на каждом поле 5х5 числа не могут повторяться.
#Функция также должна возвращать массив формы num x 5 x 5.

import numpy as np

def get_unique_loto(num):
    get_loto = list()
    loto_numbers = np.arange(1, 100+1, 1)
    for i in range(num):
        loto = np.random.choice(loto_numbers, size=(5,5), replace=False)
        get_loto.append(loto)
    get_loto = np.array(get_loto)
    return get_loto

print(get_unique_loto(3))

#ответ
'''
array([[[26, 91, 73,  7, 16],
       [46, 85, 78, 77, 51],
       [84, 86, 55, 71, 58],
       [17, 61, 50, 30, 97],
       [66, 29, 38, 41, 32]],

      [[49, 32,  3, 21, 85],
       [45,  8, 94, 46, 96],
       [41, 38, 58, 37, 98],
       [66, 77, 54, 80, 26],
       [62, 63, 72,  5, 43]],

      [[55, 60,  6, 80, 97],
       [23, 69, 94,  9, 24],
       [17, 98, 27, 63, 79],
       [84, 74, 51, 39, 54],
       [77, 30, 48, 75, 85]]])
       '''