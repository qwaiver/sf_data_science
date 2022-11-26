# Напишите функцию def division(), которая осуществляет деление двух чисел.
# Необходимо реализовать внутри функции отлов исключения ZeroDivisionError,
# в случае, если пользователь, при вызове функции, пытается поделить на ноль.

# Функция принимает на вход два числа - делимое и делитель.

def division(a, b):
    try:
      numb = a/b
    except ZeroDivisionError:
        print('Error! Matrices dimensions are different!')
        return None
    else:
        return numb

print(division(1, 0))
print(division(1, 1))
