A = int(input('введите значение A'))
result= ''

if -10 <= A <= -1:
    result = False
elif 2 <= A <= 15:
    result = False
else:
    result = True

print(result)

#if not (-10 <= A <= -1 or 2 <= A <= 15):
#    print("The number does not belong to the interval") # Число не принадлежит интервалу
#else:
#    print("The number belongs to the interval") # Число принадлежит интервалу