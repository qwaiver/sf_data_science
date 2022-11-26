#С помощью цикла for проверьте, есть ли в полученном списке повторяющиеся числа. Для этого пройдитесь
#в цикле по элементам полученного списка и на каждом шаге проверьте, сколько раз текущий элемент встречается в списке.

import random
my_list = []
N = 0
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
    #генерация обрывается на повторяющемся элементе
    print(f'Добавим в списко элемент {my_list[N]}')
    if my_list.count(my_list[N]) > 1:
        print(f'Элемент {my_list[N]} уже существует в списке')
        break
    else:
        print(my_list)
        N += 1

#решение через for на уже готовом списке
#for elem in my_list:
#    if my_list.count(my_list[N - 1]) > 1:
#        print(f'Элемент {elem} повторяется {my_list.count(elem)} раз')
#        print('Fail')
#        print(my_list)
#        break
#    else:
#        print(my_list)
#        print('Ok')



