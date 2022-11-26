#Функция должна возвращать список, в который добавила запись.
#Указание: сделайте отчество аргументом по умолчанию со значением None, так как отчество может быть
# не у всех регистрирующихся.

#Также сделайте так, чтобы пустой список создавался в том случае, если он не был передан извне.
# Таким образом, по умолчанию registry имеет значение None, и если при вызове функции список не был передан,
# он создаётся в теле функции.

#Наконец, проверьте дату на корректность. Если дата неправильная, верните ошибку ValueError("Invalid Date!").
# Для этого вам пригодится функция check_date из предыдущего задания.

def check_date(day, month, year):
    if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
        return False
    if 1900 > year or year > 2022:
        return False
    if 1 > month or month > 12:
        return False
    if 1 > month or month > 12:
        return False
    if 1 > day or day > 31:
        return False
    if month in [4,6,9,11] and day > 30:
        return False
    def is_leap():
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    if is_leap() is True and month == 2 and day > 29:
        return False
    if is_leap() is False and month == 2 and day > 28:
        return False
    return True


def register(surname, name, date, middle_name = None, registry = None):
    if registry is None:
        registry = list()
    if check_date(*date) is not True:
        raise ValueError('Invalid Date!')
    registry.append((surname, name, middle_name, date[0], date[1], date[2]))
    return registry




reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
print(reg)
# [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]

reg = register('Ivanov', 'Sergej', (24, 13, 1995))
# ValueError: Invalid Date!






