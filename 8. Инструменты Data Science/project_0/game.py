import numpy as np

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
    