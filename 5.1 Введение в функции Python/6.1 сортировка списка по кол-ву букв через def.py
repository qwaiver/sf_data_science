#В качестве упражнения попробуйте переписать использованную lambda-функцию в классический вид (с def).
# Назовите её get_length.

new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']

def get_length(new_list):
    return len(new_list)

new_list.sort(key=get_length)

print(new_list)

# Должно быть напечатано:
# ['cc', 'bbb', 'aaa', 'ababa', 'aaaaa']
#names.sort(key=lambda name: len(name))