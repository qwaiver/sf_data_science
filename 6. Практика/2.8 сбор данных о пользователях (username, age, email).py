#Напишите программу, которая запрашивает у пользователя следующие данные : username, age,
# email о нескольких пользователях и собирает эти данные в структуру
#Первый элемент каждого кортежа — порядковый номер пользователя, второй элемент — словарь с данными.
#В итоге должен получиться список с кортежами.
#Далее необходимо провести аналитику (собрать данные о пользователях в словарь)

number_user = 1
users = []
while True:
    username = input('Введите имя пользователя или введите "end" для завершения: ')
    if username == 'end':
        break
    age = input('Введите возраст пользователя: ')
    email = input('Введите email пользователя: ')
    user = (number_user, {'username': username, 'age': age, 'email': email})
    users.append(user)
    number_user += 1

dict_users = {'username':[], 'age':[], 'email':[]}

for i in range(0, len(users)):
    dict_old = users[i][1]
    dict_users['username'].append(dict_old['username'])
    dict_users['age'].append(dict_old['age'])
    dict_users['email'].append(dict_old['email'])

print(dict_users)

