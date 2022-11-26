my_list = list(range(0, 100, 3))
s = 0

for i in my_list:
    if i % 2 == 0:
      s+=1

print(s)