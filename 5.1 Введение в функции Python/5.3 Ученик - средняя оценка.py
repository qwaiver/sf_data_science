#Передайте в функцию mean_mark, которая была создана в начале данного подраздела юнита, этот список,
# а также фамилию студента Kuznetsov с помощью оператора распаковки.

marks = [4,5,5,5,5,3,4,4,5,4,5]

def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    print(name+':', result)

mean_mark('Kusznetsov', *marks)