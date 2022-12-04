from collections import deque

users = deque([6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9])

first_number = users.popleft()#3.5
print(f'Извлечём первый иэлемент: {first_number}') #извлечь элемент из начала очереди
print('')

users.rotate(-5) #переместим пять элементов из начала списка в конец
last_number = users.pop()
print(f'Извлечём последний элемент модифифицированного списка: {last_number}') #3.6
print('')
print(f'Сколько раз встречается {last_number} в списке: {users.count(last_number)}') #3.7
# users.index - ищет первый индекс, на котором встречаетсяэлемент.