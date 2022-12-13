import numpy as np

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

nans_index = np.isnan(mystery)
#Получите булевый массив nans_index с информацией о np.nan в массиве mystery: 
# True - значение пропущено, False - значение не пропущено

def nan(nans_index):
    c = 0
    for i in nans_index:
        if i:
            c += 1
    return c
n_nan = nan(nans_index)
#n_nan = sum(nans_index)
#В переменную n_nan сохраните число пропущенных значений

mystery_new = mystery
mystery_new[np.isnan(mystery_new)] = 0
#Скопируйте массив mystery в массив mystery_new. Заполните пропущенные значения 
# в массиве mystery_new нулями

mystery_int = np.int32(mystery)
#Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int

array = np.sort(mystery)
#Отсортируйте значения в массиве по возрастанию и сохраните результат в переменную array

table = array.reshape((5,3), order='F')#F - по столбцам/C - по строкам
#Сохраните в массив table двухмерный массив, полученный из массива array.
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть по столбцам!

col = table[:,1]
#Сохраните в переменную col средний столбец из table

