"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
#Обратите внимание, что в аргументах функции мы через двоеточие указываем тип данных для ввода (int), 
#через равно — стандартное значение этого типа данных. Стрелка (->) указывает, какой тип данных мы должны получить на выходе. 
#Это упростит заполнение документации (VS Code сможет автоматически генерировать её), 
#а также позволит в дальнейшем эффективнее работать с ошибками.
    """Рандомно угадываем число

    Args:
        number (int, optional): Загадонное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count

print(f'Количество попыток:{random_predict()}')