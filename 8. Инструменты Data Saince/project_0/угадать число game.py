import numpy as np

def random_predict(number:int=1) -> int:
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

number = np.random.randint(1,101) # генерируем число
count = 0 #количество угадываний

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print('Число должно быть меньше')
        
    elif predict_number < number:
        print('Число дожно быть больше')
    else:
        print('Поздравляю! Вы угадали число.')
        break
    