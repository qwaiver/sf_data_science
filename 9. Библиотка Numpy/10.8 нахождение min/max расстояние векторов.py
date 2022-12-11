#Напишите функцию min_max_dist, которая принимает на вход неограниченное число 
# векторов через запятую. Гарантируется, что все векторы, которые передаются, одинаковой длины.
#Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.

import numpy as np

def min_max_dist(*args):
    lin = []
    a = args[-1]
    for i in args:
       dist = np.linalg.norm(a-i)
       a = i
       lin.append(dist)
    min_max = (np.min(lin), np.max(lin))        
    print(min_max)
        
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)