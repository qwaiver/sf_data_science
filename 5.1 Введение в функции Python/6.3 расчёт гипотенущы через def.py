#Напишите lambda-функцию для расчёта гипотенузы прямоугольного треугольника: она принимает на вход длины
# двух катетов и возвращает длину гипотенузы

#def hyp(a, b):
#    return (a**2 + b**2)**(1/2)

hyp = lambda a, b: ((a**2 + b**2)**(1/2))

print(hyp(3,4))
print(hyp(1,9))