#Напишите рекурсивную функцию multiply_lst(), которая перемножает элементы заданного списка между собой.

def multiply_lst(lst):
    print(lst)
    if len(lst) == 0: return 1
    return lst[0] * multiply_lst(lst[1:])

m_lst = [10, 21, 24, 12]
print(multiply_lst(m_lst))