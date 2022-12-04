#Напишите функцию brackets(line), которая определяет, 
# является ли последовательность из круглых скобок правильной.

from collections import deque
line = deque((')(())'))

def brackets(line):
    l = deque()
    for i in line:
        if i == '(':
            l.append(i)
        elif i == ')':
            try:
                l.pop()
            except IndexError:
                return False
    if l == deque([]):
        return True
    else:
        return False
    
    
print(brackets(line))