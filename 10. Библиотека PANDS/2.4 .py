#В аптеку поступают партии лекарств. Их названия находятся в списке names, 
# количество единиц товара находится в списке counts.
#Например:
'''
names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
'''
#Напишите функцию create_medications(names, counts), создающую Series medications, 
# индексами которого являются названия лекарств names, а значениями — их количество в партии counts.
#Также напишите функцию get_percent(medications, name), которая возвращает 
# долю товара с именем name от общего количества товаров в партии в процентах.

import pandas as pd

names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

def create_medications(names, counts):
    medications = pd.Series(data = counts, index = names, name = 'Series medications')
    return medications

def get_percent(medications, name):
    return(medications.loc[name]/sum(medications) * 100)

print(get_percent(name = 'cyntomycin', medications = create_medications(['chlorhexidine', 'cyntomycin', 'afobazol'],[26, 18, 7])))