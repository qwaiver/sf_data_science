# Напишите свою функцию password_change, которая должна выводить на экран
# отформатированную строку в следующем виде:

# "User user_name changed password to new_password"

# Мы уже сделали заготовку функции вам осталось только задать строку
# Переменные, которые надо использовать, указаны в круглых скобках после имени функции
# user_name - имя пользователя, new_password - новый пароль
# запишите форматированную строку вместо знаков вопроса
# ! обязательное условие - задача должна быть решена с использованием метода format

def change_password(user_name, new_password):
    return 'User {} changed password to {})'.format(user_name, new_password)

print(change_password("Lena", "qwerty"))