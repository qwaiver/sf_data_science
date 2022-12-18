import pandas as pd

def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
        },
        index = years
    )
    return df
df = [create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])]
print(type(df))
print(f'тип df после выполнения create_companyDF {type(create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020]))}')

def get_profit(df, year):
    return f'тип df внутри getprofit {type(df)}'

print(get_profit(year = 2013, df = [create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])]))