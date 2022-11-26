#Напишите функцию is_prime(num), которая проверяет, является ли число простым.
#Функция должна вернуть True, если число простое, иначе — False.

def is_prime(num):
    if num == 2 or num == 3:
        return(True)
    elif num == 1 or num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0:
        return(False)
    else:
        return(True)

print(is_prime(1))
print(is_prime(10))
print(is_prime(13))

#def is_prime(num):
#    if num == 1:
#        return False
#    for i in range(2, num):
#        print(f'{num} / {i} = {num%i}')
#        if num % i == 0:
#            return False
#    return True
#
#print(is_prime(27))