import pandas as pd

melb_data = pd.read_csv('data/melb_data.csv', sep=',')

#5.1 Какова цена объекта недвижимости под индексом 15?
print(melb_data.loc[15, ['Price']])
#Price    1310000.0
#Name: 15, dtype: object
print('')

print(melb_data.loc[15, 'Price']) # 1310000.0
print('')

#5.2 Когда был продан объект под индексом 90?
print(melb_data.loc[90, ['Date']]) # Date 10/09/2016
print('')

#5.3 Во сколько раз площадь прилегающей территории, на которой находится здание с индексом 3521, 
# больше площади участка, на котором находится здание с индексом 1690? Ответ округлите 
# до целого числа.
print(melb_data.loc[3521, 'Landsize']/melb_data.loc[1690, 'Landsize']) # 2.7857142857142856(3)