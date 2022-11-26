#Дано натуральное восьмизначное число. Выясните,
# является ли оно палиндромом
# (читается одинаково слева направо и справа налево).

A = 12344321
a = str(A)
b = a[::-1]
B = int(b)
result = ''

if A == B:
    result = True
else:
    result = False

print(result)

#num = 12345678
#print(str(num) == str(num)[::-1])