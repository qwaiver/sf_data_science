#Необходимо отсортировать кортеж по убыванию рейтинга. Если рейтинги совпадают, 
# то отсортировать кафе дополнительно по названию в алфавитном порядке.
#Получите словарь cafes с упорядоченными ключами из отсортированного списка,
# где ключи — названия кафе, а значения — их рейтинг.

from collections import OrderedDict

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

ratings.sort(key=lambda x: (-x[1], x[0]))
cafes = OrderedDict(ratings)
print(cafes) #<class 'collections.OrderedDict'> - получили это не словарь(dict)

''' Списко не нужно было изменять в словарь! С чего я это взял - хз.
cafes = {}
dafes = {}


for i in ratings:
    cafes.update({i[0]: i[1]})
 
dafes = sorted(cafes, key=dafes.keys())

for w in dafes:
     dafes[w] = cafes[w]
     
print(dafes)
'''