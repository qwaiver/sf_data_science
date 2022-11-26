#Напишите функцию sort_ignore_case, которая принимает на вход список и сортирует его без учёта
# регистра по алфавиту.
#Функция возвращает отсортированный список.

def sort_ignore_case(ls):
    return sorted(ls,key = lambda s: s.lower())


print(sort_ignore_case(['Acc', 'abc']))
# ['abc', 'Acc']