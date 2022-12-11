import numpy as np

np.finfo(np.float16) # границы типа данных с плаваущей запятой
np.iinfo(np.int16) # границы типа данных целых чисел
np.iinfo(np.uint16) # границы типа данных целых неотрицательных(беззнаковый тип данных) чисел
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

#Всего в выдаче будет 24 строки. Int, uint и float мы уже изучили. 
# Datetime и timedelta используются для хранения времени, 
# complex используется для работы с комплéксными числами.

print(np.iinfo(np.int16))