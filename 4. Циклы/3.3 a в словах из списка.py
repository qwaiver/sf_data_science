#Дан список строк text_list. Посчитайте, сколько раз во всех строках списка встречается буква 'a'.
text_list = [
    'afbaad',
    'faaf',
    'afaga',
    'agag'
]

count = 0
for text in text_list:
#    for symbol in text:
#        if symbol == 'a':
#            count += 1
    count += text.count('a')
print(count)