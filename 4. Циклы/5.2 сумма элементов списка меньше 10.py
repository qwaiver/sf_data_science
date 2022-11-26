#Задайте список my_list, содержащий целые числа, с помощью модуля random, как и в предыдущей задаче.
#Используя инструкцию while, разработайте программу, которая вычисляет сумму элементов списка, пока она не
# будет больше или равна 10.

import random
my_list = []
N = 0
sum = 0
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
while sum < 10:
    print(sum)
    sum += my_list[N]
    N +=1
    print(' - ')
    print(f'Следующая сумма {sum}')
