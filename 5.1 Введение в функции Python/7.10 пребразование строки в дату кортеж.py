#Напишите функцию split_date(date), которая принимает на вход строку, задающую дату, в формате ддммгггг
#без разделителей. Функция должна вернуть кортеж из чисел (int): день, месяц, год.

def split_date(date):
    return (int(date[:2]), int(date[2:4]), int(date[4:8]))

print(split_date("31012019"))