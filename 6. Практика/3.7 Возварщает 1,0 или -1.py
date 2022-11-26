# Напишите функцию check_number_sign(), которая возвращает 1, если число положительное,
# -1, если число отрицательное, 0, если число - 0.

# Используйте в коде конструкцию if-elif-else.

# Функция принимает на вход одно число.

def check_number_sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


print(check_number_sign(0))
print(check_number_sign(100))
print(check_number_sign(-1))