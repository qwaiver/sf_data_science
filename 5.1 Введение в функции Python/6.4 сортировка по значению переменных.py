#Напишите lambda-функцию для расчёта гипотенузы прямоугольного треугольника: она принимает на вход длины
# двух катетов и возвращает длину гипотенузы

def sort_sides(l_in):
    l_in.sort(key=lambda hyp: (hyp[0]**2 + hyp[1]**2) ** (1/2))
    return l_in

print(sort_sides([(3,4), (1,2), (10,10)]))