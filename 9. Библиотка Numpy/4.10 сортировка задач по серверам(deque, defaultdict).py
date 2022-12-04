#Функция должна создавать словарь и заполнять его задачами по следующему принципу: 
# название сервера — ключ, по которому хранится очередь задач для конкретного сервера. 
# Если поступает задача без высокого приоритета (последний элемент кортежа — False), 
# добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.

from collections import deque, defaultdict

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
def task_manager(tasks):
    task = defaultdict(deque)
    for numb, name, bul in tasks: # x in tasks
        if bul: # if x[-1] #будет равно True/False
            task[name].appendleft(numb) #task[x[1]].appendleft[x[0]]
        else:
            task[name].append(numb)
    return(task)
 
 
 
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})