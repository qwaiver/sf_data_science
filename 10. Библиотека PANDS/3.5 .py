#Ваша задача — проанализировать чистую прибыль.
#Доходы (incomes), расходы (expenses) и годы (years), соответствующие им, 
# предоставлены вам в виде списков. 
#Например:
'''
incomes = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]
'''

#Создайте функцию create_companyDF(incomes, expenses, years), которая  возвращает DataFrame,
# составленный из входных данных со столбцами Incomes и Expenses и индексами, 
# соответствующими годам рассматриваемого периода. Пример такого DataFrame представлен ниже.
'''
        Incomes	Expenses
2018	  478	  156
2019	  512	  130
2020	  196	  270
'''
#Также напишите функцию get_profit(df, year), которая возвращает разницу между доходом и расходом, 
# записанными в таблице df, за год year. Учтите, что если информация за запрашиваемый 
# год не указана в вашей таблице, вам необходимо вернуть None.

#Для проверки вхождения запрашиваемого года в перечень индексов таблицы вам поможет 
# атрибут df.index, который возвращает список индексов таблицы.

import pandas as pd

income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        "Incomes": income,
        "Expenses": expenses
        },
        index = years
    )
    return df

def get_profit(df, year):
    if year in df.index:
        profit = df.loc[year, 'Incomes'] - df.loc[year, 'Expenses']
    else:
        return None
    return profit
    
print(get_profit(year = 2018, df = [create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])]))