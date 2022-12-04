import numpy as np

mystery1 = np.zeros((6,5,7), dtype=np.float16)
#массив соответсвует только структурой


#6.8
print(f'Размерность массива: {mystery1.ndim}') #3 размерность массива
print('')
#6.9
print(f'Форм\структура массива: {mystery1.shape}') # (6, 5, 7) максмальная протяжённость по одной из осей 7
print('')
#6.10
print(f'Общее число элементов в массиве: {mystery1.size}') # 210 элементов в массиве
print('')
#6.11
print(f'Тип элементов массива: {mystery1.dtype}') # float16 тип элементов массива
print('')
#6.12
print(f'Вес всех элементов массива в байтах: {mystery1.itemsize * mystery1.size} Byte') # 420 вес всех элементов массива в байтах