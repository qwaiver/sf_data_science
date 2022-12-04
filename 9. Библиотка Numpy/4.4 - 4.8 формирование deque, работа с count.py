from collections import deque, Counter

#списки не полные! Полный только на портале SkillFactory
center = [['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], ['Bread', 'Yoghurt', 'Chips', 'Ketchup']]
south = [['Cola', 'Meat', 'Cheese', 'Yoghurt', 'Beer', 'Milk', 'Milk', 'Meat', 'Cola', 'Cola', 'Cheese', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Bread', 'Milk', 'Cheese', 'Chocolate'], ['Soap', 'Milk', 'Cola'], ['Milk', 'Bread', 'Yoghurt', 'Meat', 'Meat'], ['Bread', 'Milk', 'Beer'], ['Beer'], ['Chocolate', 'Meat', 'Chocolate', 'Cola', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Bread', 'Meat', 'Soap', 'Soap', 'Milk', 'Milk', 'Cola'], ['Beer', 'Beer', 'Meat', 'Chips', 'Bread', 'Bread', 'Bread', 'Bread', 'Milk', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Chips', 'Bread', 'Bread', 'Yoghurt'], ['Chips', 'Milk', 'Soap'], ['Meat', 'Beer', 'Milk', 'Chocolate', 'Bread', 'Yoghurt'], ['Chips', 'Meat', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Meat', 'Yoghurt', 'Milk'], ['Bread', 'Soap', 'Bread', 'Meat', 'Beer', 'Yoghurt', 'Milk', 'Cola', 'Bread', 'Ketchup'], ['Meat', 'Milk'], ['Meat', 'Beer', 'Yoghurt'], ['Cola', 'Bread', 'Cola', 'Chocolate', 'Chips', 'Meat', 'Cheese'], ['Milk', 'Milk', 'Cheese', 'Meat']]
north = [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Chips'], ['Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'], ['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese'], ['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], ['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread'], ['Chips', 'Cola', 'Beer', 'Chips', 'Cola', 'Cola', 'Beer']]

#4.4
#Вначале избавьтесь от излишней вложенности: в каждой переменной (center, south, north) 
# должен храниться объединённый список купленных товаров без разбиения по чекам.
#После этого определите, в каком магазине было куплено больше всего товаров.
 
mn_c = deque()
mn_s = deque()
mn_n = deque()

for i in center:
    mn_c.extend(i)
for i in south:
    mn_s.extend(i)
for i in north:
    mn_n.extend(i)
    

''' решение без дек
for i in center:
    for y in i:
        mn_c.append(y)
mn_c = list(mn_c)
    
for i in south:
    for y in i:
        mn_s.append(y)
mn_s = list(mn_s)
    
for i in north:
    for y in i:
        mn_n.append(y)
mn_n = list(mn_n)
    '''
print(len(mn_c)) # 548
print(len(mn_s)) # 478
print(len(mn_n)) # 500
print('')

#4.5
#Теперь получите объекты-счётчики (Counter) из каждого полученного в предыдущем задании 
# списка покупок и сохраните их в отдельные переменные (они пригодятся для выполнения следующих задач).
#Сколько раз покупали самый редкий товар в магазине north? Запишите ответ в числовой форме.

count_c = Counter(mn_c)
count_s = Counter(mn_s)
count_n = Counter(mn_n)
print('4.4 Сколько раз покупали самый редкий товар в магазине north?')
print(count_n) # 'Cheese': 10
print('')

#4.6 
#Выберите товар, который в магазине center покупали чаще, чем в магазине north:
print(count_c - count_n)
#Counter({'Meat': 31, 'Cheese': 29, 'Bread': 23, 'Chips': 22, 'Milk': 21, 'Ketchup': 19, 'Chocolate': 2})
print('')

#4.7
#Есть ли такой товар, который в одном из магазинов покупали чаще, чем в двух других вместе взятых?
# Если да, выберите магазин с настолько популярным товаром:
print(f'c {count_c - (count_s + count_n)}') # пусто
print(f's {count_s - (count_c + count_n)}') # пусто
print(f'n {count_n - (count_s + count_c)}') # n Counter({'Cola': 6})
print('')

#4.8
#Определите суммарное число продаж каждого товара во всех магазинах, сложив все объекты-счётчики. 
# Сколько раз был куплен второй по популярности товар? Запишите ответ в числовой форме.
print(count_c + count_n + count_s)
#Counter({'Beer': 257, 'Bread': 240, 'Cola': 236, 'Chips': 128, 'Meat': 121, 'Milk': 111, 'Chocolate': 107, 'Yoghurt': 90, 'Soap': 80, 'Cheese': 79, 'Ketchup': 77})
