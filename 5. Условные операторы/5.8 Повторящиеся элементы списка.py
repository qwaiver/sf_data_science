#Проверьте, все ли элементы в списке являются уникальными.

A = [1,2,3,4,5]
A_set = set(A)

if len(A_set) < len(A):
    print('В списке есть повторябщиеся жлементы')
else:
    print('В списке нет повторяющихся элементов')

#print(len(list_) == len(set(list_)))