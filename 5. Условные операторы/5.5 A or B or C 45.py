A = int(input('введите значение A'))
B = int(input('Введите значение B'))
C = int(input('введите значение C'))
result = ''

if A < 45 and B > 45 and C > 45:
    result = True
elif A > 45 and B < 45 and C > 45:
    result = True
elif A > 45 and B > 45 and C < 45:
    result = True
else:
    result = False

print(result)

#if ((A < 45) and (B >= 45) and (C >=45)) or \
#    ((A >= 45) and (B < 45) and (C >=45)) or \
#    ((A >= 45) and (B >= 45) and (C < 45)):