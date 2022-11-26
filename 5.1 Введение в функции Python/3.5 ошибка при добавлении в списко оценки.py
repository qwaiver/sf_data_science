#Дополните функцию add_mark таким образом, чтобы возникала ошибка ValueError с текстом "Invalid Mark!"
# при попытке поставить оценку не из списка: 2, 3, 4 или 5.

def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if journal is None:
        journal = {}
    if mark < 2 or mark > 5:
        raise ValueError('Invalid Mark!')
    journal[name] = mark
    return journal

#add_mark('Ivanov', 6)
try:
    print(add_mark('Ivanov', 6))
#должна завершиться с ошибкой ValueError, которую мы выведем в блоке except
except ValueError as e:
    print(e)