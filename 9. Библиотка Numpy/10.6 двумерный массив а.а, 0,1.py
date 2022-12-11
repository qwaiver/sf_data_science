import numpy as np

#Напишите функцию get_chess(a), которая принимает на вход длину стороны квадрата a 
# и возвращает двумерный массив формы (a, a), заполненный 0 и 1 в шахматном порядке. 
# В левом верхнем углу всегда должен быть ноль.
#Примечание. воспользуйтесь функцией np.zeros, а затем с помощью срезов без циклов 
# задайте необходимым элементам значение 1.
#В Python для получения каждого второго элемента используется срез [::2]. 
# Подумайте, как грамотно применить этот принцип к двумерному массиву.

def get_chess(a):
    zero = np.zeros((a,a))
    zero[1::2,::2] = 1
    zero[::2, 1::2] = 1
    return zero
    

print(get_chess(6))