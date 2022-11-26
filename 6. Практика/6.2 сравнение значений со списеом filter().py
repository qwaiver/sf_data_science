#Определите функцию family(), на вход которой подаётся произвольное количество аргументов
# (строки с названием услуг МФЦ), а в результате возвращается список услуг, которые могут быть оказаны только
# многодетной семье.

#Для фильтрации входного списка аргументов используйте функцию filter().


family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]

def family(*args):
    global family_list
    return list(filter(lambda symbol: symbol in family_list, args))



print(family('newborn registration', 'parking permit', 'maternity capital', 'tax benefit', 'medical policy'))

#Должно быть выведено:
#['parking permit', 'maternity capital', 'tax benefit']