# Напишите функцию lucky_ticket(), которая проверяет, является ли билетик счастливым.

# Памятка: билетик счастливый, если сумма первых трех цифр равна сумме последних трех цифр.

# На вход функция получает шестизначное число.

def lucky_ticket(ticket_number):
    lucky_list=str(ticket_number)
    list_sum = []
    for i in lucky_list:
        list_sum.append(int(i))
    if sum(list_sum[0:3]) == sum(list_sum[3:6]):
        return True
    else:
        return False

print(lucky_ticket(111111))
print(lucky_ticket(123321))
