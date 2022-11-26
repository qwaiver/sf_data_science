#Выполните следующие действия:
#1. Приведите все символы в предложении к нижнему регистру.
#2. Исключите знаки препинания (запятые)
#3. Разделите строку по пробелам и создайте список слов, которые входят в предложение.
#4. Подсчитайте количество повторений каждого слова.
#Для подсчёта слов используйте словарь word_dict. Ключами словаря будут являться слова, а значениями —
# число вхождений этих слов в предложение.
#В результате работы вашей программы в переменной word_dict должен храниться результирующий словарь.

sentence = "A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm" #заданное предложение
word_dict = {} #создаем словарь для посчета количества слов

sentence = sentence.lower()
sentence = sentence.replace(',', '')
sentence = sentence.split(' ')

for word in sentence:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print(word_dict)