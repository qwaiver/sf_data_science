#Напишите функцию check_date(day, month, year), которая проверяет корректность даты рождения по
# следующим условиям:

#1. Все аргументы должны быть целыми числами (проверить с помощью type(day) is int).
#2. Годом рождения не может быть год до 1900 и год после 2022.
#3. Номер месяца не может быть больше 12 и меньше 1.
#4. Номер дня не может быть больше 31 и меньше 1.
#5. В сентябре, апреле, июне и ноябре 30 дней.
#6. Если год является високосным, то в феврале (второй месяц) должно быть 29 дней, в противном случае — 28.
#7. Если дата корректна, вернуть True, если же хотя бы одно из представленных условий не было выполнено — False.


def check_date(day, month, year):
    x = False
    if type(day) is int and type(month) is int and type(year) is int and\
        1899 < year < 2023 and\
        0 < month < 13 and\
        0 < day < 32:
        x = True
    if month in [4, 5, 6, 7] and day > 30:
        x = False
    def is_leap():
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    if is_leap() is True and month == 2 and day > 28:
        x = False
    if is_leap() is False and month == 2 and day > 27:
        x = False
    return x



print(check_date(18,9,1999))
print(check_date(29,2,2000))
print(check_date(29,2,2021))
print(check_date(13,13,2021))
print(check_date(13.5,12,2021))



# True
# True
# False
# False
# False