#Ваша задача — составить новый список links, в котором будут храниться полные ссылки до статей на сайте
# Коммерсант. Например, полная ссылка до первой статьи будет иметь вид:
# https://www.kommersant.ru//doc/5041434?query=data%20science
#Для решения задачи используйте функцию map(). К каждому элементу списка docs примените функцию-преобразование,
# которая добавляет к ссылке на начальную страницу сайта путь до статьи из списка docs.
#Результат работы функции map() оберните в список и занесите в переменную links.

docs = [
    '//doc/5041434?query=data%20science',
    '//doc/5041567?query=data%20science',
    '//doc/4283670?query=data%20science',
    '//doc/3712659?query=data%20science',
    '//doc/4997267?query=data%20science',
    '//doc/4372673?query=data%20science',
    '//doc/3779060?query=data%20science',
    '//doc/3495410?query=data%20science',
    '//doc/4308832?query=data%20science',
    '//doc/4079881?query=data%20science'
]

def link(lst):
    lnk = 'https://www.kommersant.ru'
    return lnk+lst

links = list(map(link, docs))
print(links)