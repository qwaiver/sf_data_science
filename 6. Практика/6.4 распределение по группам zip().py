#Напишите функцию print_groups, которая принимает список с именами пользователей. Используя генератор групп group_gen, печатайте на экран:
#<Фамилия И.> in group <номер группы по порядку>.


users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']

def group_gen(n=3):
    while True:
        for i in range(1, n+1):
            yield i

def print_groups(users):
    for group, name in zip(group_gen(), users):
        print(f'{name} in group {group}')