import numpy as np

a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

#8.4
#Однако на практике не всегда есть возможность нарисовать вектора, чтобы понять,
# являются ли они сонаправленными. Поэтому есть несколько математических способов 
# определить сонаправленность векторов. Один из них: сумма длин сонаправленных векторов должна 
# быть равной длине суммы двух векторов.
#С помощью этого критерия среди векторов a, b и c (которые приведены в файле выше)
# найдите пару сонаправленных векторов.

#длинны векторов
len_a = np.linalg.norm(a) #np.sqrt(np.sum(a ** 2))
len_b = np.linalg.norm(b)
len_c = np.linalg.norm(c)

#длинна суммы двух векторов
len_a_b = np.linalg.norm(a + b)
len_b_c = np.linalg.norm(b + c)
len_c_a = np.linalg.norm(c + a)

print(f'a, b: {len_a_b == len_a + len_b}') #False
print(f'b, c: {len_b_c == len_b + len_c}') #False
print(f'c, a: {len_c_a == len_c + len_a}') #True
print('')

#8.5
#Найдите пару векторов, расстояние между которыми больше 100.
#distance = np.sqrt(np.sum((a-b)**2))
dist_a_b = np.linalg.norm(a-b)
dist_b_c = np.linalg.norm(b-c)
dist_a_c = np.linalg.norm(a-c)

print(f'Растояние между векторами a и b больше 100? {100<dist_a_b}')
print(f'Растояние между векторами b и c больше 100? {100<dist_b_c}')
print(f'Растояние между векторами a и c больше 100? {100<dist_a_c}')
print('')

#8.6
#Найдите пару перпендикулярных векторов с помощью скалярного произведения 
# (оно должно быть равно нулю).
#scalar_product = np.sum(a*b)
dot_a_b = np.dot(a,b)
dot_b_c = np.dot(b,c)
dot_a_c = np.dot(a,c)

print(f'Вектора a и b являются перпендикулярными? {dot_a_b == 0}')
print(f'Вектора b и c являются перпендикулярными? {dot_b_c == 0}')
print(f'Вектора a и c являются перпендикулярными? {dot_a_c == 0}')

