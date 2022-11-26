my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
s = 0

for i in my_list:
    if type(i) == str:
        s+=1

print(s)